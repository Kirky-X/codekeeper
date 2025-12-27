import logging
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import ClassVar

logger = logging.getLogger(__name__)


class JunkType(Enum):
    EDITOR_TEMP = "editor_temp"
    OS_CACHE = "os_cache"
    PYTHON_CACHE = "python_cache"
    BUILD_ARTIFACT = "build_artifact"
    EMPTY_FILE = "empty_file"
    ORPHAN_FILE = "orphan_file"
    LOG_FILE = "log_file"
    UNKNOWN = "unknown"


@dataclass
class JunkFile:
    file_path: Path
    junk_type: JunkType
    size_bytes: int = 0
    modified_time: float = 0
    reason: str = ""


@dataclass
class CleanResult:
    file_path: Path
    success: bool
    action: str
    message: str
    junk_type: JunkType | None = None
    original_size: int = 0


@dataclass
class CleanStats:
    total_scanned: int = 0
    total_junk_found: int = 0
    total_size_bytes: int = 0
    files_deleted: int = 0
    bytes_freed: int = 0
    errors: int = 0
    junk_by_type: dict[JunkType, int] = field(default_factory=dict)
    junk_by_type_bytes: dict[JunkType, int] = field(default_factory=dict)

    def add_junk(self, junk: JunkFile) -> None:
        self.total_junk_found += 1
        self.total_size_bytes += junk.size_bytes
        self.junk_by_type[junk.junk_type] = self.junk_by_type.get(junk.junk_type, 0) + 1
        self.junk_by_type_bytes[junk.junk_type] = (
                self.junk_by_type_bytes.get(junk.junk_type, 0) + junk.size_bytes
        )

    def record_deletion(self, size_bytes: int) -> None:
        self.files_deleted += 1
        self.bytes_freed += size_bytes

    def to_dict(self) -> dict:
        return {
            "total_scanned": self.total_scanned,
            "total_junk_found": self.total_junk_found,
            "total_size_mb": round(self.total_size_bytes / (1024 * 1024), 2),
            "files_deleted": self.files_deleted,
            "bytes_freed": self.bytes_freed,
            "errors": self.errors,
            "junk_by_type": {kt.value: count for kt, count in self.junk_by_type.items()},
            "junk_by_type_bytes": {kt.value: size for kt, size in self.junk_by_type_bytes.items()},
        }


