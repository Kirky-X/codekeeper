from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class ConfigFileError(Exception):
    """Exception raised for configuration file errors."""

    pass


class ConfigurationError(Exception):
    """Exception raised for configuration validation errors."""

    pass


VALID_LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}


class CodeKeeperConfig(BaseModel):
    """Configuration for CodeKeeper."""

    model_config = ConfigDict(extra="ignore", populate_by_name=True, frozen=True)

    author: str = ""
    license: str = "MIT"
    max_workers: int = 4
    cache_dir: Path = Path.home() / ".cache" / "codekeeper"
    snapshot_dir: Path = Path(".codekeeper/snapshots")
    log_level: str = "INFO"
    ignore_patterns: list[str] = Field(
        default_factory=lambda: [
            "__pycache__",
            "node_modules",
            ".git",
            "dist",
            "build",
            "*.pyc",
            "*.pyo",
        ]
    )

    @field_validator("max_workers")
    @classmethod
    def validate_max_workers(cls, v: int) -> int:
        if v < 1:
            raise ConfigurationError(f"max_workers must be at least 1, got {v}")
        if v > 128:
            raise ConfigurationError(f"max_workers cannot exceed 128, got {v}")
        return v

    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, v: str) -> str:
        if v.upper() not in VALID_LOG_LEVELS:
            raise ConfigurationError(
                f"Invalid log_level '{v}'. Must be one of: {', '.join(VALID_LOG_LEVELS)}"
            )
        return v.upper()

    @field_validator("cache_dir", "snapshot_dir")
    @classmethod
    def validate_paths(cls, v: str | Path) -> Path:
        if isinstance(v, str):
            return Path(v)
        return v

    @field_validator("license")
    @classmethod
    def validate_license(cls, v: str) -> str:
        valid_licenses = {"MIT", "Apache-2.0", "GPL-3.0", "BSD-3-Clause", "Proprietary"}
        if v not in valid_licenses:
            raise ConfigurationError(
                f"Invalid license '{v}'. Common values: {', '.join(valid_licenses)}"
            )
        return v

    def model_dump(self, *args, **kwargs) -> dict:
        """Override to convert Path objects to strings for JSON serialization."""
        data = super().model_dump(*args, **kwargs)
        if "cache_dir" in data and isinstance(data["cache_dir"], Path):
            data["cache_dir"] = str(data["cache_dir"])
        if "snapshot_dir" in data and isinstance(data["snapshot_dir"], Path):
            data["snapshot_dir"] = str(data["snapshot_dir"])
        return data


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_prefix="CODEKEEPER_",
        env_nested_delimiter="_",
        env_file=None,
    )

    codekeeper_author: str = ""
    codekeeper_license: str = "MIT"
    codekeeper_max_workers: int = 4
    codekeeper_cache_dir: Path = Path.home() / ".cache" / "codekeeper"
    codekeeper_snapshot_dir: Path = Path(".codekeeper/snapshots")
    codekeeper_log_level: str = "INFO"
    codekeeper_ignore_patterns: str = ""

    @property
    def config(self) -> CodeKeeperConfig:
        """Convert settings to configuration model."""
        patterns = [p.strip() for p in self.codekeeper_ignore_patterns.split(",") if p.strip()]

        return CodeKeeperConfig(
            author=self.codekeeper_author or "",
            license=self.codekeeper_license,
            max_workers=self.codekeeper_max_workers,
            cache_dir=self.codekeeper_cache_dir,
            snapshot_dir=self.codekeeper_snapshot_dir,
            log_level=self.codekeeper_log_level,
            ignore_patterns=patterns or CodeKeeperConfig().ignore_patterns,
        )


def load_config(config_path: Path | None = None) -> CodeKeeperConfig:
    """Load configuration from file and environment.

    Configuration priority (highest to lowest):
    1. Environment variables
    2. Config file (if provided)
    3. Default values

    Args:
        config_path: Optional path to config file (JSON format)

    Returns:
        Configuration object

    Raises:
        ConfigFileError: If config file cannot be read or parsed
        ConfigurationError: If configuration values are invalid
    """
    settings = Settings()

    if config_path is not None:
        config_path = Path(config_path)
        if config_path.exists():
            if config_path.suffix.lower() == ".json":
                try:
                    with open(config_path, encoding="utf-8") as f:
                        file_config = f.read()
                    config_data = settings.config.model_dump()
                    file_values = CodeKeeperConfig.model_validate_json(file_config)
                    for field, value in file_values.model_dump().items():
                        if value is not None and value != getattr(settings.config, field):
                            config_data[field] = value
                    return CodeKeeperConfig(**config_data)
                except (OSError, ValueError) as e:
                    raise ConfigFileError(f"Failed to read or parse config file {config_path}: {e}")
                except ValidationError as e:
                    raise ConfigurationError(f"Invalid configuration in file {config_path}: {e}")
            else:
                raise ConfigFileError(
                    f"Unsupported config file format: {config_path.suffix}. "
                    "Only .json files are supported."
                )

    return settings.config


def save_config(config: CodeKeeperConfig, config_path: Path) -> None:
    """Save configuration to a JSON file.

    Args:
        config: Configuration to save
        config_path: Path to save the config file

    Raises:
        ConfigFileError: If the file cannot be written
    """
    config_path = Path(config_path)
    try:
        config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(config_path, "w", encoding="utf-8") as f:
            f.write(config.model_dump_json(indent=2))
    except OSError as e:
        raise ConfigFileError(f"Failed to save config file {config_path}: {e}")
