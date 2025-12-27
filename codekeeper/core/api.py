import logging
from pathlib import Path

from codekeeper.core.annotation import AnnotationResult, AnnotationScanner
from codekeeper.core.clean import CleanManager, CleanResult, CleanStats, JunkFile
from codekeeper.core.copyright import CopyrightManager, CopyrightResult, OverwriteMode
from codekeeper.infra.apm import APMVendor, get_apm_integration
from codekeeper.infra.metrics import get_monitor
from codekeeper.languages.base import FunctionInfo
from codekeeper.security import (
    InvalidPathError,
    PathValidator,
    is_safe_path,
)

logger = logging.getLogger(__name__)


class CodeKeeper:
    """Main entry point for CodeKeeper operations."""

    def __init__(
            self,
            root_dir: Path | None = None,
            config_path: Path | None = None,
            apm_enabled: bool = True,
            apm_vendor: str = "custom",
    ):
        """Initialize CodeKeeper.

        Args:
            root_dir: Root directory of the project
            config_path: Path to configuration file
            apm_enabled: Whether to enable APM integration
            apm_vendor: APM vendor (datadog, prometheus, opentelemetry, custom)
        """
        self.root_dir = root_dir or Path.cwd()
        self.config_path = config_path
        self.path_validator = PathValidator(self.root_dir)
        self._monitor = get_monitor()
        self._apm = get_apm_integration(
            vendor=APMVendor(apm_vendor) if apm_vendor else APMVendor.CUSTOM,
            service_name="codekeeper",
            enabled=apm_enabled,
        )

        logger.info(f"CodeKeeper initialized with root: {self.root_dir}")

    def initialize_apm(self, config: dict) -> None:
        """Initialize APM with configuration.

        Args:
            config: APM configuration dictionary
        """
        self._apm.initialize(config)
        logger.info(f"APM integration initialized with vendor: {self._apm.vendor.value}")

    def get_performance_summary(self) -> dict:
        """Get performance monitoring summary.

        Returns:
            Performance metrics dictionary
        """
        return self._monitor.get_summary()

    def get_apm_report(self) -> dict:
        """Get APM report.

        Returns:
            APM report dictionary
        """
        return self._apm.get_report()

    def flush_apm(self) -> None:
        """Flush APM data.

        This should be called periodically to send metrics to the APM backend.
        """
        self._apm.flush()

    def scan(self, recursive: bool = True) -> list[Path]:
        """Scan for code files.

        Args:
            recursive: Whether to scan recursively

        Returns:
            List of file paths

        Raises:
            InvalidPathError: If root directory is invalid
        """
        if not self.root_dir.exists():
            raise InvalidPathError(f"Root directory does not exist: {self.root_dir}")

        if not is_safe_path(self.root_dir):
            raise InvalidPathError(f"Root directory is not safe: {self.root_dir}")

        from codekeeper.utils.file import scan_files

        with self._monitor.measure_operation("codekeeper.scan"):
            self._apm.start_trace("scan_files", {"recursive": str(recursive)})
            try:
                result = scan_files(self.root_dir, recursive=recursive)
                self._apm.end_trace(self._apm._current_trace_id or "", status="ok")
                return result
            except Exception as e:
                self._apm.end_trace(
                    self._apm._current_trace_id or "", status="error", error_message=str(e)
                )
                raise

    def analyze(self, file_path: Path) -> dict:
        """Analyze a single file.

        Args:
            file_path: Path to the file

        Returns:
            Analysis result dictionary

        Raises:
            InvalidPathError: If file path is invalid
            PathTraversalError: If path traversal attack detected
        """
        if not is_safe_path(file_path, self.root_dir):
            raise InvalidPathError(f"Invalid or unsafe file path: {file_path}")

        with self._monitor.measure_operation("codekeeper.analyze"):
            self._apm.start_trace("analyze_file", {"path": str(file_path)})
            try:
                result = {"path": str(file_path), "language": "unknown"}
                self._apm.end_trace(self._apm._current_trace_id or "", status="ok")
                return result
            except Exception as e:
                self._apm.end_trace(
                    self._apm._current_trace_id or "", status="error", error_message=str(e)
                )
                raise

    def add_copyright_headers(
            self,
            recursive: bool = True,
            license_type: str = "MIT",
            author: str | None = None,
            year_range: str | None = None,
            overwrite_mode: OverwriteMode = OverwriteMode.UPDATE_YEAR,
            skip_if_exists: bool = True,
            extensions: list[str] | None = None,
    ) -> list[CopyrightResult]:
        """Add copyright headers to all supported files in the project.

        Args:
            recursive: Whether to scan recursively
            license_type: License type to use (mit, apache-2.0, gpl-3.0, bsd-3-clause)
            author: Copyright author name
            year_range: Year range (e.g., "2023-2025")
            overwrite_mode: How to handle existing copyright headers
            skip_if_exists: Skip files that already have copyright headers
            extensions: File extensions to process (default: all supported)

        Returns:
            List of CopyrightResult objects
        """
        with self._monitor.measure_operation("codekeeper.add_copyright"):
            self._apm.start_trace(
                "add_copyright_headers",
                {
                    "recursive": str(recursive),
                    "license": license_type,
                },
            )
            try:
                files = self.scan(recursive=recursive)

                if extensions:
                    files = [f for f in files if f.suffix.lstrip(".") in extensions]

                copyright_manager = CopyrightManager(
                    author=author,
                    license=license,
                    year_range=year_range,
                    overwrite_mode=overwrite_mode,
                    skip_if_exists=skip_if_exists,
                )

                results = []
                for file_path in files:
                    result = copyright_manager.add_copyright(file_path)
                    results.append(result)

                self._apm.end_trace(self._apm._current_trace_id or "", status="ok")
                return results
            except Exception as e:
                self._apm.end_trace(
                    self._apm._current_trace_id or "", status="error", error_message=str(e)
                )
                raise

    def remove_copyright_headers(
            self,
            recursive: bool = True,
            extensions: list[str] | None = None,
    ) -> list[CopyrightResult]:
        """Remove copyright headers from all supported files in the project.

        Args:
            recursive: Whether to scan recursively
            extensions: File extensions to process (default: all supported)

        Returns:
            List of CopyrightResult objects
        """
        with self._monitor.measure_operation("codekeeper.remove_copyright"):
            self._apm.start_trace("remove_copyright_headers", {"recursive": str(recursive)})
            try:
                files = self.scan(recursive=recursive)

                if extensions:
                    files = [f for f in files if f.suffix.lstrip(".") in extensions]

                copyright_manager = CopyrightManager(
                    skip_if_exists=False,
                )

                results = []
                for file_path in files:
                    result = copyright_manager.remove_copyright(file_path)
                    results.append(result)

                self._apm.end_trace(self._apm._current_trace_id or "", status="ok")
                return results
            except Exception as e:
                self._apm.end_trace(
                    self._apm._current_trace_id or "", status="error", error_message=str(e)
                )
                raise

    def validate_copyright_headers(
            self,
            recursive: bool = True,
            extensions: list[str] | None = None,
    ) -> list[CopyrightResult]:
        """Validate copyright headers in all supported files.

        Args:
            recursive: Whether to scan recursively
            extensions: File extensions to process (default: all supported)

        Returns:
            List of CopyrightResult objects with validation status
        """
        with self._monitor.measure_operation("codekeeper.validate_copyright"):
            self._apm.start_trace("validate_copyright_headers", {"recursive": str(recursive)})
            try:
                files = self.scan(recursive=recursive)

                if extensions:
                    files = [f for f in files if f.suffix.lstrip(".") in extensions]

                copyright_manager = CopyrightManager()

                results = []
                for file_path in files:
                    result = copyright_manager.validate_copyright(file_path)
                    results.append(result)

                self._apm.end_trace(self._apm._current_trace_id or "", status="ok")
                return results
            except Exception as e:
                self._apm.end_trace(
                    self._apm._current_trace_id or "", status="error", error_message=str(e)
                )
                raise

    def clean_junk_files(
            self,
            paths: list[Path] | None = None,
            recursive: bool = True,
            confirm: bool = False,
    ) -> tuple[list[CleanResult], CleanStats]:
        """Scan and optionally clean junk files.

        Args:
            paths: Paths to scan (default: root_dir)
            recursive: Whether to scan recursively
            confirm: Whether to actually remove files (False = preview mode)

        Returns:
            Tuple of (CleanResult list, CleanStats)

        Raises:
            InvalidPathError: If any path is invalid
            PathTraversalError: If path traversal attack detected
        """
        with self._monitor.measure_operation("codekeeper.clean_junk"):
            self._apm.start_trace(
                "clean_junk_files",
                {
                    "recursive": str(recursive),
                    "confirm": str(confirm),
                },
            )
            try:
                scan_paths = paths or [self.root_dir]

                for path in scan_paths:
                    if not path.is_absolute():
                        path = self.root_dir / path
                    if not is_safe_path(path, self.root_dir):
                        raise InvalidPathError(f"Invalid or unsafe path: {path}")

                clean_manager = CleanManager()
                result = clean_manager.clean(scan_paths, recursive, confirm, self.root_dir)

                self._apm.end_trace(self._apm._current_trace_id or "", status="ok")
                return result
            except Exception as e:
                self._apm.end_trace(
                    self._apm._current_trace_id or "", status="error", error_message=str(e)
                )
                raise

    def preview_junk_files(
            self,
            paths: list[Path] | None = None,
            recursive: bool = True,
    ) -> tuple[list[JunkFile], CleanStats]:
        """Preview junk files that would be cleaned.

        Args:
            paths: Paths to scan (default: root_dir)
            recursive: Whether to scan recursively

        Returns:
            Tuple of (JunkFile list, CleanStats)

        Raises:
            InvalidPathError: If any path is invalid
            PathTraversalError: If path traversal attack detected
        """
        with self._monitor.measure_operation("codekeeper.preview_junk"):
            self._apm.start_trace("preview_junk_files", {"recursive": str(recursive)})
            try:
                scan_paths = paths or [self.root_dir]

                for path in scan_paths:
                    if not path.is_absolute():
                        path = self.root_dir / path
                    if not is_safe_path(path, self.root_dir):
                        raise InvalidPathError(f"Invalid or unsafe path: {path}")

                clean_manager = CleanManager()
                result = clean_manager.preview(scan_paths, recursive, self.root_dir)

                self._apm.end_trace(self._apm._current_trace_id or "", status="ok")
                return result
            except Exception as e:
                self._apm.end_trace(
                    self._apm._current_trace_id or "", status="error", error_message=str(e)
                )
                raise

    def register_junk_pattern(
            self,
            pattern: str,
            name: str | None = None,
            _description: str = "",
            _severity: str = "low",
    ) -> None:
        """Register a custom junk file pattern.

        Args:
            pattern: Regex pattern for matching files
            name: Pattern name (auto-generated if not provided)
            _description: Pattern description
            _severity: Pattern severity (low, medium, high)
        """
        with self._monitor.measure_operation("codekeeper.register_pattern"):
            self._apm.start_trace("register_junk_pattern", {"pattern": pattern[:100]})
            try:
                clean_manager = CleanManager()
                clean_manager.add_custom_pattern(pattern, name)
                logger.info(f"Registered custom junk pattern: {name or pattern}")
                self._apm.end_trace(self._apm._current_trace_id or "", status="ok")
            except Exception as e:
                self._apm.end_trace(
                    self._apm._current_trace_id or "", status="error", error_message=str(e)
                )
                raise

    def scan_function_annotations(
            self,
            recursive: bool = True,
            skip_private: bool = False,
            skip_dunder: bool = True,
            extensions: list[str] | None = None,
    ) -> list[AnnotationResult]:
        """Scan for functions with missing annotations/comments.

        Args:
            recursive: Whether to scan recursively
            skip_private: Whether to skip private functions (starting with _)
            skip_dunder: Whether to skip dunder methods (starting and ending with __)
            extensions: File extensions to process (default: all supported)

        Returns:
            List of AnnotationResult objects
        """
        with self._monitor.measure_operation("codekeeper.scan_annotations"):
            self._apm.start_trace("scan_function_annotations", {"recursive": str(recursive)})
            try:
                files = self.scan(recursive=recursive)

                if extensions:
                    files = [f for f in files if f.suffix.lstrip(".") in extensions]

                scanner = AnnotationScanner(
                    skip_private=skip_private,
                    skip_dunder=skip_dunder,
                )

                results = []
                for file_path in files:
                    if str(file_path).endswith(".py"):
                        result = scanner.scan_python_file(file_path)
                        if result.functions_found > 0:
                            results.append(result)

                self._apm.end_trace(self._apm._current_trace_id or "", status="ok")
                return results
            except Exception as e:
                self._apm.end_trace(
                    self._apm._current_trace_id or "", status="error", error_message=str(e)
                )
                raise

    def get_missing_annotations(
            self,
            recursive: bool = True,
            skip_private: bool = False,
            skip_dunder: bool = True,
            extensions: list[str] | None = None,
    ) -> list[FunctionInfo]:
        """Get list of functions that are missing comments/annotations.

        Args:
            recursive: Whether to scan recursively
            skip_private: Whether to skip private functions
            skip_dunder: Whether to skip dunder methods
            extensions: File extensions to process

        Returns:
            List of FunctionInfo objects for functions without comments
        """
        with self._monitor.measure_operation("codekeeper.get_missing_annotations"):
            self._apm.start_trace("get_missing_annotations", {"recursive": str(recursive)})
            try:
                results = self.scan_function_annotations(
                    recursive=recursive,
                    skip_private=skip_private,
                    skip_dunder=skip_dunder,
                    extensions=extensions,
                )

                missing = []
                for result in results:
                    missing.extend(result.missing_comments)

                self._apm.end_trace(self._apm._current_trace_id or "", status="ok")
                return missing
            except Exception as e:
                self._apm.end_trace(
                    self._apm._current_trace_id or "", status="error", error_message=str(e)
                )
                raise

    def annotation_summary(
            self,
            recursive: bool = True,
            extensions: list[str] | None = None,
    ) -> dict:
        """Get summary of annotation coverage.

        Args:
            recursive: Whether to scan recursively
            extensions: File extensions to process

        Returns:
            Summary dictionary with annotation statistics
        """
        with self._monitor.measure_operation("codekeeper.annotation_summary"):
            self._apm.start_trace("annotation_summary", {"recursive": str(recursive)})
            try:
                results = self.scan_function_annotations(
                    recursive=recursive,
                    extensions=extensions,
                )

                total_functions = sum(r.functions_found for r in results)
                with_comments = sum(r.functions_with_comments for r in results)
                without_comments = sum(r.functions_without_comments for r in results)

                coverage = 0.0
                if total_functions > 0:
                    coverage = (with_comments / total_functions) * 100

                summary = {
                    "files_scanned": len(results),
                    "total_functions": total_functions,
                    "functions_with_comments": with_comments,
                    "functions_without_comments": without_comments,
                    "annotation_coverage_percent": round(coverage, 2),
                }

                self._apm.end_trace(self._apm._current_trace_id or "", status="ok")
                return summary
            except Exception as e:
                self._apm.end_trace(
                    self._apm._current_trace_id or "", status="error", error_message=str(e)
                )
                raise
