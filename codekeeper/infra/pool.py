import logging
import multiprocessing
import os
import signal
import sys
import time
from collections.abc import Callable
from concurrent.futures import Future, ProcessPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from typing import Any, TypeVar

logger = logging.getLogger(__name__)

T = TypeVar("T")


@dataclass
class TaskResult:
    task_id: str
    success: bool
    result: Any = None
    error: str | None = None
    duration_ms: float = 0.0


@dataclass
class Task:
    task_id: str
    func: Callable[..., T]
    args: tuple = ()
    kwargs: dict = None
    priority: int = 0
    file_path: str | None = None
    file_size: int = 0

    def __post_init__(self):
        if self.kwargs is None:
            self.kwargs = {}

    @property
    def sort_key(self) -> tuple:
        return (-self.priority, -self.file_size, self.task_id)


def _init_worker_impl() -> None:
    """Initialize worker process (module-level function for pickle compatibility)."""
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGTERM, signal.SIG_DFL)


def _execute_task_impl(task: Task, task_timeout: float) -> TaskResult:
    """Execute a single task (module-level function for pickle compatibility).

    Args:
        task: Task to execute
        task_timeout: Timeout for task execution in milliseconds

    Returns:
        TaskResult with execution outcome
    """
    import signal

    start_time = time.time()
    timeout_secs = task_timeout / 1000.0

    def run_with_timeout():
        def timeout_handler(signum, frame):
            raise TimeoutError(f"Task execution exceeded {task_timeout}ms")

        old_handler = signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(int(timeout_secs) + 1)

        try:
            return task.func(*task.args, **task.kwargs)
        finally:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old_handler)

    try:
        if task.file_path and Path(task.file_path).exists():
            os.nice(10)

        if task_timeout > 0:
            result = run_with_timeout()
        else:
            result = task.func(*task.args, **task.kwargs)

        duration_ms = (time.time() - start_time) * 1000
        return TaskResult(
            task_id=task.task_id,
            success=True,
            result=result,
            duration_ms=duration_ms,
        )

    except Exception as e:
        duration_ms = (time.time() - start_time) * 1000
        error_msg = f"{type(e).__name__}: {e!s}"
        return TaskResult(
            task_id=task.task_id,
            success=False,
            error=error_msg,
            duration_ms=duration_ms,
        )


