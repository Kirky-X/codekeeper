import json
import os
import tempfile
from pathlib import Path

import pytest

from codekeeper.infra.config import (
    VALID_LOG_LEVELS,
    CodeKeeperConfig,
    ConfigFileError,
    ConfigurationError,
    Settings,
    load_config,
    save_config,
)


class TestCodeKeeperConfig:
    def test_default_values(self):
        config = CodeKeeperConfig()

        assert config.author == ""
        assert config.license == "MIT"
        assert config.max_workers == 4
        assert config.cache_dir == Path.home() / ".cache" / "codekeeper"
        assert config.snapshot_dir == Path(".codekeeper/snapshots")
        assert config.log_level == "INFO"
        assert "__pycache__" in config.ignore_patterns
        assert "node_modules" in config.ignore_patterns

    def test_custom_values(self):
        config = CodeKeeperConfig(
            author="Test Author",
            license="Apache-2.0",
            max_workers=8,
            cache_dir=Path("/tmp/test_cache"),
            snapshot_dir=Path("/tmp/snapshots"),
            log_level="DEBUG",
            ignore_patterns=["*.log", ".env"],
        )

        assert config.author == "Test Author"
        assert config.license == "Apache-2.0"
        assert config.max_workers == 8
        assert config.cache_dir == Path("/tmp/test_cache")
        assert config.log_level == "DEBUG"
        assert "*.log" in config.ignore_patterns
        assert ".env" in config.ignore_patterns

    def test_extra_fields_ignored(self):
        config = CodeKeeperConfig(
            author="Test",
            unknown_field="should be ignored",
        )

        assert config.author == "Test"

    def test_ignore_patterns_default_factory(self):
        config1 = CodeKeeperConfig()
        config2 = CodeKeeperConfig()

        assert config1.ignore_patterns == config2.ignore_patterns
        assert len(config1.ignore_patterns) > 0

    def test_model_config_extra_ignore(self):
        config = CodeKeeperConfig(
            author="Test",
            extra_field="value",
        )

        assert not hasattr(config, "extra_field")

    def test_cache_dir_path_type(self):
        config = CodeKeeperConfig()

        assert isinstance(config.cache_dir, Path)
        assert isinstance(config.snapshot_dir, Path)

    def test_ignore_patterns_list_contents(self):
        config = CodeKeeperConfig()

        expected_patterns = [
            "__pycache__",
            "node_modules",
            ".git",
            "dist",
            "build",
            "*.pyc",
            "*.pyo",
        ]

        for pattern in expected_patterns:
            assert pattern in config.ignore_patterns


class TestSettings:
    def test_default_values(self):
        settings = Settings()

        assert settings.codekeeper_author == ""
        assert settings.codekeeper_license == "MIT"
        assert settings.codekeeper_max_workers == 4
        assert settings.codekeeper_log_level == "INFO"

    def test_config_property_returns_config(self):
        settings = Settings()

        config = settings.config

        assert isinstance(config, CodeKeeperConfig)
        assert config.author == ""
        assert config.license == "MIT"
        assert config.max_workers == 4

    def test_env_prefix_is_codekeeper(self):
        settings = Settings()

        assert hasattr(settings, "codekeeper_author")
        assert hasattr(settings, "codekeeper_license")
        assert hasattr(settings, "codekeeper_max_workers")
        assert hasattr(settings, "codekeeper_cache_dir")
        assert hasattr(settings, "codekeeper_snapshot_dir")

    def test_ignore_patterns_attribute_exists(self):
        settings = Settings()

        assert hasattr(settings, "codekeeper_ignore_patterns")


class TestLoadConfig:
    def test_load_config_returns_config(self):
        config = load_config()

        assert isinstance(config, CodeKeeperConfig)
        assert hasattr(config, "author")
        assert hasattr(config, "max_workers")
        assert hasattr(config, "ignore_patterns")

    def test_load_config_returns_correct_type(self):
        config = load_config()

        assert isinstance(config, CodeKeeperConfig)
        assert isinstance(config.cache_dir, Path)
        assert isinstance(config.snapshot_dir, Path)
        assert isinstance(config.ignore_patterns, list)

    def test_load_config_has_required_attributes(self):
        config = load_config()

        assert hasattr(config, "author")
        assert hasattr(config, "license")
        assert hasattr(config, "max_workers")
        assert hasattr(config, "cache_dir")
        assert hasattr(config, "snapshot_dir")
        assert hasattr(config, "log_level")
        assert hasattr(config, "ignore_patterns")


