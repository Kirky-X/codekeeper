import hashlib
import logging
import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path

logger = logging.getLogger(__name__)

DEFAULT_CACHE_DIR = Path.home() / ".cache" / "codekeeper"


@dataclass
class CacheEntry:
    file_path: str
    file_hash: str
    file_size: int
    mtime: float
    cached_at: datetime


@dataclass
class CacheStats:
    total_entries: int
    valid_entries: int
    stale_entries: int
    hit_count: int
    miss_count: int

    @property
    def hit_rate(self) -> float:
        total = self.hit_count + self.miss_count
        if total == 0:
            return 0.0
        return self.hit_count / total


class HashCache:
    """SQLite-based file hash cache with WAL mode for performance."""

    def __init__(self, cache_dir: Path = DEFAULT_CACHE_DIR, db_name: str = "file_hashes.db"):
        """Initialize the hash cache.

        Args:
            cache_dir: Directory to store the cache database
            db_name: Name of the SQLite database file
        """
        self.cache_dir = cache_dir
        self.db_path = self.cache_dir / db_name
        self._hit_count = 0
        self._miss_count = 0
        self._ensure_cache_dir()
        self._init_db()

    def _ensure_cache_dir(self) -> None:
        """Ensure the cache directory exists."""
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _init_db(self) -> None:
        """Initialize the SQLite database with WAL mode."""
        with self._get_connection() as conn:
            conn.execute("PRAGMA journal_mode=WAL")
            conn.execute("PRAGMA synchronous=NORMAL")
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS file_hashes
                (
                    file_path
                    TEXT
                    PRIMARY
                    KEY,
                    file_hash
                    TEXT
                    NOT
                    NULL,
                    file_size
                    INTEGER
                    NOT
                    NULL,
                    mtime
                    REAL
                    NOT
                    NULL,
                    cached_at
                    TEXT
                    NOT
                    NULL
                )
                """
            )
            conn.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_file_hash
                    ON file_hashes(file_hash)
                """
            )
            conn.commit()

    @contextmanager
    def _get_connection(self) -> Iterator[sqlite3.Connection]:
        """Get a database connection with context manager."""
        conn = sqlite3.connect(str(self.db_path), timeout=30.0)
        try:
            yield conn
        finally:
            conn.close()

    def get(self, file_path: str) -> CacheEntry | None:
        """Retrieve a cached hash entry.

        Args:
            file_path: Path to the file

        Returns:
            CacheEntry if found and valid, None otherwise
        """
        with self._get_connection() as conn:
            cursor = conn.execute(
                """
                SELECT file_path, file_hash, file_size, mtime, cached_at
                FROM file_hashes
                WHERE file_path = ?
                """,
                (file_path,),
            )
            row = cursor.fetchone()

            if row is None:
                self._miss_count += 1
                return None

            self._hit_count += 1
            return CacheEntry(
                file_path=row[0],
                file_hash=row[1],
                file_size=row[2],
                mtime=row[3],
                cached_at=datetime.fromisoformat(row[4]),
            )

    def get_hash(self, file_path: str, current_mtime: float, current_size: int) -> str | None:
        """Get cached hash if file hasn't changed.

        Args:
            file_path: Path to the file
            current_mtime: Current modification time of the file
            current_size: Current size of the file

        Returns:
            Cached hash if valid, None otherwise
        """
        entry = self.get(file_path)
        if entry is None:
            return None

        if entry.mtime != current_mtime or entry.file_size != current_size:
            logger.debug(f"Cache invalid for {file_path}: mtime or size changed")
            return None

        return entry.file_hash

    def is_changed(self, file_path: str, current_mtime: float, current_size: int) -> bool:
        """Check if file has changed since last cache.

        Args:
            file_path: Path to the file
            current_mtime: Current modification time of the file
            current_size: Current size of the file

        Returns:
            True if file has changed, False otherwise
        """
        entry = self.get(file_path)
        if entry is None:
            return True
        return entry.mtime != current_mtime or entry.file_size != current_size

    def get_or_compute_hash(
            self, file_path: str, compute_func: callable = None
    ) -> tuple[str, bool]:
        """Get cached hash or compute new one if changed.

        Args:
            file_path: Path to the file
            compute_func: Optional function to compute hash (default: compute_file_hash)

        Returns:
            Tuple of (file_hash, was_cached)
        """
        if compute_func is None:
            compute_func = compute_file_hash

        path = Path(file_path)
        if not path.exists():
            logger.warning(f"File not found: {file_path}")
            return ("", False)

        current_mtime = path.stat().st_mtime
        current_size = path.stat().st_size

        cached_hash = self.get_hash(file_path, current_mtime, current_size)
        if cached_hash is not None:
            logger.debug(f"Cache hit for {file_path}")
            return (cached_hash, True)

        logger.debug(f"Cache miss for {file_path}, computing hash")
        file_hash = compute_func(file_path)
        self.set(file_path, file_hash, current_mtime, current_size)
        return (file_hash, False)

    def batch_check(
            self, file_paths: list[str], compute_func: callable = None
    ) -> dict[str, tuple[str, bool]]:
        """Check multiple files and return changed ones with their hashes.

        Args:
            file_paths: List of file paths to check
            compute_func: Optional function to compute hash

        Returns:
            Dict mapping file_path to (file_hash, was_cached)
        """
        if compute_func is None:
            compute_func = compute_file_hash

        results = {}
        changed_files = []

        for file_path in file_paths:
            path = Path(file_path)
            if not path.exists():
                logger.warning(f"File not found: {file_path}")
                results[file_path] = ("", False)
                continue

            current_mtime = path.stat().st_mtime
            current_size = path.stat().st_size

            if not self.is_changed(file_path, current_mtime, current_size):
                entry = self.get(file_path)
                if entry:
                    results[file_path] = (entry.file_hash, True)
                else:
                    changed_files.append(file_path)
            else:
                changed_files.append(file_path)

        for file_path in changed_files:
            file_hash = compute_func(file_path)
            path = Path(file_path)
            if path.exists():
                current_mtime = path.stat().st_mtime
                current_size = path.stat().st_size
                self.set(file_path, file_hash, current_mtime, current_size)
                results[file_path] = (file_hash, False)

        return results

    def get_stale_entries(self) -> list[CacheEntry]:
        """Get entries where the file no longer exists or has changed.

        Returns:
            List of stale CacheEntry objects
        """
        entries = []
        with self._get_connection() as conn:
            cursor = conn.execute(
                "SELECT file_path, file_hash, file_size, mtime, cached_at FROM file_hashes"
            )
            for row in cursor.fetchall():
                file_path = row[0]
                path = Path(file_path)
                if not path.exists():
                    entries.append(
                        CacheEntry(
                            file_path=row[0],
                            file_hash=row[1],
                            file_size=row[2],
                            mtime=row[3],
                            cached_at=datetime.fromisoformat(row[4]),
                        )
                    )
                else:
                    current_mtime = path.stat().st_mtime
                    current_size = path.stat().st_size
                    if current_mtime != row[3] or current_size != row[2]:
                        entries.append(
                            CacheEntry(
                                file_path=row[0],
                                file_hash=row[1],
                                file_size=row[2],
                                mtime=row[3],
                                cached_at=datetime.fromisoformat(row[4]),
                            )
                        )
        return entries

    def cleanup_stale(self) -> int:
        """Remove entries for files that no longer exist or have changed.

        Returns:
            Number of entries deleted
        """
        stale = self.get_stale_entries()
        count = 0
        for entry in stale:
            if self.delete(entry.file_path):
                count += 1
        return count

    def get_stats(self) -> CacheStats:
        """Get cache statistics.

        Returns:
            CacheStats object with current statistics
        """
        with self._get_connection() as conn:
            cursor = conn.execute("SELECT COUNT(*) FROM file_hashes")
            total_entries = cursor.fetchone()[0]

        stale_entries = len(self.get_stale_entries())
        valid_entries = total_entries - stale_entries

        return CacheStats(
            total_entries=total_entries,
            valid_entries=valid_entries,
            stale_entries=stale_entries,
            hit_count=self._hit_count,
            miss_count=self._miss_count,
        )

    def set(
            self,
            file_path: str,
            file_hash: str,
            file_size: int,
            mtime: float,
    ) -> None:
        """Store a file hash in the cache.

        Args:
            file_path: Path to the file
            file_hash: SHA-256 hash of the file content
            file_size: Size of the file in bytes
            mtime: Modification time of the file
        """
        with self._get_connection() as conn:
            cached_at = datetime.now().isoformat()
            conn.execute(
                """
                INSERT OR REPLACE INTO file_hashes
                (file_path, file_hash, file_size, mtime, cached_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                (file_path, file_hash, file_size, mtime, cached_at),
            )
            conn.commit()

    def delete(self, file_path: str) -> bool:
        """Delete a cached entry.

        Args:
            file_path: Path to the file

        Returns:
            True if entry was deleted, False if not found
        """
        with self._get_connection() as conn:
            cursor = conn.execute(
                "DELETE FROM file_hashes WHERE file_path = ?",
                (file_path,),
            )
            conn.commit()
            return cursor.rowcount > 0

    def clear(self) -> int:
        """Clear all cached entries.

        Returns:
            Number of entries deleted
        """
        with self._get_connection() as conn:
            cursor = conn.execute("DELETE FROM file_hashes")
            conn.commit()
            return cursor.rowcount

    def cleanup(self, max_age_days: int = 30) -> int:
        """Remove entries older than max_age_days.

        Args:
            max_age_days: Maximum age in days

        Returns:
            Number of entries deleted
        """
        cutoff_date = datetime.now() - timedelta(days=max_age_days)
        cutoff_str = cutoff_date.isoformat()

        with self._get_connection() as conn:
            cursor = conn.execute(
                "DELETE FROM file_hashes WHERE cached_at < ?",
                (cutoff_str,),
            )
            conn.commit()
            return cursor.rowcount

    def verify_integrity(self) -> bool:
        """Verify database integrity.

        Returns:
            True if integrity check passes, False otherwise
        """
        try:
            with self._get_connection() as conn:
                cursor = conn.execute("PRAGMA integrity_check")
                result = cursor.fetchone()
                return result[0] == "ok"
        except sqlite3.Error as e:
            logger.error(f"Database integrity check failed: {e}")
            return False

    def close(self) -> None:
        """Close the database connection and vacuum."""
        with self._get_connection() as conn:
            conn.execute("VACUUM")
            conn.commit()


def compute_file_hash(file_path: str, algorithm: str = "sha256", block_size: int = 65536) -> str:
    """Compute hash of a file.

    Args:
        file_path: Path to the file
        algorithm: Hash algorithm (sha256, sha1, md5)
        block_size: Block size for reading file

    Returns:
        Hexadecimal hash string
    """
    hasher = hashlib.new(algorithm)
    path = Path(file_path)

    if not path.exists() or not path.is_file():
        return ""

    try:
        with open(file_path, "rb") as f:
            for block in iter(lambda: f.read(block_size), b""):
                hasher.update(block)
        return hasher.hexdigest()
    except OSError as e:
        logger.error(f"Error computing hash for {file_path}: {e}")
        return ""
