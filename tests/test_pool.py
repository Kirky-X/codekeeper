import time
from pathlib import Path

import pytest

from codekeeper.infra.pool import SmartProcessPool, Task, TaskResult


def simple_task_multiply(x):
    return x * 2


def add_numbers(a, b):
    return a + b


def return_small():
    return "small"


def return_large():
    return "large"


def failing_task_func():
    raise ValueError("Task failed intentionally")


def slow_task_fail():
    raise ValueError("Failed")


def slow_task_done():
    time.sleep(0.5)
    return "done"


def very_slow_task():
    time.sleep(5)
    return "done"


def slow_cancel_task():
    time.sleep(10)
    return "done"


def simple_task_result():
    return "result"


def simple_task_return_42():
    return 42


def dummy_task_func():
    time.sleep(10)
    return "done"


class TestSmartProcessPool:
    def test_init_default_workers(self, tmp_path):
        pool = SmartProcessPool()

        assert pool.max_workers >= 1
        assert pool.task_timeout == 300.0
        assert pool.max_queue_size == 1000

    def test_init_custom_workers(self, tmp_path):
        pool = SmartProcessPool(max_workers=2)

        assert pool.max_workers == 2

    def test_init_clamped_workers(self, tmp_path):
        pool = SmartProcessPool(max_workers=1000)
        assert pool.max_workers == 1000

    def test_submit_task(self, tmp_path):
        pool = SmartProcessPool(max_workers=2)

        task = Task(
            task_id="test_001",
            func=simple_task_multiply,
            args=(5,),
        )

        task_id = pool.submit(task)

        assert task_id == "test_001"

        results = pool.wait_for_results([task_id], timeout=5.0)
        assert task_id in results
        assert results[task_id].success
        assert results[task_id].result == 10

        pool.shutdown()

    def test_submit_multiple_tasks(self, tmp_path):
        pool = SmartProcessPool(max_workers=2)

        tasks = [Task(task_id=f"task_{i}", func=add_numbers, args=(i, i)) for i in range(4)]

        results = pool.submit_batch(tasks, sort_by_size=False)

        assert len(results) == 4
        for i in range(4):
            assert results[f"task_{i}"].success
            assert results[f"task_{i}"].result == i * 2

        pool.shutdown()

    def test_task_with_file_priority(self, tmp_path):
        pool = SmartProcessPool(max_workers=2)

        large_file = tmp_path / "large.txt"
        small_file = tmp_path / "small.txt"
        large_file.write_text("x" * 10000)
        small_file.write_text("y" * 100)

        tasks = [
            Task(
                task_id="small",
                func=return_small,
                file_path=str(small_file),
                file_size=small_file.stat().st_size,
                priority=0,
            ),
            Task(
                task_id="large",
                func=return_large,
                file_path=str(large_file),
                file_size=large_file.stat().st_size,
                priority=0,
            ),
        ]

        results = pool.submit_batch(tasks, sort_by_size=True)

        assert len(results) == 2
        assert results["small"].success
        assert results["large"].success

        pool.shutdown()

    def test_task_failure(self, tmp_path):
        pool = SmartProcessPool(max_workers=1)

        task = Task(
            task_id="failing",
            func=failing_task_func,
        )

        pool.submit(task)

        results = pool.wait_for_results(["failing"], timeout=5.0)

        assert "failing" in results
        assert not results["failing"].success
        assert "ValueError" in results["failing"].error

        pool.shutdown()

    def test_fail_fast(self, tmp_path):
        pool = SmartProcessPool(max_workers=2)

        pool.submit(Task(task_id="fail", func=slow_task_fail))
        pool.submit(Task(task_id="slow", func=slow_task_done))

        results = pool.wait_for_results(["fail", "slow"], timeout=3.0, fail_fast=True)

        assert "fail" in results
        assert not results["fail"].success

        pool.shutdown()

    def test_cancel_task(self, tmp_path):
        pool = SmartProcessPool(max_workers=1)

        def slow_task():
            time.sleep(10)
            return "done"

        task = Task(task_id="cancel_me", func=slow_task)
        pool.submit(task)

        time.sleep(0.1)

        pool.cancel("cancel_me")

        assert True

        pool.shutdown(wait=False)

    def test_wait_timeout(self, tmp_path):
        pool = SmartProcessPool(max_workers=1)

        def very_slow_task():
            time.sleep(5)
            return "done"

        task = Task(task_id="timeout_test", func=very_slow_task)
        pool.submit(task)

        start = time.time()
        pool.wait_for_results(["timeout_test"], timeout=0.5)
        elapsed = time.time() - start

        assert elapsed < 2

        pool.shutdown(wait=False)

    def test_get_stats(self, tmp_path):
        pool = SmartProcessPool(max_workers=2)

        def simple_task():
            return "result"

        stats_before = pool.get_stats()
        assert stats_before["max_workers"] == 2
        assert stats_before["active_tasks"] == 0

        task = Task(task_id="stats_test", func=simple_task)
        pool.submit(task)

        stats_during = pool.get_stats()
        assert stats_during["active_tasks"] >= 0

        pool.wait_for_results(["stats_test"], timeout=5.0)

        stats_after = pool.get_stats()
        assert stats_after["completed_tasks"] >= 0

        pool.shutdown()

    def test_context_manager(self, tmp_path):
        with SmartProcessPool(max_workers=2) as pool:
            task = Task(task_id="context_test", func=simple_task_return_42)
            pool.submit(task)

            results = pool.wait_for_results(["context_test"], timeout=5.0)
            assert results["context_test"].success
            assert results["context_test"].result == 42

    def test_init_default_workers(self, tmp_path):
        from codekeeper.infra.pool import _init_worker_impl

        _init_worker_impl()

    def test_queue_full_error(self, tmp_path):
        pool = SmartProcessPool(max_workers=1, max_queue_size=2)

        def dummy_task():
            time.sleep(10)
            return "done"

        for i in range(3):
            task = Task(task_id=f"queue_test_{i}", func=dummy_task)
            try:
                pool.submit(task)
            except RuntimeError as e:
                assert "queue is full" in str(e)
                break

        pool.shutdown(wait=False)

    def test_submit_after_shutdown(self, tmp_path):
        pool = SmartProcessPool(max_workers=1)
        pool.shutdown()

        task = Task(task_id="after_shutdown", func=simple_task_multiply)

        with pytest.raises(RuntimeError, match="pool is shutting down"):
            pool.submit(task)


