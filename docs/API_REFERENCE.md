<div align="center">

# 📘 API Reference

### Complete API Documentation

[🏠 Home](../README.md) • [📖 User Guide](USER_GUIDE.md)

---

</div>

## 📋 Table of Contents

- [Overview](#overview)
- [Core API](#core-api)
    - [CodeKeeper Class](#codekeeper-class)
    - [Initialization](#initialization)
    - [File Scanning](#file-scanning)
    - [Copyright Management](#copyright-management)
    - [Junk File Cleaning](#junk-file-cleaning)
    - [Annotation Scanning](#annotation-scanning)
- [Configuration](#configuration)
- [Type Definitions](#type-definitions)
- [Examples](#examples)

---

## Overview

<div align="center">

### 🎯 API Design Principles

</div>

<table>
<tr>
<td width="25%" align="center">
<img src="https://img.icons8.com/fluency/96/000000/easy.png" width="64"><br>
<b>Simple</b><br>
Intuitive and easy to use
</td>
<td width="25%" align="center">
<img src="https://img.icons8.com/fluency/96/000000/security-checked.png" width="64"><br>
<b>Safe</b><br>
Type-safe and secure by default
</td>
<td width="25%" align="center">
<img src="https://img.icons8.com/fluency/96/000000/module.png" width="64"><br>
<b>Composable</b><br>
Build complex workflows easily
</td>
<td width="25%" align="center">
<img src="https://img.icons8.com/fluency/96/000000/documentation.png" width="64"><br>
<b>Well-documented</b><br>
Comprehensive documentation
</td>
</tr>
</table>

CodeKeeper provides a unified Python API for code quality management, including copyright header management, junk file cleaning, and annotation scanning across multiple programming languages.

---

## Core API

### CodeKeeper Class

<div align="center">

#### 🚀 Main Entry Point

</div>

---

#### `CodeKeeper`

Main entry point for CodeKeeper operations. Provides unified access to all code quality management features.

<table>
<tr>
<td width="30%"><b>Signature</b></td>
<td width="70%">

```python
from codekeeper.core.api import CodeKeeper

keeper = CodeKeeper(
    root_dir: Path | None = None,
    config_path: Path | None = None,
    apm_enabled: bool = True,
    apm_vendor: str = "custom",
)
```

</td>
</tr>
<tr>
<td><b>Description</b></td>
<td>Initializes the CodeKeeper instance with optional root directory and configuration.</td>
</tr>
<tr>
<td><b>Parameters</b></td>
<td>

- `root_dir: Path | None` - Root directory of the project (default: current working directory)
- `config_path: Path | None` - Path to configuration file
- `apm_enabled: bool` - Whether to enable APM integration (default: True)
- `apm_vendor: str` - APM vendor (datadog, prometheus, opentelemetry, custom)

</td>
</tr>
</table>

**Example:**

```python
from pathlib import Path
from codekeeper.core.api import CodeKeeper

keeper = CodeKeeper(
    root_dir=Path("/path/to/project"),
    apm_enabled=True,
    apm_vendor="custom"
)
```

---

#### `initialize_apm()`

Initialize APM with configuration.

<table>
<tr>
<td width="30%"><b>Signature</b></td>
<td width="70%">

```python
def initialize_apm(self, config: dict) -> None
```

</td>
</tr>
<tr>
<td><b>Parameters</b></td>
<td>

- `config: dict` - APM configuration dictionary

</td>
</tr>
<tr>
<td><b>Returns</b></td>
<td>`None`</td>
</tr>
</table>

**Example:**

```python
keeper.initialize_apm({
    "service_name": "codekeeper",
    "environment": "production"
})
```

---

#### `get_performance_summary()`

Get performance monitoring summary.

<table>
<tr>
<td width="30%"><b>Signature</b></td>
<td width="70%">

```python
def get_performance_summary(self) -> dict
```

</td>
</tr>
<tr>
<td><b>Returns</b></td>
<td>`dict` - Performance metrics dictionary</td>
</tr>
</table>

**Example:**

```python
summary = keeper.get_performance_summary()
print(f"Operations: {summary}")
```

---

#### `get_apm_report()`

Get APM report.

<table>
<tr>
<td width="30%"><b>Signature</b></td>
<td width="70%">

```python
def get_apm_report(self) -> dict
```

</td>
</tr>
<tr>
<td><b>Returns</b></td>
<td>`dict` - APM report dictionary</td>
</tr>
</table>

---

#### `flush_apm()`

Flush APM data. Should be called periodically to send metrics to the APM backend.

<table>
<tr>
<td width="30%"><b>Signature</b></td>
<td width="70%">

```python
def flush_apm(self) -> None
```

</td>
</tr>
<tr>
<td><b>Returns</b></td>
<td>`None`</td>
</tr>
</table>

---

### File Scanning

<div align="center">

#### 📁 File Discovery and Analysis

</div>

---

#### `scan()`

Scan for code files in the project.

<table>
<tr>
<td width="30%"><b>Signature</b></td>
<td width="70%">

```python
def scan(self, recursive: bool = True) -> list[Path]
```

</td>
</tr>
<tr>
<td><b>Parameters</b></td>
<td>

- `recursive: bool` - Whether to scan recursively (default: True)

</td>
</tr>
<tr>
<td><b>Returns</b></td>
<td>`list[Path]` - List of file paths</td>
</tr>
<tr>
<td><b>Raises</b></td>
<td>

- `InvalidPathError` - If root directory is invalid

</td>
</tr>
</table>

**Example:**

```python
from codekeeper.core.api import CodeKeeper

keeper = CodeKeeper()
files = keeper.scan(recursive=True)
print(f"Found {len(files)} files")
for f in files[:5]:
    print(f)
```

---

#### `analyze()`

Analyze a single file.

<table>
<tr>
td width="30%"><b>Signature</b></td>
<td width="70%">

```python
def analyze(self, file_path: Path) -> dict
```

</td>
</tr>
<tr>
<td><b>Parameters</b></td>
<td>

- `file_path: Path` - Path to the file

</td>
</tr>
<tr>
<td><b>Returns</b></td>
<td>`dict` - Analysis result dictionary</td>
</tr>
<tr>
<td><b>Raises</b></td>
<td>

- `InvalidPathError` - If file path is invalid
- `PathTraversalError` - If path traversal attack detected

</td>
</tr>
</table>

**Example:**

```python
from pathlib import Path
from codekeeper.core.api import CodeKeeper

keeper = CodeKeeper()
result = keeper.analyze(Path("src/main.py"))
print(result)
```

---

### Copyright Management

<div align="center">

#### 📝 Copyright Header Operations

</div>

---

#### `add_copyright_headers()`

Add copyright headers to all supported files in the project.

<table>
<tr>
<td width="30%"><b>Signature</b></td>
<td width="70%">

```python
def add_copyright_headers(
    self,
    recursive: bool = True,
    license_type: str = "MIT",
    author: str | None = None,
    year_range: str | None = None,
    overwrite_mode: OverwriteMode = OverwriteMode.UPDATE_YEAR,
    skip_if_exists: bool = True,
    extensions: list[str] | None = None,
) -> list[CopyrightResult]
```

</td>
</tr>
<tr>
<td><b>Parameters</b></td>
<td>

- `recursive: bool` - Whether to scan recursively (default: True)
- `license_type: str` - License type to use (mit, apache-2.0, gpl-3.0, bsd-3-clause)
- `author: str | None` - Copyright author name
- `year_range: str | None` - Year range (e.g., "2023-2025")
- `overwrite_mode: OverwriteMode` - How to handle existing copyright headers
- `skip_if_exists: bool` - Skip files that already have copyright headers
- `extensions: list[str] | None` - File extensions to process

</td>
</tr>
<tr>
<td><b>Returns</b></td>
<td>`list[CopyrightResult]` - List of CopyrightResult objects</td>
</tr>
</table>

**Example:**

```python
from codekeeper.core.api import CodeKeeper
from codekeeper.core.copyright import OverwriteMode

keeper = CodeKeeper()
results = keeper.add_copyright_headers(
    license_type="MIT",
    author="John Doe",
    year_range="2023-2025",
    overwrite_mode=OverwriteMode.UPDATE_YEAR,
    extensions=["py", "js", "ts"]
)
print(f"Processed {len(results)} files")
```

---

#### `remove_copyright_headers()`

Remove copyright headers from all supported files in the project.

<table>
<tr>
<td width="30%"><b>Signature</b></td>
<td width="70%">

```python
def remove_copyright_headers(
    self,
    recursive: bool = True,
    extensions: list[str] | None = None,
) -> list[CopyrightResult]
```

</td>
</tr>
<tr>
<td><b>Parameters</b></td>
<td>

- `recursive: bool` - Whether to scan recursively (default: True)
- `extensions: list[str] | None` - File extensions to process

</td>
</tr>
<tr>
<td><b>Returns</b></td>
<td>`list[CopyrightResult]` - List of CopyrightResult objects</td>
</tr>
</table>

**Example:**

```python
from codekeeper.core.api import CodeKeeper

keeper = CodeKeeper()
results = keeper.remove_copyright_headers(
    extensions=["py", "js"]
)
print(f"Removed copyright from {len(results)} files")
```

---

#### `validate_copyright_headers()`

Validate copyright headers in all supported files.

<table>
<tr>
<td width="30%"><b>Signature</b></td>
<td width="70%">

```python
def validate_copyright_headers(
    self,
    recursive: bool = True,
    extensions: list[str] | None = None,
) -> list[CopyrightResult]
```

</td>
</tr>
<tr>
<td><b>Parameters</b></td>
<td>

- `recursive: bool` - Whether to scan recursively (default: True)
- `extensions: list[str] | None` - File extensions to process

</td>
</tr>
<tr>
<td><b>Returns</b></td>
<td>`list[CopyrightResult]` - List of CopyrightResult objects with validation status</td>
</tr>
</table>

**Example:**

```python
from codekeeper.core.api import CodeKeeper

keeper = CodeKeeper()
results = keeper.validate_copyright_headers()
invalid = [r for r in results if not r.success or r.action == "skip"]
print(f"Invalid copyright headers: {len(invalid)}")
```

---

### Junk File Cleaning

<div align="center">

#### 🧹 Junk File Detection and Removal

</div>

---

#### `clean_junk_files()`

Scan and optionally clean junk files.

<table>
<tr>
<td width="30%"><b>Signature</b></td>
<td width="70%">

```python
def clean_junk_files(
    self,
    paths: list[Path] | None = None,
    recursive: bool = True,
    confirm: bool = False,
) -> tuple[list[CleanResult], CleanStats]
```

</td>
</tr>
<tr>
<td><b>Parameters</b></td>
<td>

- `paths: list[Path] | None` - Paths to scan (default: root_dir)
- `recursive: bool` - Whether to scan recursively (default: True)
- `confirm: bool` - Whether to actually remove files (False = preview mode)

</td>
</tr>
<tr>
<td><b>Returns</b></td>
<td>`tuple[list[CleanResult], CleanStats]` - Tuple of (CleanResult list, CleanStats)</td>
</tr>
<tr>
<td><b>Raises</b></td>
<td>

- `InvalidPathError` - If any path is invalid
- `PathTraversalError` - If path traversal attack detected

</td>
</tr>
</table>

**Example:**

```python
from pathlib import Path
from codekeeper.core.api import CodeKeeper

keeper = CodeKeeper()

results, stats = keeper.clean_junk_files(
    paths=[Path(".")],
    confirm=False  # Preview mode
)
print(f"Found {stats.total_junk_found} junk files")
print(f"Total size: {stats.total_size_bytes} bytes")
```

---

#### `preview_junk_files()`

Preview junk files without cleaning.

<table>
<tr>
<td width="30%"><b>Signature</b></td>
<td width="70%">

```python
def preview_junk_files(
    self,
    paths: list[Path] | None = None,
    recursive: bool = True,
) -> tuple[list[JunkFile], CleanStats]
```

</td>
</tr>
<tr>
<td><b>Parameters</b></td>
<td>

- `paths: list[Path] | None` - Paths to scan (default: root_dir)
- `recursive: bool` - Whether to scan recursively (default: True)

</td>
</tr>
<tr>
<td><b>Returns</b></td>
<td>`tuple[list[JunkFile], CleanStats]` - Tuple of (JunkFile list, CleanStats)</td>
</tr>
</table>

**Example:**

```python
from pathlib import Path
from codekeeper.core.api import CodeKeeper

keeper = CodeKeeper()
junk_files, stats = keeper.preview_junk_files()
print(f"Junk files by type:")
for junk_type, count in stats.junk_by_type.items():
    print(f"  {junk_type.value}: {count}")
```

---

#### `register_junk_pattern()`

Register a custom junk file pattern for detection.

<table>
<tr>
<td width="30%"><b>Signature</b></td>
<td width="70%">

```python
def register_junk_pattern(
    self,
    pattern: str,
    name: str | None = None,
    _description: str = "",
    _severity: str = "low",
) -> None
```

</td>
</tr>
<tr>
<td><b>Parameters</b></td>
<td>

- `pattern: str` - Regex pattern for matching files
- `name: str | None` - Pattern name (auto-generated if not provided)
- `_description: str` - Pattern description
- `_severity: str` - Pattern severity (low, medium, high)

</td>
</tr>
<tr>
<td><b>Returns</b></td>
<td>`None`</td>
</tr>
</table>

**Example:**

```python
from codekeeper.core.api import CodeKeeper

keeper = CodeKeeper()
keeper.register_junk_pattern(
    pattern=r".*\.log\d*$",
    name="rotated_logs",
    _description="Rotated log files",
    _severity="low"
)
```

---

### Annotation Scanning

<div align="center">

#### 🔍 Documentation Coverage Analysis

</div>

---

#### `scan_function_annotations()`

Scan for functions with missing documentation comments.

<table>
<tr>
<td width="30%"><b>Signature</b></td>
<td width="70%">

```python
def scan_function_annotations(
    self,
    recursive: bool = True,
    skip_private: bool = False,
    skip_dunder: bool = True,
    extensions: list[str] | None = None,
) -> list[AnnotationResult]
```

</td>
</tr>
<tr>
<td><b>Parameters</b></td>
<td>

- `recursive: bool` - Whether to scan recursively (default: True)
- `skip_private: bool` - Whether to skip private functions (starting with _)
- `skip_dunder: bool` - Whether to skip dunder methods (default: True)
- `extensions: list[str] | None` - File extensions to process

</td>
</tr>
<tr>
<td><b>Returns</b></td>
<td>`list[AnnotationResult]` - List of AnnotationResult objects</td>
</tr>
</table>

**Example:**

```python
from codekeeper.core.api import CodeKeeper

keeper = CodeKeeper()
results = keeper.scan_function_annotations(
    recursive=True,
    skip_private=False,
    extensions=["py", "js", "ts"]
)
print(f"Found {len(results)} files with undocumented functions")
```

---

#### `get_missing_annotations()`

Get list of functions that are missing documentation comments.

<table>
<tr>
<td width="30%"><b>Signature</b></td>
<td width="70%">

```python
def get_missing_annotations(
    self,
    recursive: bool = True,
    skip_private: bool = False,
    skip_dunder: bool = True,
    extensions: list[str] | None = None,
) -> list[FunctionInfo]
```

</td>
</tr>
<tr>
<td><b>Parameters</b></td>
<td>

- `recursive: bool` - Whether to scan recursively (default: True)
- `skip_private: bool` - Whether to skip private functions (starting with _)
- `skip_dunder: bool` - Whether to skip dunder methods (default: True)
- `extensions: list[str] | None` - File extensions to process

</td>
</tr>
<tr>
<td><b>Returns</b></td>
<td>`list[FunctionInfo]` - List of FunctionInfo objects for functions without comments</td>
</tr>
</table>

**Example:**

```python
from codekeeper.core.api import CodeKeeper

keeper = CodeKeeper()
missing = keeper.get_missing_annotations(extensions=["py"])
print(f"Found {len(missing)} functions without documentation")
for func in missing[:5]:
    print(f"  {func.file_path}:{func.line_number} - {func.name}")
```

---

#### `annotation_summary()`

Get summary of annotation coverage.

<table>
<tr>
<td width="30%"><b>Signature</b></td>
<td width="70%">

```python
def annotation_summary(
    self,
    recursive: bool = True,
    extensions: list[str] | None = None,
) -> dict
```

</td>
</tr>
<tr>
<td><b>Parameters</b></td>
<td>

- `recursive: bool` - Whether to scan recursively (default: True)
- `extensions: list[str] | None` - File extensions to process

</td>
</tr>
<tr>
<td><b>Returns</b></td>
<td>`dict` - Summary dictionary with annotation statistics including files_scanned, total_functions, functions_with_comments, functions_without_comments, and annotation_coverage_percent</td>
</tr>
</table>

**Example:**

```python
from codekeeper.core.api import CodeKeeper

keeper = CodeKeeper()
summary = keeper.annotation_summary()
print(f"Annotation Coverage: {summary['annotation_coverage_percent']:.1f}%")
print(f"Functions with comments: {summary['functions_with_comments']}/{summary['total_functions']}")
```

---

## Configuration

<div align="center">

#### ⚙️ Configuration Management

</div>

### Environment Variables

<table>
<tr>
<th>Variable</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
<tr>
<td><code>CODEKEEPER_ROOT</code></td>
<td>string</td>
<td>Current directory</td>
<td>Root directory of the project</td>
</tr>
<tr>
<td><code>CODEKEEPER_CONFIG</code></td>
<td>string</td>
<td>None</td>
<td>Path to configuration file</td>
</tr>
<tr>
<td><code>CODEKEEPER_APM</code></td>
<td>bool</td>
<td>True</td>
<td>Enable APM integration</td>
</tr>
<tr>
<td><code>CODEKEEPER_APM_VENDOR</code></td>
<td>string</td>
<td>custom</td>
<td>APM vendor (datadog, prometheus, opentelemetry, custom)</td>
</tr>
</table>

### Configuration File

```python
# codekeeper.config.yaml
root_dir: /path/to/project
config_path: /path/to/config.yaml
apm_enabled: true
apm_vendor: custom
```

---

## Type Definitions

<div align="center">

#### 📦 Core Data Types

</div>

### OverwriteMode Enum

```python
from codekeeper.core.copyright import OverwriteMode

class OverwriteMode(Enum):
    SKIP = "skip"
    UPDATE_YEAR = "update_year"
    OVERWRITE = "overwrite"
```

### CopyrightResult Dataclass

```python
from dataclasses import dataclass
from pathlib import Path

@dataclass
class CopyrightResult:
    file_path: Path
    success: bool
    action: str
    message: str
    old_content: str | None = None
    new_content: str | None = None
```

### JunkType Enum

```python
from codekeeper.core.clean import JunkType

class JunkType(Enum):
    EDITOR_TEMP = "editor_temp"
    OS_CACHE = "os_cache"
    PYTHON_CACHE = "python_cache"
    BUILD_ARTIFACT = "build_artifact"
    EMPTY_FILE = "empty_file"
    ORPHAN_FILE = "orphan_file"
    LOG_FILE = "log_file"
    UNKNOWN = "unknown"
```

### JunkFile Dataclass

```python
from dataclasses import dataclass
from pathlib import Path

@dataclass
class JunkFile:
    file_path: Path
    junk_type: JunkType
    size_bytes: int = 0
    modified_time: float = 0
    reason: str = ""
```

### CleanResult Dataclass

```python
from dataclasses import dataclass
from pathlib import Path

@dataclass
class CleanResult:
    file_path: Path
    success: bool
    action: str
    message: str
    junk_type: JunkType | None = None
    original_size: int = 0
```

### CleanStats Dataclass

```python
from dataclasses import dataclass, field

@dataclass
class CleanStats:
    total_scanned: int = 0
    total_junk_found: int = 0
    total_size_bytes: int = 0
    files_deleted: int = 0
    bytes_freed: int = 0
    errors: int = 0
    junk_by_type: dict[JunkType, int] = field(default_factory=dict)
    junk_by_type_bytes: dict[JunkType, int] = field(default_factory=dict)

    def to_dict(self) -> dict:
        # Returns dictionary representation
```

### AnnotationResult Dataclass

```python
from dataclasses import dataclass
from pathlib import Path

@dataclass
class AnnotationResult:
    file_path: Path
    function_name: str
    line_number: int
    has_docstring: bool
    missing_params: list[str] = field(default_factory=list)
```

---

## Examples

<div align="center">

### 💡 Common Usage Patterns

</div>

### Example 1: Basic Setup and File Scanning

```python
from pathlib import Path
from codekeeper.core.api import CodeKeeper

keeper = CodeKeeper(
    root_dir=Path("/path/to/project"),
    apm_enabled=True,
    apm_vendor="custom"
)

files = keeper.scan(recursive=True)
print(f"Found {len(files)} files")
```

### Example 2: Copyright Header Management

```python
from codekeeper.core.api import CodeKeeper
from codekeeper.core.copyright import OverwriteMode

keeper = CodeKeeper()

results = keeper.add_copyright_headers(
    license_type="MIT",
    author="John Doe",
    year_range="2023-2025",
    overwrite_mode=OverwriteMode.UPDATE_YEAR,
    extensions=["py", "js", "ts", "java"]
)

success_count = sum(1 for r in results if r.success)
print(f"Successfully processed {success_count}/{len(results)} files")
```

### Example 3: Junk File Cleaning

```python
from pathlib import Path
from codekeeper.core.api import CodeKeeper

keeper = CodeKeeper()

print("Previewing junk files...")
junk_files, stats = keeper.preview_junk_files(
    paths=[Path(".")]
)

print(f"Total junk files: {stats.total_junk_found}")
print(f"Total size: {stats.total_size_bytes / 1024 / 1024:.2f} MB")
print(f"By type: {dict(stats.junk_by_type)}")

if input("Clean these files? [y/N]: ").lower() == "y":
    results, clean_stats = keeper.clean_junk_files(
        paths=[Path(".")],
        confirm=True
    )
    print(f"Deleted {clean_stats.files_deleted} files")
    print(f"Freed {clean_stats.bytes_freed / 1024 / 1024:.2f} MB")
```

### Example 4: Annotation Scanning

```python
from codekeeper.core.api import CodeKeeper

keeper = CodeKeeper()

results = keeper.scan_function_annotations(
    extensions=["py"],
    skip_private=True,
    skip_dunder=True
)

missing_docs = [r for r in results if r.functions_without_comments > 0]
print(f"Files with undocumented functions: {len(missing_docs)}")

for result in missing_docs[:10]:
    print(f"  {result.file_path}: {result.functions_without_comments} functions need documentation")
```

### Example 5: Full Workflow

```python
from pathlib import Path
from codekeeper.core.api import CodeKeeper
from codekeeper.core.copyright import OverwriteMode

keeper = CodeKeeper(root_dir=Path("/path/to/project"))

print("=" * 50)
print("CodeKeeper Analysis Report")
print("=" * 50)

print("\n1. Scanning project files...")
files = keeper.scan(recursive=True)
print(f"   Found {len(files)} files")

print("\n2. Checking copyright headers...")
copyright_results = keeper.validate_copyright_headers()
missing_copyright = [r for r in copyright_results if not r.success]
print(f"   {len(copyright_results) - len(missing_copyright)} files have valid copyright")

print("\n3. Previewing junk files...")
_, junk_stats = keeper.preview_junk_files()
print(f"   {junk_stats.total_junk_found} junk files found")
print(f"   {junk_stats.total_size_bytes / 1024 / 1024:.2f} MB of junk")

print("\n4. Scanning for missing documentation...")
annotation_results = keeper.scan_function_annotations()
print(f"   {sum(r.functions_without_comments for r in annotation_results)} functions need documentation")

print("\n" + "=" * 50)
print("APM Performance Summary")
print("=" * 50)
print(keeper.get_performance_summary())
```

---

<div align="center">

**[📖 User Guide](USER_GUIDE.md)** • **[🏗️ Architecture](ARCHITECTURE.md)** • **[🏠 Home](../README.md)**

Made with ❤️ by the CodeKeeper Team

[⬆ Back to Top](#-api-reference)
