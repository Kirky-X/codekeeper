import gzip
import hashlib
import json
import logging
import shutil
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from codekeeper.utils.hash import compute_content_hash

logger = logging.getLogger(__name__)

DEFAULT_SNAPSHOT_DIR = Path(".codekeeper/snapshots")


@dataclass
class SnapshotMetadata:
    snapshot_id: str
    name: str
    description: str
    created_at: datetime
    file_count: int
    total_size: int
    checksum: str
    base_path: Path | None = None


@dataclass
class SnapshotFile:
    original_path: str
    snapshot_path: Path
    file_size: int
    checksum: str


@contextmanager
def atomic_write(path: Path, mode: str = "w") -> Iterator:
    """Context manager for atomic file writes.

    Args:
        path: Target file path
        mode: File open mode

    Yields:
        File handle
    """
    temp_path = path.with_suffix(path.suffix + ".tmp")
    try:
        if "b" in mode:
            with open(temp_path, mode) as f:
                yield f
        else:
            with open(temp_path, mode, encoding="utf-8") as f:
                yield f
        temp_path.replace(path)
    except Exception:
        if temp_path.exists():
            temp_path.unlink()
        raise


class SnapshotManager:
    """Manages file snapshots for rollback and recovery."""

    def __init__(
            self,
            snapshot_dir: Path = DEFAULT_SNAPSHOT_DIR,
            max_snapshots: int = 50,
    ):
        """Initialize the snapshot manager.

        Args:
            snapshot_dir: Directory to store snapshots
            max_snapshots: Maximum number of snapshots to keep
        """
        self.snapshot_dir = snapshot_dir
        self.max_snapshots = max_snapshots
        self._ensure_snapshot_dir()

    def _ensure_snapshot_dir(self) -> None:
        """Ensure the snapshot directory exists."""
        self.snapshot_dir.mkdir(parents=True, exist_ok=True)

    def _get_snapshot_path(self, snapshot_id: str) -> Path:
        """Get the path for a snapshot.

        Args:
            snapshot_id: Unique snapshot identifier

        Returns:
            Path to the snapshot directory
        """
        return self.snapshot_dir / snapshot_id

    def _generate_snapshot_id(self) -> str:
        """Generate a unique snapshot ID.

        Returns:
            Unique snapshot identifier
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        random_part = hashlib.md5(f"{timestamp}{id(self)}".encode()).hexdigest()[:8]
        return f"snap_{timestamp}_{random_part}"

    def _compress_content(self, content: bytes) -> bytes:
        """Compress content using gzip.

        Args:
            content: Raw content to compress

        Returns:
            Compressed content
        """
        return gzip.compress(content, compresslevel=6)

    def _decompress_content(self, compressed: bytes) -> bytes:
        """Decompress gzip content.

        Args:
            compressed: Compressed content

        Returns:
            Decompressed content
        """
        return gzip.decompress(compressed)

    def create_snapshot(
            self,
            files: list[Path],
            name: str,
            description: str = "",
            base_dir: Path | None = None,
    ) -> SnapshotMetadata:
        """Create a snapshot of the specified files.

        Args:
            files: List of files to include in the snapshot
            name: Human-readable snapshot name
            description: Snapshot description
            base_dir: Base directory for relative paths

        Returns:
            SnapshotMetadata with snapshot information
        """
        snapshot_id = self._generate_snapshot_id()
        snapshot_path = self._get_snapshot_path(snapshot_id)
        snapshot_path.mkdir(parents=True, exist_ok=True)

        manifest: dict = {
            "snapshot_id": snapshot_id,
            "name": name,
            "description": description,
            "created_at": datetime.now().isoformat(),
            "base_dir": str(base_dir) if base_dir else None,
            "files": [],
        }

        total_size = 0
        file_records = []

        for file_path in files:
            if not file_path.exists() or not file_path.is_file():
                logger.warning(f"Skipping non-existent or non-file: {file_path}")
                continue

            try:
                if base_dir:
                    try:
                        original_path = str(file_path.relative_to(base_dir))
                    except ValueError:
                        original_path = str(file_path)
                else:
                    try:
                        original_path = str(file_path.relative_to(Path.cwd()))
                    except ValueError:
                        original_path = str(file_path)

                content = file_path.read_bytes()
                compressed = self._compress_content(content)
                checksum = compute_content_hash(content)

                if base_dir:
                    try:
                        relative_path = file_path.relative_to(base_dir)
                    except ValueError:
                        relative_path = Path(file_path.name)
                else:
                    try:
                        relative_path = file_path.relative_to(Path.cwd())
                    except ValueError:
                        relative_path = Path(file_path.name)

                safe_name = "".join(
                    c for c in str(relative_path) if c.isalnum() or c in "._-"
                ).replace("/", "_")
                snapshot_file_path = snapshot_path / f"{safe_name}.gz"

                with atomic_write(snapshot_file_path, "wb") as f:
                    f.write(compressed)

                file_records.append(
                    {
                        "original_path": original_path,
                        "snapshot_path": f"{safe_name}.gz",
                        "file_size": len(content),
                        "compressed_size": len(compressed),
                        "checksum": checksum,
                    }
                )
                total_size += len(content)

            except OSError as e:
                logger.error(f"Failed to snapshot {file_path}: {e}")

        manifest["files"] = file_records
        manifest["checksum"] = compute_content_hash(
            json.dumps(file_records, sort_keys=True).encode("utf-8")
        )

        manifest_path = snapshot_path / "manifest.json"
        manifest_content = json.dumps(manifest, indent=2, ensure_ascii=False)
        manifest_checksum = compute_content_hash(manifest_content.encode("utf-8"))
        manifest["checksum"] = manifest_checksum

        with atomic_write(manifest_path, "w") as f:
            f.write(manifest_content)

        self._cleanup_old_snapshots()

        return SnapshotMetadata(
            snapshot_id=snapshot_id,
            name=name,
            description=description,
            created_at=datetime.now(),
            file_count=len(file_records),
            total_size=total_size,
            checksum=manifest_checksum,
            base_path=base_dir,
        )

    def get_snapshot(self, snapshot_id: str) -> SnapshotMetadata | None:
        """Get metadata for a specific snapshot.

        Args:
            snapshot_id: ID of the snapshot

        Returns:
            SnapshotMetadata if found, None otherwise
        """
        snapshot_path = self._get_snapshot_path(snapshot_id)
        manifest_path = snapshot_path / "manifest.json"

        if not manifest_path.exists():
            return None

        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

            return SnapshotMetadata(
                snapshot_id=manifest["snapshot_id"],
                name=manifest["name"],
                description=manifest.get("description", ""),
                created_at=datetime.fromisoformat(manifest["created_at"]),
                file_count=len(manifest["files"]),
                total_size=sum(f["file_size"] for f in manifest["files"]),
                checksum=manifest["checksum"],
                base_path=Path(manifest["base_dir"]) if manifest.get("base_dir") else None,
            )
        except (json.JSONDecodeError, KeyError, OSError) as e:
            logger.error(f"Failed to read snapshot {snapshot_id}: {e}")
            return None

    def list_snapshots(self) -> list[SnapshotMetadata]:
        """List all available snapshots.

        Returns:
            List of SnapshotMetadata sorted by creation time (newest first)
        """
        snapshots = []

        for entry in self.snapshot_dir.iterdir():
            if entry.is_dir():
                metadata = self.get_snapshot(entry.name)
                if metadata:
                    snapshots.append(metadata)

        return sorted(snapshots, key=lambda s: s.created_at, reverse=True)

    def rollback(
            self,
            snapshot_id: str,
            target_dir: Path | None = None,
            file_filter: list[str] | None = None,
    ) -> int:
        """Rollback files from a snapshot.

        Args:
            snapshot_id: ID of the snapshot to rollback
            target_dir: Target directory to restore files to
            file_filter: Optional list of file paths to restore (all if None)

        Returns:
            Number of files restored
        """
        snapshot_path = self._get_snapshot_path(snapshot_id)
        manifest_path = snapshot_path / "manifest.json"

        if not manifest_path.exists():
            raise ValueError(f"Snapshot {snapshot_id} not found")

        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

            if target_dir:
                base_dir = Path(target_dir)
            elif manifest.get("base_dir"):
                base_dir = Path(manifest["base_dir"])
            else:
                base_dir = None
            if base_dir:
                base_dir.mkdir(parents=True, exist_ok=True)

            restored_count = 0

            for file_record in manifest["files"]:
                original_path = file_record["original_path"]

                if file_filter:
                    normalized_filter = [str(Path(f).resolve()) for f in file_filter]
                    normalized_original = str(Path(original_path).resolve())
                    if (
                            normalized_original not in normalized_filter
                            and original_path not in file_filter
                    ):
                        continue

                try:
                    snapshot_file_path = snapshot_path / file_record["snapshot_path"]

                    if not snapshot_file_path.exists():
                        logger.warning(f"Missing file in snapshot: {file_record['snapshot_path']}")
                        continue

                    compressed = snapshot_file_path.read_bytes()
                    decompressed = self._decompress_content(compressed)

                    actual_checksum = compute_content_hash(decompressed)
                    if actual_checksum != file_record["checksum"]:
                        logger.error(
                            f"Checksum mismatch for {file_record['original_path']}: "
                            f"expected {file_record['checksum']}, got {actual_checksum}"
                        )
                        continue

                    if target_dir:
                        target_path = target_dir / Path(original_path).name
                    elif base_dir:
                        target_path = base_dir / original_path
                    else:
                        original_path_obj = Path(original_path)
                        if original_path_obj.is_absolute():
                            target_path = original_path_obj
                        else:
                            target_path = Path.cwd() / original_path
                    target_path.parent.mkdir(parents=True, exist_ok=True)

                    target_path.write_bytes(decompressed)
                    restored_count += 1

                except OSError as e:
                    logger.error(f"Failed to restore {file_record['original_path']}: {e}")

            return restored_count

        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid snapshot manifest: {e}")

    def delete_snapshot(self, snapshot_id: str) -> bool:
        """Delete a snapshot.

        Args:
            snapshot_id: ID of the snapshot to delete

        Returns:
            True if deleted, False if not found
        """
        snapshot_path = self._get_snapshot_path(snapshot_id)

        if not snapshot_path.exists():
            return False

        try:
            shutil.rmtree(snapshot_path)
            return True
        except OSError as e:
            logger.error(f"Failed to delete snapshot {snapshot_id}: {e}")
            return False

    def _cleanup_old_snapshots(self) -> int:
        """Remove old snapshots exceeding max_snapshots limit.

        Returns:
            Number of snapshots deleted
        """
        snapshots = self.list_snapshots()

        if len(snapshots) <= self.max_snapshots:
            return 0

        to_delete = len(snapshots) - self.max_snapshots
        deleted_count = 0

        for snapshot in snapshots[-to_delete:]:
            if self.delete_snapshot(snapshot.snapshot_id):
                deleted_count += 1

        return deleted_count

    def get_snapshot_contents(self, snapshot_id: str) -> list[SnapshotFile]:
        """Get list of files in a snapshot.

        Args:
            snapshot_id: ID of the snapshot

        Returns:
            List of SnapshotFile records
        """
        snapshot_path = self._get_snapshot_path(snapshot_id)
        manifest_path = snapshot_path / "manifest.json"

        if not manifest_path.exists():
            return []

        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

            return [
                SnapshotFile(
                    original_path=f["original_path"],
                    snapshot_path=snapshot_path / f["snapshot_path"],
                    file_size=f["file_size"],
                    checksum=f["checksum"],
                )
                for f in manifest["files"]
            ]
        except (json.JSONDecodeError, KeyError, OSError):
            return []

    def export_snapshot(self, snapshot_id: str, target_zip: Path) -> None:
        """Export a snapshot as a ZIP file.

        Args:
            snapshot_id: ID of the snapshot
            target_zip: Target path for the ZIP file
        """
        snapshot_path = self._get_snapshot_path(snapshot_id)

        if not snapshot_path.exists():
            raise ValueError(f"Snapshot {snapshot_id} not found")

        shutil.make_archive(
            str(target_zip.with_suffix("")),
            format="zip",
            root_dir=self.snapshot_dir,
            base_dir=snapshot_id,
        )

    def import_snapshot(self, source_zip: Path) -> SnapshotMetadata:
        """Import a snapshot from a ZIP file.

        Args:
            source_zip: Path to the ZIP file

        Returns:
            SnapshotMetadata of the imported snapshot
        """
        if not source_zip.exists():
            raise ValueError(f"ZIP file not found: {source_zip}")

        import zipfile

        with zipfile.ZipFile(source_zip, "r") as zf:
            snapshot_id = zf.namelist()[0].rstrip("/")
            target_path = self._get_snapshot_path(snapshot_id)

            if target_path.exists():
                shutil.rmtree(target_path)

            zf.extractall(self.snapshot_dir)

        metadata = self.get_snapshot(snapshot_id)
        if metadata is None:
            raise ValueError(f"Invalid snapshot in ZIP file: {snapshot_id}")

        return metadata
