import logging
import sys
from pathlib import Path

from codekeeper.infra.config import CodeKeeperConfig, load_config

LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s:%(lineno)d | %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logging(
        level: str | int = "INFO",
        log_file: Path | None = None,
        format: str = LOG_FORMAT,
        date_format: str = DATE_FORMAT,
        stream: bool = True,
        config: CodeKeeperConfig | None = None,
) -> logging.Logger:
    """Set up logging configuration for CodeKeeper.

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL) or int
        log_file: Optional path to log file
        format: Log message format string
        date_format: Date/time format string
        stream: Whether to log to stderr
        config: Optional CodeKeeperConfig object (will be loaded if not provided)

    Returns:
        Configured root logger for codekeeper
    """
    if config is not None:
        level = config.log_level
        log_file = config.snapshot_dir / "codekeeper.log" if log_file is None else log_file

    if isinstance(level, str):
        level = getattr(logging, level.upper(), logging.INFO)

    root_logger = logging.getLogger("codekeeper")
    root_logger.setLevel(level)

    root_logger.handlers.clear()

    formatter = logging.Formatter(fmt=format, datefmt=date_format)

    if stream:
        stream_handler = logging.StreamHandler(sys.stderr)
        stream_handler.setLevel(level)
        stream_handler.setFormatter(formatter)
        root_logger.addHandler(stream_handler)

    if log_file:
        log_file = Path(log_file)
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)

    return root_logger


def get_logger(name: str) -> logging.Logger:
    """Get a logger for a specific module.

    Args:
        name: Module name (usually __name__)

    Returns:
        Logger instance
    """
    return logging.getLogger(f"codekeeper.{name}")


def configure_from_config(config_path: Path | None = None) -> logging.Logger:
    """Configure logging from a CodeKeeper config file.

    Args:
        config_path: Path to config file (default: .codekeeper/config.json)

    Returns:
        Configured logger
    """
    if config_path is None:
        config_path = Path.cwd() / ".codekeeper" / "config.json"

    config = load_config(config_path) if config_path.exists() else None

    return setup_logging(config=config)


class LogLevel:
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    @classmethod
    def from_string(cls, level: str) -> int:
        return getattr(cls, level.upper(), logging.INFO)


def add_log_level(level_name: str, level_value: int) -> None:
    """Add a custom log level.

    Args:
        level_name: Name of the new level
        level_value: Numeric value for the level
    """
    if not hasattr(logging, level_name):
        logging.addLevelName(level_value, level_name)
        setattr(LogLevel, level_name.upper(), level_value)
