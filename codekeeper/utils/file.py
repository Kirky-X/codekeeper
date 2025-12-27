import re
from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".py": "python",
    ".rs": "rust",
    ".java": "java",
    ".go": "go",
}

IGNORE_PATTERNS = {
    "__pycache__",
    "*.pyc",
    "*.pyo",
    "node_modules",
    ".git",
    ".svn",
    ".hg",
    "*.egg-info",
    "dist",
    "build",
    ".venv",
    "venv",
    ".pytest_cache",
    ".mypy_cache",
}


def is_supported_file(file_path: Path) -> bool:
    """Check if file extension is supported.

    Args:
        file_path: Path to check

    Returns:
        True if file extension is supported
    """
    return file_path.suffix in SUPPORTED_EXTENSIONS


def should_ignore(path: Path) -> bool:
    """Check if path should be ignored.

    Args:
        path: Path to check

    Returns:
        True if path should be ignored
    """
    path_str = str(path)

    for pattern in IGNORE_PATTERNS:
        if pattern.startswith("*"):
            regex_pattern = pattern.replace("*", ".*")
            if re.search(regex_pattern, path_str):
                return True
        elif path.name == pattern or path_str == pattern:
            return True

    return False


def get_language(file_path: Path) -> str | None:
    """Get language identifier for a file.

    Args:
        file_path: Path to the file

    Returns:
        Language identifier or None if not supported
    """
    return SUPPORTED_EXTENSIONS.get(file_path.suffix)


def scan_files(path: Path, recursive: bool = True, supported_only: bool = True) -> list[Path]:
    """Scan directory for files.

    Args:
        path: Directory to scan
        recursive: Whether to scan recursively
        supported_only: Whether to only include supported files

    Returns:
        List of file paths
    """
    files: list[Path] = []

    if path.is_file():
        if not supported_only or is_supported_file(path):
            files.append(path)
        return files

    iterator = path.rglob("*") if recursive else path.glob("*")

    for item in iterator:
        if (
                item.is_file()
                and not should_ignore(item)
                and (not supported_only or is_supported_file(item))
        ):
            files.append(item)

    return sorted(files)


def normalize_path(path: Path, base_dir: Path) -> Path:
    """Normalize path relative to base directory.

    Args:
        path: Path to normalize
        base_dir: Base directory

    Returns:
        Normalized relative path
    """
    try:
        resolved_path = path.resolve()
        resolved_base = base_dir.resolve()

        if resolved_path.is_relative_to(resolved_base):
            return resolved_path.relative_to(resolved_base)

        return path

    except (ValueError, OSError):
        return path
