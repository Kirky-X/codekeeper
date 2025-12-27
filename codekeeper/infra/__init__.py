import logging
from pathlib import Path

from codekeeper.infra.config import CodeKeeperConfig, load_config, save_config

_INFRA_LOGGER = logging.getLogger(__name__)

from codekeeper.infra.logging import LogLevel, get_logger, setup_logging

__all__ = [
    "LogLevel",
    "get_logger",
    "get_project_config",
    "init_project",
    "is_project_initialized",
    "setup_logging",
]


def init_project(
        project_dir: Path | None = None,
        author: str = "",
        license_type: str = "MIT",
        log_level: str = "INFO",
        max_workers: int = 4,
        config_path: Path | None = None,
        force: bool = False,
) -> Path:
    """Initialize a CodeKeeper project in the specified directory.

    This function creates the `.codekeeper/` directory and generates a default
    configuration file if they don't exist or if `force` is True.

    Args:
        project_dir: Project root directory (default: current working directory)
        author: Default author name for copyright headers
        license_type: License type (MIT, Apache-2.0, GPL-3.0, BSD-3-Clause, Proprietary)
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        max_workers: Maximum number of worker processes
        config_path: Custom path for config file (relative to project_dir)
        force: Overwrite existing configuration if it exists

    Returns:
        Path to the created or updated configuration file

    Raises:
        FileExistsError: If config file exists and force is False
        PermissionError: If unable to create directories or files
    """
    project_dir = project_dir or Path.cwd()
    project_dir = project_dir.resolve()

    if config_path:
        config_path = project_dir / config_path
    else:
        config_path = project_dir / ".codekeeper" / "config.json"

    if config_path.exists() and not force:
        _INFRA_LOGGER.info(f"Configuration already exists at {config_path}")
        return config_path

    config = CodeKeeperConfig(
        author=author,
        license=license_type,
        log_level=log_level,
        max_workers=max_workers,
        snapshot_dir=Path(".codekeeper/snapshots"),
    )

    try:
        save_config(config, config_path)
        _INFRA_LOGGER.info(f"Project initialized successfully at {project_dir}")
        _INFRA_LOGGER.info(f"Configuration saved to {config_path}")
    except Exception as e:
        _INFRA_LOGGER.error(f"Failed to initialize project: {e}")
        raise

    return config_path


def get_project_config(project_dir: Path | None = None) -> CodeKeeperConfig | None:
    """Get the CodeKeeper configuration for a project.

    Args:
        project_dir: Project root directory (default: current working directory)

    Returns:
        Configuration object if found, None otherwise
    """
    project_dir = project_dir or Path.cwd()
    config_path = project_dir / ".codekeeper" / "config.json"

    if config_path.exists():
        return load_config(config_path)

    return None


def is_project_initialized(project_dir: Path | None = None) -> bool:
    """Check if a directory is initialized as a CodeKeeper project.

    Args:
        project_dir: Project root directory (default: current working directory)

    Returns:
        True if the project is initialized, False otherwise
    """
    project_dir = project_dir or Path.cwd()
    config_path = project_dir / ".codekeeper" / "config.json"
    return config_path.exists()
