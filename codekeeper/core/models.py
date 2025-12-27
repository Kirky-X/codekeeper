from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class ProcessingResult:
    file_path: Path
    success: bool
    action: str
    error: str | None = None
    details: dict | None = None

    def to_dict(self) -> dict:
        return {
            "file_path": str(self.file_path),
            "success": self.success,
            "action": self.action,
            "error": self.error,
            "details": self.details,
        }


@dataclass
class BatchResult:
    total_files: int
    success_count: int
    failure_count: int
    skipped_count: int
    results: list[ProcessingResult]

    def to_dict(self) -> dict:
        return {
            "total_files": self.total_files,
            "success_count": self.success_count,
            "failure_count": self.failure_count,
            "skipped_count": self.skipped_count,
            "results": [r.to_dict() for r in self.results],
        }


@dataclass
class FileInfo:
    path: Path
    size: int
    extension: str
    language: str | None = None
    modified_at: str | None = None
    hash: str | None = None

    def to_dict(self) -> dict:
        return {
            "path": str(self.path),
            "size": self.size,
            "extension": self.extension,
            "language": self.language,
            "modified_at": self.modified_at,
            "hash": self.hash,
        }


@dataclass
class FunctionAnnotation:
    name: str
    file_path: Path
    start_line: int
    end_line: int
    signature: str
    parameters: list[str]
    return_type: str | None
    has_docstring: bool
    has_inline_comment: bool
    is_method: bool = False
    class_name: str | None = None

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "file_path": str(self.file_path),
            "start_line": self.start_line,
            "end_line": self.end_line,
            "signature": self.signature,
            "parameters": self.parameters,
            "return_type": self.return_type,
            "has_docstring": self.has_docstring,
            "has_inline_comment": self.has_inline_comment,
            "is_method": self.is_method,
            "class_name": self.class_name,
        }


@dataclass
class AnnotationCoverage:
    file_path: Path
    total_functions: int
    documented_functions: int
    undocumented_functions: int
    coverage_percent: float
    undocumented_functions_list: list[FunctionAnnotation] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "file_path": str(self.file_path),
            "total_functions": self.total_functions,
            "documented_functions": self.documented_functions,
            "undocumented_functions": [f.to_dict() for f in self.undocumented_functions_list],
            "coverage_percent": round(self.coverage_percent, 2),
        }


@dataclass
class JunkPattern:
    name: str
    pattern: str
    description: str = ""
    severity: str = "low"
    enabled: bool = True

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "pattern": self.pattern,
            "description": self.description,
            "severity": self.severity,
            "enabled": self.enabled,
        }


@dataclass
class JunkFile:
    file_path: Path
    pattern_name: str
    file_size: int
    relative_path: str

    def to_dict(self) -> dict:
        return {
            "file_path": str(self.file_path),
            "pattern_name": self.pattern_name,
            "file_size": self.file_size,
            "relative_path": self.relative_path,
        }


@dataclass
class CleanOperationResult:
    file_path: Path
    success: bool
    freed_bytes: int
    error: str | None = None

    def to_dict(self) -> dict:
        return {
            "file_path": str(self.file_path),
            "success": self.success,
            "freed_bytes": self.freed_bytes,
            "error": self.error,
        }


@dataclass
class CleanStats:
    files_scanned: int = 0
    files_cleaned: int = 0
    bytes_freed: int = 0
    errors: int = 0

    def to_dict(self) -> dict:
        return {
            "files_scanned": self.files_scanned,
            "files_cleaned": self.files_cleaned,
            "bytes_freed": self.bytes_freed,
            "errors": self.errors,
        }


@dataclass
class CopyrightInfo:
    author: str
    year: str
    license: str
    full_text: str

    def to_dict(self) -> dict:
        return {
            "author": self.author,
            "year": self.year,
            "license": self.license,
            "full_text": self.full_text,
        }


@dataclass
class ValidationResult:
    is_valid: bool
    issues: list[str]
    suggestions: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "is_valid": self.is_valid,
            "issues": self.issues,
            "suggestions": self.suggestions,
        }


@dataclass
class SnapshotInfo:
    snapshot_id: str
    created_at: str
    root_path: Path
    file_count: int
    description: str | None = None

    def to_dict(self) -> dict:
        return {
            "snapshot_id": self.snapshot_id,
            "created_at": self.created_at,
            "root_path": str(self.root_path),
            "file_count": self.file_count,
            "description": self.description,
        }


@dataclass
class ConfigInfo:
    key: str
    value: Any
    source: str
    description: str | None = None

    def to_dict(self) -> dict:
        return {
            "key": self.key,
            "value": self.value,
            "source": self.source,
            "description": self.description,
        }
