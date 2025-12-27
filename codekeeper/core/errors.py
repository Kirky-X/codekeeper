from enum import IntEnum
from pathlib import Path
from typing import Any


class ErrorCode(IntEnum):
    SUCCESS = 0

    FILE_NOT_FOUND = 1001
    FILE_TOO_LARGE = 1002
    FILE_NOT_READABLE = 1003
    FILE_NOT_WRITABLE = 1004
    INVALID_FILE_TYPE = 1005
    INVALID_FILE_PATH = 1006

    PERMISSION_DENIED = 2001
    ACCESS_DENIED = 2002

    CACHE_READ_ERROR = 3001
    CACHE_WRITE_ERROR = 3002
    CACHE_CORRUPTED = 3003

    SNAPSHOT_CREATE_ERROR = 4001
    SNAPSHOT_NOT_FOUND = 4002
    SNAPSHOT_CORRUPTED = 4003
    ROLLBACK_FAILED = 4004

    PARSE_ERROR = 5001
    UNSUPPORTED_LANGUAGE = 5002
    INVALID_SYNTAX = 5003

    INVALID_CONFIG = 6001
    MISSING_CONFIG = 6002

    PROCESS_POOL_ERROR = 7001
    CONCURRENT_WRITE_ERROR = 7002

    SECURITY_ERROR = 8001
    PATH_TRAVERSAL = 8002
    INVALID_PATH = 8003


ERROR_MESSAGES = {
    ErrorCode.SUCCESS: "操作成功",
    ErrorCode.FILE_NOT_FOUND: "文件不存在",
    ErrorCode.FILE_TOO_LARGE: "文件过大",
    ErrorCode.FILE_NOT_READABLE: "文件不可读",
    ErrorCode.FILE_NOT_WRITABLE: "文件不可写",
    ErrorCode.INVALID_FILE_TYPE: "不支持的文件类型",
    ErrorCode.INVALID_FILE_PATH: "无效的文件路径",
    ErrorCode.PERMISSION_DENIED: "权限被拒绝",
    ErrorCode.ACCESS_DENIED: "访问被拒绝",
    ErrorCode.CACHE_READ_ERROR: "缓存读取错误",
    ErrorCode.CACHE_WRITE_ERROR: "缓存写入错误",
    ErrorCode.CACHE_CORRUPTED: "缓存损坏",
    ErrorCode.SNAPSHOT_CREATE_ERROR: "创建快照失败",
    ErrorCode.SNAPSHOT_NOT_FOUND: "快照不存在",
    ErrorCode.SNAPSHOT_CORRUPTED: "快照损坏",
    ErrorCode.ROLLBACK_FAILED: "回滚失败",
    ErrorCode.PARSE_ERROR: "解析错误",
    ErrorCode.UNSUPPORTED_LANGUAGE: "不支持的语言",
    ErrorCode.INVALID_SYNTAX: "语法错误",
    ErrorCode.INVALID_CONFIG: "配置无效",
    ErrorCode.MISSING_CONFIG: "配置缺失",
    ErrorCode.PROCESS_POOL_ERROR: "进程池错误",
    ErrorCode.CONCURRENT_WRITE_ERROR: "并发写入错误",
    ErrorCode.SECURITY_ERROR: "安全错误",
    ErrorCode.PATH_TRAVERSAL: "检测到路径遍历攻击",
    ErrorCode.INVALID_PATH: "路径验证失败",
}


class CodeKeeperError(Exception):
    def __init__(
            self,
            message: str | None = None,
            error_code: ErrorCode = ErrorCode.SUCCESS,
            details: dict[str, Any] | None = None,
    ):
        self.error_code = error_code
        self.message = message or ERROR_MESSAGES.get(error_code, "未知错误")
        self.details = details or {}
        super().__init__(self.message)

    def __str__(self) -> str:
        base = f"[{self.error_code.name}] {self.message}"
        if self.details:
            details_str = ", ".join(f"{k}={v}" for k, v in self.details.items())
            return f"{base} ({details_str})"
        return base

    def to_dict(self) -> dict[str, Any]:
        return {
            "error_code": int(self.error_code),
            "error_name": self.error_code.name,
            "message": self.message,
            "details": self.details,
        }