class CleanManager:
    EDITOR_TEMP_PATTERNS: ClassVar[set[str]] = {
        r".*~$",
        r".*\.swp$",
        r".*\.swo$",
        r".*\.bak$",
        r".*\.orig$",
        r".*\.rej$",
        r".*\#.*\#",
        r".*~",
        r".*\.tmp$",
    }

    OS_CACHE_PATTERNS: ClassVar[set[str]] = {
        ".DS_Store",
        "Thumbs.db",
        "desktop.ini",
        ".Spotlight-V100",
        ".Trashes",
        "ehthumbs.db",
        "SyncIgnore",
    }

    PYTHON_CACHE_PATTERNS: ClassVar[set[str]] = {
        "__pycache__",
        "*.pyc",
        "*.pyo",
        "*.pyd",
        ".Python",
        "*.so",
        "*.egg",
        "*.egg-info",
        "*.egg-info/",
        "dist/",
        "build/",
        ".eggs/",
    }

    BUILD_ARTIFACT_PATTERNS: ClassVar[set[str]] = {
        "*.o",
        "*.obj",
        "*.a",
        "*.lib",
        "*.so",
        "*.dylib",
        "*.dll",
        "*.exe",
        "*.pdb",
        "*.idb",
        "*.ilk",
        "*.meta",
        "*.wasm",
        "node_modules/",
        ".next/",
        ".nuxt/",
        ".cache/",
        ".parcel-cache/",
        ".vite/",
    }

    LOG_FILE_PATTERNS: ClassVar[set[str]] = {
        "*.log",
        "*.tmp",
        "nohup.out",
    }

    def __init__(
            self,
            dry_run: bool = True,
            check_empty_files: bool = True,
            empty_file_threshold: int = 0,
            exclude_patterns: list[str] | None = None,
            exclude_paths: list[Path] | None = None,
    ):
        self.dry_run = dry_run
        self.check_empty_files = check_empty_files
        self.empty_file_threshold = empty_file_threshold
        self.exclude_patterns = exclude_patterns or []
        self.exclude_paths = exclude_paths or []

    def _should_exclude(self, file_path: Path) -> bool:
        for pattern in self.exclude_patterns:
            if pattern in str(file_path):
                return True
        for exclude_path in self.exclude_paths:
            try:
                if file_path.is_relative_to(exclude_path):
                    return True
            except TypeError:
                pass
        return False

    def _determine_junk_type(self, _file_path: Path, name: str) -> JunkType | None:
        if name.startswith("."):
            if name in self.OS_CACHE_PATTERNS:
                return JunkType.OS_CACHE
            if name in ("__pycache__",):
                return JunkType.PYTHON_CACHE
            if name in ("node_modules", ".next", ".nuxt", ".cache", ".parcel-cache", ".vite"):
                return JunkType.BUILD_ARTIFACT
            if name.endswith(".log"):
                return JunkType.LOG_FILE

        for pattern in self.EDITOR_TEMP_PATTERNS:
            import re

            if re.match(pattern, name):
                return JunkType.EDITOR_TEMP

        if name.endswith(".pyc") or name.endswith(".pyo"):
            return JunkType.PYTHON_CACHE

        if name in ("__pycache__", ".pytest_cache", ".tox", ".nox"):
            return JunkType.PYTHON_CACHE

        for pattern in self.BUILD_ARTIFACT_PATTERNS:
            if pattern.endswith("/") and name == pattern.rstrip("/"):
                return JunkType.BUILD_ARTIFACT
            if "*" in pattern and name.endswith(pattern[1:]):
                return JunkType.BUILD_ARTIFACT

        if name.endswith(".log"):
            return JunkType.LOG_FILE

        return None

    def _is_empty_file(self, file_path: Path) -> bool:
        if self.empty_file_threshold > 0:
            try:
                return file_path.stat().st_size <= self.empty_file_threshold
            except OSError:
                return False
        try:
            return file_path.stat().st_size == 0
        except OSError:
            return False

    def scan_directory(self, directory: Path, recursive: bool = True) -> list[JunkFile]:
        junk_files: list[JunkFile] = []

        try:
            iterator = directory.rglob("*") if recursive else directory.glob("*")
        except (OSError, PermissionError) as e:
            logger.warning(f"Cannot access directory {directory}: {e}")
            return junk_files

        for item in iterator:
            try:
                if not item.is_file():
                    continue

                if self._should_exclude(item):
                    continue

                junk_type = self._determine_junk_type(item, item.name)

                if junk_type:
                    try:
                        size = item.stat().st_size
                        mtime = item.stat().st_mtime
                    except (OSError, PermissionError):
                        size = 0
                        mtime = 0

                    junk_files.append(
                        JunkFile(
                            file_path=item,
                            junk_type=junk_type,
                            size_bytes=size,
                            modified_time=mtime,
                            reason=f"Detected as {junk_type.value}",
                        )
                    )
                elif self.check_empty_files and self._is_empty_file(item):
                    try:
                        size = item.stat().st_size
                    except (OSError, PermissionError):
                        size = 0
                    junk_files.append(
                        JunkFile(
                            file_path=item,
                            junk_type=JunkType.EMPTY_FILE,
                            size_bytes=size,
                            reason="Empty file",
                        )
                    )

            except (OSError, PermissionError) as e:
                logger.warning(f"Cannot process file {item}: {e}")
                continue

        return junk_files

    def clean_junk_file(self, junk: JunkFile) -> CleanResult:
        file_path = junk.file_path

        try:
            size = file_path.stat().st_size
        except (OSError, PermissionError):
            size = 0

        if self.dry_run:
            return CleanResult(
                file_path=file_path,
                success=True,
                action="skip (dry run)",
                message=f"Would delete {file_path}",
                junk_type=junk.junk_type,
                original_size=size,
            )

        try:
            file_path.unlink()
            return CleanResult(
                file_path=file_path,
                success=True,
                action="deleted",
                message=f"Successfully deleted {file_path}",
                junk_type=junk.junk_type,
                original_size=size,
            )
        except (OSError, PermissionError) as e:
            return CleanResult(
                file_path=file_path,
                success=False,
                action="error",
                message=f"Failed to delete {file_path}: {e}",
                junk_type=junk.junk_type,
                original_size=size,
            )

    def clean_directory(
            self,
            directory: Path,
            recursive: bool = True,
            junk_types: list[JunkType] | None = None,
    ) -> tuple[list[CleanResult], CleanStats]:
        junk_files = self.scan_directory(directory, recursive)

        if junk_types:
            junk_files = [j for j in junk_files if j.junk_type in junk_types]

        results: list[CleanResult] = []
        stats = CleanStats(total_scanned=len(junk_files))

        for junk in junk_files:
            stats.add_junk(junk)
            result = self.clean_junk_file(junk)
            results.append(result)
            if result.success and result.action == "deleted":
                stats.record_deletion(result.original_size)
            elif not result.success:
                stats.errors += 1

        return results, stats

    def scan_and_report(
            self, directory: Path, recursive: bool = True
    ) -> tuple[list[JunkFile], CleanStats]:
        junk_files = self.scan_directory(directory, recursive)

        stats = CleanStats(total_scanned=len(junk_files))
        for junk in junk_files:
            stats.add_junk(junk)

        return junk_files, stats

    def get_junk_summary(self, junk_files: list[JunkFile]) -> dict:
        summary: dict = {
            "total_count": len(junk_files),
            "by_type": {},
            "total_size_bytes": 0,
        }

        for junk in junk_files:
            junk_type_value = junk.junk_type.value
            if junk_type_value not in summary["by_type"]:
                summary["by_type"][junk_type_value] = {"count": 0, "size_bytes": 0}
            summary["by_type"][junk_type_value]["count"] += 1
            summary["by_type"][junk_type_value]["size_bytes"] += junk.size_bytes
            summary["total_size_bytes"] += junk.size_bytes

        summary["total_size_mb"] = round(summary["total_size_bytes"] / (1024 * 1024), 2)

        return summary
