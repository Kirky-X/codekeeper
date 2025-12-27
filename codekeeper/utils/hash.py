import hashlib
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB


def compute_file_hash(file_path: str | Path, chunk_size: int = 4096) -> str:
    """Compute SHA-256 hash of a file.

    Args:
        file_path: Path to the file
        chunk_size: Size of chunks to read (default 4KB)

    Returns:
        Hexadecimal string of the hash

    Raises:
        FileNotFoundError: If file does not exist
        PermissionError: If file cannot be read
        ValueError: If file size exceeds MAX_FILE_SIZE
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    file_size = path.stat().st_size

    if file_size > MAX_FILE_SIZE:
        raise ValueError(f"File size {file_size} exceeds maximum allowed size {MAX_FILE_SIZE}")

    sha256_hash = hashlib.sha256()

    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                sha256_hash.update(chunk)
    except PermissionError as e:
        raise PermissionError(f"Cannot read file {file_path}: {e}") from e

    return sha256_hash.hexdigest()


def compute_content_hash(content: bytes) -> str:
    """Compute SHA-256 hash of bytes content.

    Args:
        content: Binary content to hash

    Returns:
        Hexadecimal string of the hash
    """
    return hashlib.sha256(content).hexdigest()