class FileError(CodeKeeperError):
    def __init__(
            self,
            message: str | None = None,
            error_code: ErrorCode = ErrorCode.INVALID_FILE_PATH,
            file_path: Path | None = None,
            **kwargs,
    ):
        details = kwargs.pop("details", {})
        if file_path:
            details["file_path"] = str(file_path)
        super().__init__(message=message, error_code=error_code, details=details)


class FileNotFoundError(FileError):
    def __init__(self, file_path: Path):
        super().__init__(
            message=f"文件不存在: {file_path}",
            error_code=ErrorCode.FILE_NOT_FOUND,
            file_path=file_path,
        )


class FileNotReadableError(FileError):
    def __init__(self, file_path: Path):
        super().__init__(
            message=f"文件不可读: {file_path}",
            error_code=ErrorCode.FILE_NOT_READABLE,
            file_path=file_path,
        )


class FileNotWritableError(FileError):
    def __init__(self, file_path: Path):
        super().__init__(
            message=f"文件不可写: {file_path}",
            error_code=ErrorCode.FILE_NOT_WRITABLE,
            file_path=file_path,
        )


class PermissionError(CodeKeeperError):
    def __init__(
            self,
            message: str | None = None,
            path: Path | None = None,
            operation: str = "access",
    ):
        details = {"operation": operation}
        if path:
            details["path"] = str(path)
        super().__init__(
            message=message or f"权限被拒绝: {operation} 操作失败",
            error_code=ErrorCode.PERMISSION_DENIED,
            details=details,
        )


class CacheError(CodeKeeperError):
    def __init__(
            self,
            message: str | None = None,
            error_code: ErrorCode = ErrorCode.CACHE_READ_ERROR,
            cache_key: str | None = None,
    ):
        details = {}
        if cache_key:
            details["cache_key"] = cache_key
        super().__init__(message=message, error_code=error_code, details=details)


class SnapshotError(CodeKeeperError):
    def __init__(
            self,
            message: str | None = None,
            error_code: ErrorCode = ErrorCode.SNAPSHOT_CREATE_ERROR,
            snapshot_id: str | None = None,
    ):
        details = {}
        if snapshot_id:
            details["snapshot_id"] = snapshot_id
        super().__init__(message=message, error_code=error_code, details=details)


class ParseError(CodeKeeperError):
    def __init__(
            self,
            message: str | None = None,
            file_path: Path | None = None,
            line_number: int | None = None,
            language: str | None = None,
    ):
        details = {}
        if file_path:
            details["file_path"] = str(file_path)
        if line_number:
            details["line_number"] = line_number
        if language:
            details["language"] = language
        super().__init__(
            message=message or "解析错误",
            error_code=ErrorCode.PARSE_ERROR,
            details=details,
        )


class ConfigError(CodeKeeperError):
    def __init__(
            self,
            message: str | None = None,
            config_key: str | None = None,
    ):
        details = {}
        if config_key:
            details["config_key"] = config_key
        super().__init__(
            message=message or "配置错误",
            error_code=ErrorCode.INVALID_CONFIG,
            details=details,
        )


class SecurityError(CodeKeeperError):
    def __init__(
            self,
            message: str | None = None,
            path: Path | None = None,
            error_code: ErrorCode = ErrorCode.SECURITY_ERROR,
    ):
        details = {}
        if path:
            details["path"] = str(path)
        super().__init__(
            message=message or "安全错误",
            error_code=error_code,
            details=details,
        )


class PathTraversalError(SecurityError):
    def __init__(self, path: Path, attempted_path: str):
        super().__init__(
            message=f"检测到路径遍历攻击: {attempted_path}",
            error_code=ErrorCode.PATH_TRAVERSAL,
            path=path,
        )


class InvalidPathError(SecurityError):
    def __init__(self, path: Path, reason: str | None = None):
        super().__init__(
            message=f"路径验证失败: {path}" + (f" - {reason}" if reason else ""),
            error_code=ErrorCode.INVALID_PATH,
            path=path,
        )