class SmartProcessPool:
    """Smart process pool with dynamic worker management."""

    def __init__(
            self,
            max_workers: int | None = None,
            task_timeout: float = 300.0,
            max_queue_size: int = 1000,
    ):
        """Initialize the smart process pool.

        Args:
            max_workers: Maximum number of worker processes (None = auto-detect)
            task_timeout: Timeout for individual tasks in seconds
            max_queue_size: Maximum size of task queue
        """
        self.max_workers = self._detect_optimal_workers(max_workers)
        self.task_timeout = task_timeout
        self.max_queue_size = max_queue_size
        self._executor: ProcessPoolExecutor | None = None
        self._pending_tasks: dict[str, Future] = {}
        self._task_counter = 0
        self._shutdown_requested = False

        logger.info(
            f"SmartProcessPool initialized with {self.max_workers} workers, "
            f"timeout={task_timeout}s, queue_size={max_queue_size}"
        )

    def _detect_optimal_workers(self, requested: int | None) -> int:
        """Detect optimal number of workers based on CPU cores.

        Args:
            requested: Requested number of workers (None for auto)

        Returns:
            Optimal number of workers
        """
        physical_cores = self._get_physical_cores()
        logical_cores = multiprocessing.cpu_count()

        if requested is not None:
            requested = max(1, requested)
            logger.info(
                f"Using requested worker count: {requested} "
                f"(physical cores: {physical_cores}, logical: {logical_cores})"
            )
            return requested

        optimal = max(1, physical_cores - 1)
        logger.info(
            f"Auto-detected optimal workers: {optimal} "
            f"(physical cores: {physical_cores}, reserving 1 for main process)"
        )
        return optimal

    def _get_physical_cores(self) -> int:
        """Get number of physical CPU cores.

        Returns:
            Number of physical CPU cores
        """
        try:
            if sys.platform == "linux":
                with open("/proc/cpuinfo") as f:
                    cpuinfo = f.read()
                    physical_ids = cpuinfo.count("physical id")
                    if physical_ids > 0:
                        core_counts = cpuinfo.split("physical id")
                        return len([p for p in core_counts[1:] if "physical id\t:" in p])
                    siblings = cpuinfo.split("siblings")
                    if len(siblings) > 1:
                        return int(siblings[1].split("\n")[0].split(":")[1].strip())
            elif sys.platform == "darwin":
                import subprocess

                result = subprocess.run(
                    ["sysctl", "-n", "hw.physicalcpu"],
                    capture_output=True,
                    text=True,
                )
                if result.returncode == 0:
                    return int(result.stdout.strip())
            elif sys.platform == "win32":
                import subprocess

                result = subprocess.run(
                    ["wmic", "CPU", "Get", "NumberOfCores", "/value"],
                    capture_output=True,
                    text=True,
                )
                if result.returncode == 0:
                    cores = [
                        line.split("=")[1]
                        for line in result.stdout.strip().split("\n")
                        if "NumberOfCores=" in line
                    ]
                    return sum(int(c) for c in cores)
        except Exception as e:
            logger.warning(f"Failed to detect physical cores: {e}")

        return multiprocessing.cpu_count()

    def _start_executor(self) -> None:
        """Start the process pool executor."""
        ctx = multiprocessing.get_context("spawn")
        self._executor = ProcessPoolExecutor(
            max_workers=self.max_workers,
            initializer=_init_worker_impl,
            mp_context=ctx,
        )

    def submit(self, task: Task) -> str:
        """Submit a task to the pool.

        Args:
            task: Task to execute

        Returns:
            Task ID

        Raises:
            RuntimeError: If pool is shutdown or queue is full
        """
        if self._shutdown_requested:
            raise RuntimeError("Cannot submit task: pool is shutting down")

        if len(self._pending_tasks) >= self.max_queue_size:
            raise RuntimeError(f"Task queue is full (max: {self.max_queue_size})")

        if not self._executor:
            self._start_executor()

        task_id = task.task_id
        future = self._executor.submit(_execute_task_impl, task, self.task_timeout * 1000)
        self._pending_tasks[task_id] = future

        logger.debug(f"Task submitted: {task_id}")
        return task_id

    def submit_batch(
            self,
            tasks: list[Task],
            sort_by_size: bool = True,
            fail_fast: bool = False,
    ) -> dict[str, TaskResult]:
        """Submit multiple tasks to the pool.

        Args:
            tasks: List of tasks to execute
            sort_by_size: Sort tasks by size (large files first)
            fail_fast: Stop on first error

        Returns:
            Dictionary mapping task_id to TaskResult
        """
        if sort_by_size:
            tasks = sorted(tasks, key=lambda t: t.sort_key)

        results = {}

        for task in tasks:
            task_id = self.submit(task)
            results[task_id] = None

        return self.wait_for_results(results.keys(), fail_fast=fail_fast)

    def wait_for_results(
            self,
            task_ids: list[str],
            timeout: float | None = None,
            fail_fast: bool = False,
    ) -> dict[str, TaskResult]:
        """Wait for tasks to complete.

        Args:
            task_ids: List of task IDs to wait for
            timeout: Maximum time to wait (None = infinite)
            fail_fast: Stop waiting on first failure

        Returns:
            Dictionary mapping task_id to TaskResult
        """
        results = {}
        pending_ids = set(task_ids)

        start_time = time.time()

        while pending_ids:
            if timeout is not None:
                elapsed = time.time() - start_time
                remaining = timeout - elapsed
                if remaining <= 0:
                    for task_id in pending_ids:
                        results[task_id] = TaskResult(
                            task_id=task_id,
                            success=False,
                            error="Timeout",
                            duration_ms=timeout * 1000,
                        )
                    return results
            else:
                remaining = None

            done_ids = set()
            for task_id in pending_ids:
                future = self._pending_tasks.get(task_id)
                if future is None:
                    done_ids.add(task_id)
                    continue

                try:
                    if remaining is not None:
                        result = future.result(timeout=remaining)
                    else:
                        result = future.result(timeout=1.0)
                    results[task_id] = result
                    done_ids.add(task_id)

                    if fail_fast and not result.success:
                        for remaining_id in pending_ids - done_ids:
                            self.cancel(remaining_id)
                        break

                except TimeoutError:
                    continue
                except Exception as e:
                    logger.error(f"Unexpected error waiting for {task_id}: {e}")
                    results[task_id] = TaskResult(
                        task_id=task_id,
                        success=False,
                        error=f"Unexpected error: {type(e).__name__}",
                    )
                    done_ids.add(task_id)

            pending_ids -= done_ids

        for task_id in task_ids:
            if task_id not in results:
                future = self._pending_tasks.get(task_id)
                if future:
                    try:
                        results[task_id] = future.result(timeout=1.0)
                    except Exception:
                        pass

        return results

    def cancel(self, task_id: str) -> bool:
        """Cancel a pending task.

        Args:
            task_id: ID of task to cancel

        Returns:
            True if cancelled, False if not found or already running
        """
        future = self._pending_tasks.get(task_id)
        if future and future.cancel():
            del self._pending_tasks[task_id]
            logger.info(f"Task cancelled: {task_id}")
            return True
        return False

    def get_stats(self) -> dict[str, Any]:
        """Get pool statistics.

        Returns:
            Dictionary with pool statistics
        """
        active_count = sum(1 for f in self._pending_tasks.values() if not f.done())
        completed_count = sum(1 for f in self._pending_tasks.values() if f.done())

        return {
            "max_workers": self.max_workers,
            "active_tasks": active_count,
            "completed_tasks": completed_count,
            "pending_tasks": len(self._pending_tasks) - active_count - completed_count,
            "shutdown": self._shutdown_requested,
        }

    def shutdown(self, wait: bool = True) -> None:
        """Shutdown the process pool.

        Args:
            wait: Wait for pending tasks to complete
        """
        if self._shutdown_requested:
            return

        self._shutdown_requested = True
        logger.info("Shutting down SmartProcessPool...")

        if self._executor:
            self._executor.shutdown(wait=wait, cancel_futures=not wait)

        self._pending_tasks.clear()
        self._executor = None

        logger.info("SmartProcessPool shutdown complete")

    def __enter__(self) -> "SmartProcessPool":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.shutdown(wait=True)