class TestConfigEdgeCases:
    def test_empty_author_string(self):
        config = CodeKeeperConfig()

        assert config.author == ""
        assert not config.author

    def test_license_default_is_mit(self):
        config = CodeKeeperConfig()

        assert config.license == "MIT"

    def test_multiple_ignore_patterns(self):
        config = CodeKeeperConfig(
            ignore_patterns=["*.pyc", "*.pyo", "__pycache__", ".git", "node_modules"]
        )

        assert len(config.ignore_patterns) == 5
        assert "*.pyc" in config.ignore_patterns
        assert ".git" in config.ignore_patterns

    def test_empty_ignore_patterns_list(self):
        config = CodeKeeperConfig(ignore_patterns=[])

        assert config.ignore_patterns == []

    def test_custom_license(self):
        config = CodeKeeperConfig(license="Apache-2.0")

        assert config.license == "Apache-2.0"

    def test_custom_log_level(self):
        config = CodeKeeperConfig(log_level="DEBUG")

        assert config.log_level == "DEBUG"

    def test_path_absolute_vs_relative(self):
        config = CodeKeeperConfig(
            cache_dir=Path("/absolute/path"),
            snapshot_dir=Path("./relative/path"),
        )

        assert str(config.cache_dir).startswith("/")
        assert not str(config.snapshot_dir).startswith("/")

    def test_max_workers_boundary_values(self):
        config_min = CodeKeeperConfig(max_workers=1)
        config_max = CodeKeeperConfig(max_workers=100)

        assert config_min.max_workers == 1
        assert config_max.max_workers == 100

    def test_config_immutable_after_creation(self):
        from pydantic import ValidationError

        config = CodeKeeperConfig(author="Test")

        with pytest.raises(ValidationError):
            config.author = "Changed"

    def test_model_dump_returns_dict(self):
        config = CodeKeeperConfig(author="Test Author", max_workers=8)

        data = config.model_dump()

        assert isinstance(data, dict)
        assert data["author"] == "Test Author"
        assert data["max_workers"] == 8

    def test_model_dump_json_returns_json_string(self):
        config = CodeKeeperConfig(author="Test Author")

        json_str = config.model_dump_json()

        assert isinstance(json_str, str)
        assert "Test Author" in json_str


class TestConfigValidation:
    def test_max_workers_minimum(self):
        with pytest.raises(ConfigurationError):
            CodeKeeperConfig(max_workers=0)

    def test_max_workers_negative(self):
        with pytest.raises(ConfigurationError):
            CodeKeeperConfig(max_workers=-1)

    def test_max_workers_maximum(self):
        with pytest.raises(ConfigurationError):
            CodeKeeperConfig(max_workers=129)

    def test_max_workers_valid_boundary(self):
        config_min = CodeKeeperConfig(max_workers=1)
        config_max = CodeKeeperConfig(max_workers=128)

        assert config_min.max_workers == 1
        assert config_max.max_workers == 128

    def test_invalid_log_level(self):
        with pytest.raises(ConfigurationError):
            CodeKeeperConfig(log_level="INVALID")

    def test_log_level_case_insensitive(self):
        config = CodeKeeperConfig(log_level="debug")
        assert config.log_level == "DEBUG"

    def test_valid_log_levels(self):
        for level in VALID_LOG_LEVELS:
            config = CodeKeeperConfig(log_level=level)
            assert config.log_level == level

    def test_invalid_license(self):
        with pytest.raises(ConfigurationError):
            CodeKeeperConfig(license="InvalidLicense")

    def test_valid_licenses(self):
        for lic in ["MIT", "Apache-2.0", "GPL-3.0", "BSD-3-Clause", "Proprietary"]:
            config = CodeKeeperConfig(license=lic)
            assert config.license == lic