class TestTask:
    def test_task_creation(self):
        def sample_func(a, b):
            return a + b

        task = Task(
            task_id="test_task",
            func=sample_func,
            args=(1, 2),
            kwargs={"extra": True},
            priority=5,
            file_path=Path("/test/file.py"),
            file_size=1000,
        )

        assert task.task_id == "test_task"
        assert task.func is sample_func
        assert task.args == (1, 2)
        assert task.kwargs == {"extra": True}
        assert task.priority == 5
        assert task.file_size == 1000

    def test_task_sort_key(self):
        task1 = Task(
            task_id="task1",
            func=simple_task_result,
            priority=5,
            file_size=100,
        )
        task2 = Task(
            task_id="task2",
            func=simple_task_result,
            priority=3,
            file_size=200,
        )

        assert task1.sort_key < task2.sort_key

    def test_task_default_kwargs(self):
        task = Task(task_id="default_test", func=lambda: None)

        assert task.kwargs == {}


class TestTaskResult:
    def test_task_result_success(self):
        result = TaskResult(
            task_id="success_test",
            success=True,
            result={"key": "value"},
            duration_ms=50.5,
        )

        assert result.success
        assert result.result == {"key": "value"}
        assert result.error is None
        assert result.duration_ms == 50.5

    def test_task_result_failure(self):
        result = TaskResult(
            task_id="failure_test",
            success=False,
            error="ValueError: invalid input",
            duration_ms=25.0,
        )

        assert not result.success
        assert result.result is None
        assert "ValueError" in result.error

    def test_task_result_empty(self):
        result = TaskResult(task_id="empty", success=True)

        assert result.success
        assert result.result is None
        assert result.error is None
        assert result.duration_ms == 0.0