class TestConfigFileOperations:
    def test_save_and_load_config(self):
        config = CodeKeeperConfig(
            author="Test Author",
            license="Apache-2.0",
            max_workers=8,
            log_level="DEBUG",
            ignore_patterns=["*.log", "*.tmp"],
        )

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            temp_path = Path(f.name)

        try:
            save_config(config, temp_path)
            loaded_config = load_config(temp_path)

            assert loaded_config.author == "Test Author"
            assert loaded_config.license == "Apache-2.0"
            assert loaded_config.max_workers == 8
            assert loaded_config.log_level == "DEBUG"
            assert "*.log" in loaded_config.ignore_patterns
        finally:
            if temp_path.exists():
                os.unlink(temp_path)

    def test_load_config_from_nonexistent_file(self):
        config = load_config(Path("/nonexistent/path/config.json"))

        assert isinstance(config, CodeKeeperConfig)

    def test_save_config_creates_parent_directories(self):
        config = CodeKeeperConfig(author="Test")

        temp_dir = tempfile.mkdtemp()
        nested_path = Path(temp_dir) / "nested" / "deep" / "config.json"

        try:
            save_config(config, nested_path)
            assert nested_path.exists()
        finally:
            import shutil

            shutil.rmtree(temp_dir, ignore_errors=True)

    def test_save_config_writes_valid_json(self):
        config = CodeKeeperConfig(
            author="JSON Test",
            max_workers=16,
            cache_dir=Path("/test/cache"),
        )

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            temp_path = Path(f.name)

        try:
            save_config(config, temp_path)
            with open(temp_path) as f:
                data = json.load(f)

            assert data["author"] == "JSON Test"
            assert data["max_workers"] == 16
            assert data["cache_dir"] == "/test/cache"
        finally:
            if temp_path.exists():
                os.unlink(temp_path)

    def test_load_config_invalid_json_raises_error(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write("{ invalid json }")
            temp_path = Path(f.name)

        try:
            with pytest.raises(ConfigFileError):
                load_config(temp_path)
        finally:
            if temp_path.exists():
                os.unlink(temp_path)

    def test_load_config_invalid_values_raises_error(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump({"max_workers": -1}, f)
            temp_path = Path(f.name)

        try:
            with pytest.raises(ConfigurationError):
                load_config(temp_path)
        finally:
            if temp_path.exists():
                os.unlink(temp_path)

    def test_load_config_ignores_extra_fields(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(
                {
                    "author": "Test",
                    "unknown_field": "should be ignored",
                    "extra_nested": {"key": "value"},
                },
                f,
            )
            temp_path = Path(f.name)

        try:
            config = load_config(temp_path)
            assert config.author == "Test"
        finally:
            if temp_path.exists():
                os.unlink(temp_path)


class TestConfigImmutability:
    def test_config_is_frozen(self):
        config = CodeKeeperConfig(author="Original")

        with pytest.raises((TypeError, ValueError)):
            config.author = "Modified"

    def test_config_equality_works(self):
        config1 = CodeKeeperConfig(author="Test", max_workers=8)
        config2 = CodeKeeperConfig(author="Test", max_workers=8)
        config3 = CodeKeeperConfig(author="Test", max_workers=4)

        assert config1 == config2
        assert config1 != config3

    def test_config_copy_creates_new_instance(self):
        config1 = CodeKeeperConfig(author="Original")
        config2 = config1.model_copy()

        assert config1 == config2
        assert config1 is not config2


class TestConfigSerialization:
    def test_model_dump_converts_paths_to_strings(self):
        config = CodeKeeperConfig(
            cache_dir=Path("/test/cache"),
            snapshot_dir=Path("/test/snapshots"),
        )

        data = config.model_dump()

        assert isinstance(data["cache_dir"], str)
        assert isinstance(data["snapshot_dir"], str)
        assert data["cache_dir"] == "/test/cache"
        assert data["snapshot_dir"] == "/test/snapshots"

    def test_model_dump_json_contains_all_fields(self):
        config = CodeKeeperConfig(
            author="Test",
            license="MIT",
            max_workers=4,
            log_level="INFO",
        )

        json_str = config.model_dump_json()
        data = json.loads(json_str)

        assert data["author"] == "Test"
        assert data["license"] == "MIT"
        assert data["max_workers"] == 4
        assert data["log_level"] == "INFO"

    def test_config_round_trip_json(self):
        original = CodeKeeperConfig(
            author="Round Trip Test",
            license="Apache-2.0",
            max_workers=16,
            log_level="WARNING",
            ignore_patterns=["*.log", "*.tmp", "*.bak"],
        )

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            temp_path = Path(f.name)

        try:
            save_config(original, temp_path)
            loaded = load_config(temp_path)

            assert loaded.author == original.author
            assert loaded.license == original.license
            assert loaded.max_workers == original.max_workers
            assert loaded.log_level == original.log_level
            assert loaded.ignore_patterns == original.ignore_patterns
        finally:
            if temp_path.exists():
                os.unlink(temp_path)
