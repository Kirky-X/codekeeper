<div align="center">

# ❓ Frequently Asked Questions (FAQ)

### Quick Answers to Common Questions

[🏠 Home](../README.md) • [📖 User Guide](USER_GUIDE.md)

---

</div>

## 📋 Table of Contents

- [General Questions](#general-questions)
- [Installation & Setup](#installation--setup)
- [Usage & Features](#usage--features)
- [Performance](#performance)
- [Security](#security)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Licensing](#licensing)

---

## General Questions

<div align="center">

### 🤔 About CodeKeeper

</div>

<details>
<summary><b>❓ What is CodeKeeper?</b></summary>

<br>

**CodeKeeper** is a powerful code management toolkit designed to help you maintain code quality through automated operations. It provides:

- ✅ **Copyright Header Management** - Automatically add, update, and validate copyright headers in code files
- ✅ **Junk File Cleaning** - Scan for and remove junk files based on customizable patterns
- ✅ **Annotation Scanning** - Identify functions missing documentation comments or type annotations
- ✅ **Multi-Language Support** - Supports Python, Rust, Java, Go, C++, TypeScript, and more

**Target Audience:** Developers and teams who want to maintain consistent code quality and reduce technical debt.

**Learn more:** [User Guide](USER_GUIDE.md)

</details>

<details>
<summary><b>❓ Why should I use CodeKeeper instead of alternatives?</b></summary>

<br>

<table>
<tr>
<th>Feature</th>
<th>CodeKeeper</th>
<th>Manual Checks</th>
<th>Other Tools</th>
</tr>
<tr>
<td>Copyright Management</td>
<td>✅ Automated</td>
<td>❌ Manual</td>
<td>⚠️ Limited</td>
</tr>
<tr>
<td>Junk File Cleaning</td>
<td>✅ Built-in Patterns</td>
<td>❌ Manual</td>
<td>⚠️ Separate tools</td>
</tr>
<tr>
<td>Annotation Coverage</td>
<td>✅ Detailed Reports</td>
<td>❌ Manual</td>
<td>⚠️ Basic</td>
</tr>
<tr>
<td>Multi-Language</td>
<td>✅ 6+ Languages</td>
<td>N/A</td>
<td>⚠️ Varies</td>
</tr>
<tr>
<td>Easy to Use</td>
<td>✅ Simple Python API</td>
<td>N/A</td>
<td>⚠️ Complex</td>
</tr>
</table>

**Key Advantages:**

- 🚀 Single tool for multiple code quality tasks
- 🔒 Written in Python with type safety
- 💡 Simple and intuitive API
- 📖 Comprehensive documentation

</details>

<details>
<summary><b>❓ Is CodeKeeper production-ready?</b></summary>

<br>

**Current Status:** ✅ **Yes, production-ready!**

<table>
<tr>
<td width="50%">

**What's Ready:**

- ✅ Core functionality stable and tested
- ✅ Comprehensive error handling
- ✅ Performance monitoring with APM
- ✅ Well documented with examples

</td>
<td width="50%">

**Features:**

- 📊 Code quality metrics
- 🔧 Configurable via JSON/YAML
- 📈 Performance tracking
- 🔒 Security-conscious design

</td>
</tr>
</table>

> **Note:** Always review the [CHANGELOG](../CHANGELOG.md) before upgrading versions.

</details>

<details>
<summary><b>❓ What platforms are supported?</b></summary>

<br>

<table>
<tr>
<th>Platform</th>
<th>Architecture</th>
<th>Status</th>
<th>Notes</th>
</tr>
<tr>
<td rowspan="2"><b>Linux</b></td>
<td>x86_64</td>
<td>✅ Fully Supported</td>
<td>Primary platform</td>
</tr>
<tr>
<td>ARM64</td>
<td>✅ Fully Supported</td>
<td>Tested on ARM servers</td>
</tr>
<tr>
<td rowspan="2"><b>macOS</b></td>
<td>x86_64</td>
<td>✅ Fully Supported</td>
<td>Intel Macs</td>
</tr>
<tr>
<td>ARM64</td>
<td>✅ Fully Supported</td>
<td>Apple Silicon (M1/M2/M3)</td>
</tr>
<tr>
<td><b>Windows</b></td>
<td>x86_64</td>
<td>✅ Fully Supported</td>
<td>Windows 10+</td>
</tr>
</table>

**Requirements:** Python 3.10 or higher

</details>

<details>
<summary><b>❓ What programming languages are supported?</b></summary>

<br>

<table>
<tr>
<td width="33%" align="center">

**🐍 Python**

✅ **Full Support**

All features available

</td>
<td width="33%" align="center">

**🦀 Rust**

✅ **Full Support**

All features available

</td>
<td width="33%" align="center">

**☕ Java**

✅ **Full Support**

All features available

</td>
</tr>
<tr>
<td width="33%" align="center">

**🔷 Go**

✅ **Full Support**

All features available

</td>
<td width="33%" align="center">

**⚡ C/C++**

✅ **Full Support**

All features available

</td>
<td width="33%" align="center">

**📘 TypeScript**

✅ **Full Support**

All features available

</td>
</tr>
</table>

**Documentation:**

- [User Guide](USER_GUIDE.md)
- [API Reference](../api/)

</details>

---

## Installation & Setup

<div align="center">

### 🚀 Getting Started

</div>

<details>
<summary><b>❓ How do I install CodeKeeper?</b></summary>

<br>

**Using pip (Recommended):**

```bash
# Install from PyPI
pip install codekeeper

# Or install latest from GitHub
pip install git+https://github.com/your-org/codekeeper.git
```

**Using uv (Modern Python Package Manager):**

```bash
uv pip install codekeeper
```

**From Source:**

```bash
git clone https://github.com/your-org/codekeeper
cd codekeeper
pip install -e .
```

**Verification:**

```python
from codekeeper import CodeKeeper
from pathlib import Path

keeper = CodeKeeper(root_dir=Path.cwd())
print("✅ CodeKeeper is ready!")
```

**See also:** [Installation Guide](USER_GUIDE.md#installation)

</details>

<details>
<summary><b>❓ What are the system requirements?</b></summary>

<br>

**Minimum Requirements:**

<table>
<tr>
<th>Component</th>
<th>Requirement</th>
<th>Recommended</th>
</tr>
<tr>
<td>Python Version</td>
<td>3.10+</td>
<td>3.11 or 3.12</td>
</tr>
<tr>
<td>Memory</td>
<td>256 MB</td>
<td>512 MB+</td>
</tr>
<tr>
<td>Disk Space</td>
<td>10 MB</td>
<td>50 MB+</td>
</tr>
<tr>
<td>CPU</td>
<td>1 core</td>
<td>2+ cores</td>
</tr>
</table>

**Required Dependencies:**

- pydantic (configuration and validation)
- pathspec (file pattern matching)

**Optional:**

- 🔧 Docker (for containerized deployment)

</details>

<details>
<summary><b>❓ I'm getting import errors, what should I do?</b></summary>

<br>

**Common Solutions:**

1. **Check Python version:**
   ```bash
   python --version
   # Must be 3.10 or higher
   ```

2. **Verify installation:**
   ```bash
   pip show codekeeper
   ```

3. **Reinstall package:**
   ```bash
   pip uninstall codekeeper
   pip install codekeeper
   ```

4. **Check virtual environment:**
   ```bash
   # Make sure you're in the right environment
   which python
   pip list | grep codekeeper
   ```

**Still having issues?**

- 📝 Check [Troubleshooting Guide](#troubleshooting)
- 🐛 [Open an issue](../../issues) with error details

</details>

<details>
<summary><b>❓ Can I use this with Docker?</b></summary>

<br>

**Yes!** Here's a sample Dockerfile:

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "your_script.py"]
```

**Docker Compose:**

```yaml
version: '3.8'
services:
  codekeeper:
    build: .
    volumes:
      - .:/app
    environment:
      - CODEKEEPER_LOG_LEVEL=INFO
```

**Pre-built Images:**

```bash
docker pull ghcr.io/your-org/codekeeper:latest
```

</details>

---

## Usage & Features

<div align="center">

### 💡 Working with the API

</div>

<details>
<summary><b>❓ How do I get started with basic usage?</b></summary>

<br>

**5-Minute Quick Start:**

```python
from pathlib import Path
from codekeeper import CodeKeeper
from codekeeper.core.copyright import OverwriteMode

def main():
    # 1. Initialize CodeKeeper
    keeper = CodeKeeper(root_dir=Path.cwd())
    
    # 2. Scan for code files
    files = keeper.scan(recursive=True)
    print(f"📁 Scanned {len(files)} files")
    
    # 3. Add copyright headers
    results = keeper.add_copyright_headers(
        recursive=True,
        license_type="MIT",
        author="Your Name",
        year_range="2023-2025",
        overwrite_mode=OverwriteMode.UPDATE_YEAR
    )
    print(f"📝 Updated copyright in {len(results)} files")
    
    # 4. Preview junk files
    junk_files, stats = keeper.preview_junk_files(recursive=True)
    print(f"🗑️ Found {len(junk_files)} junk files ({stats.total_size_mb:.2f} MB)")
    
    # 5. Check annotation coverage
    summary = keeper.annotation_summary(recursive=True)
    print(f"📊 Annotation coverage: {summary['annotation_coverage_percent']:.1f}%")

if __name__ == "__main__":
    main()
```

**Next Steps:**

- 📖 [User Guide](USER_GUIDE.md)
- 💻 [More Examples](../examples/)

</details>

<details>
<summary><b>❓ What license types are supported?</b></summary>

<br>

<div align="center">

### 📄 Supported License Types

</div>

**Copyright Header Licenses:**

- ✅ MIT
- ✅ Apache-2.0
- ✅ GPL-3.0
- ✅ BSD-3-Clause
- ✅ Proprietary

**Usage Example:**

```python
from codekeeper import CodeKeeper
from pathlib import Path

keeper = CodeKeeper(root_dir=Path.cwd())

# Add MIT license headers
results = keeper.add_copyright_headers(
    recursive=True,
    license_type="MIT",
    author="Your Name",
    year_range="2023-2025"
)

# Add Apache-2.0 license headers
results = keeper.add_copyright_headers(
    recursive=True,
    license_type="Apache-2.0",
    author="Your Name"
)
```

**See also:** [Copyright Management](USER_GUIDE.md#-copyright-manager)

</details>

<details>
<summary><b>❓ How do junk file patterns work?</b></summary>

<br>

**CodeKeeper includes built-in junk patterns:**

- `__pycache__/` - Python cache directories
- `*.pyc` - Python compiled files
- `*.pyo` - Python optimized files
- `node_modules/` - Node.js dependencies
- `.git/` - Git repository data
- `dist/` - Distribution directories
- `build/` - Build directories
- `*.egg-info/` - Python egg info

**Custom Patterns:**

```python
from codekeeper import CodeKeeper
from pathlib import Path

keeper = CodeKeeper(root_dir=Path.cwd())

# Register custom pattern
keeper.register_junk_pattern(
    pattern=r"\.tmp$",
    name="temporary_files",
    description="Temporary files with .tmp extension"
)

# Preview before cleaning
junk_files, stats = keeper.preview_junk_files(recursive=True)
print(f"Found {len(junk_files)} junk files")

# Clean (with confirmation)
results, stats = keeper.clean_junk_files(
    paths=[Path.cwd()],
    recursive=True,
    confirm=True  # Set to False for preview only
)
```

**Benefits:**

- 🔒 Safe preview mode before deletion
- 📊 Size tracking and reporting
- 🎯 Custom pattern support via regex
- ✅ Confirmation prompts for safety

</details>

<details>
<summary><b>❓ How do I handle errors properly?</b></summary>

<br>

**Recommended Pattern:**

```python
from pathlib import Path
from codekeeper import CodeKeeper
from codekeeper.security import InvalidPathError

def safe_scan():
    try:
        keeper = CodeKeeper(root_dir=Path.cwd())
        files = keeper.scan(recursive=True)
        print(f"✅ Scanned {len(files)} files")
        return files
    except InvalidPathError as e:
        print(f"⚠️ Invalid path: {e}")
        # Handle invalid path - maybe create directory first
        return []
    except PermissionError as e:
        print(f"❌ Permission denied: {e}")
        # Handle permission issues
        return []
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        raise

# Or use conditional checks
def safe_scan():
    keeper = CodeKeeper(root_dir=Path.cwd())
    
    if not keeper.root_dir.exists():
        print(f"⚠️ Directory does not exist: {keeper.root_dir}")
        return []
    
    if not keeper.root_dir.is_dir():
        print(f"⚠️ Not a directory: {keeper.root_dir}")
        return []
    
    return keeper.scan(recursive=True)
```

**Error Types:**

- `InvalidPathError` - Invalid or unsafe path provided
- `PermissionError` - Permission denied accessing files
- `FileNotFoundError` - File or directory not found

</details>

<details>
<summary><b>❓ Does CodeKeeper support APM monitoring?</b></summary>

<br>

**Yes!** CodeKeeper supports multiple APM vendors:

```python
from codekeeper import CodeKeeper
from pathlib import Path

# Enable APM with custom vendor
keeper = CodeKeeper(
    root_dir=Path.cwd(),
    apm_enabled=True,
    apm_vendor="prometheus"  # datadog, prometheus, opentelemetry, custom
)

# Initialize with custom config
keeper.initialize_apm({
    "endpoint": "http://apm.example.com",
    "api_key": "your-api-key",
    "service_name": "my-codekeeper"
})

# Perform operations
keeper.scan(recursive=True)
keeper.add_copyright_headers(recursive=True)

# Get performance report
report = keeper.get_apm_report()
print(f"APM Report: {report}")

# Get performance summary
summary = keeper.get_performance_summary()
print(f"Performance: {summary}")

# Flush APM data
keeper.flush_apm()
```

**Supported Vendors:**

- 📊 **Datadog** - Full APM integration
- 📊 **Prometheus** - Metrics export
- 📊 **OpenTelemetry** - Vendor-neutral tracing
- 📊 **Custom** - Simple custom reporter

</details>

---

## Performance

<div align="center">

### ⚡ Speed and Optimization

</div>

<details>
<summary><b>❓ How fast is it?</b></summary>

<br>

**Performance Characteristics:**

<table>
<tr>
<th>Operation</th>
<th>Throughput</th>
<th>Notes</th>
</tr>
<tr>
<td>File Scanning</td>
<td>1000+ files/second</td>
<td>Depends on file system</td>
</tr>
<tr>
<td>Copyright Headers</td>
<td>500+ files/second</td>
<td>With default settings</td>
</tr>
<tr>
<td>Junk File Preview</td>
<td>2000+ files/second</td>
<td>Pattern matching speed</td>
</tr>
<tr>
<td>Annotation Scanning</td>
<td>100+ files/second</td>
<td>Python file parsing</td>
</tr>
</table>

**Factors Affecting Performance:**

- File system speed (SSD vs HDD)
- Number of files in project
- Depth of directory structure
- Custom pattern complexity

**Optimization Tips:**

1. **Increase worker threads:**
   ```python
   from codekeeper.infra.config import CodeKeeperConfig
   
   config = CodeKeeperConfig(max_workers=8)
   ```

2. **Use appropriate scan depth:**
   ```python
   # Only scan top-level for quick checks
   files = keeper.scan(recursive=False)
   
   # Full scan for comprehensive analysis
   files = keeper.scan(recursive=True)
   ```

3. **Limit file types:**
   ```python
   results = keeper.add_copyright_headers(
       recursive=True,
       extensions=["py", "rs"]  # Only specific languages
   )
   ```

</details>

<details>
<summary><b>❓ How can I improve performance?</b></summary>

<br>

**Optimization Tips:**

1. **Use Recursive Flag Appropriately:**
   ```python
   # ❌ Inefficient - multiple separate scans
   for dir in dirs:
       files = keeper.scan_directory(dir)
   
   # ✅ Efficient - single recursive scan
   files = keeper.scan(recursive=True)
   ```

2. **Batch Operations:**
   ```python
   # ❌ Inefficient - process one by one
   for file in files:
       result = keeper.add_copyright_header(file)
   
   # ✅ Efficient - batch processing
   results = keeper.add_copyright_headers(
       recursive=True,
       extensions=["py"]
   )
   ```

3. **Configure Thread Pool:**
   ```python
   from codekeeper.infra.config import CodeKeeperConfig
   
   config = CodeKeeperConfig(max_workers=8)
   keeper = CodeKeeper(
       root_dir=Path.cwd(),
       config_path=Path("codekeeper.json")
   )
   ```

4. **Limit Scope:**
   ```python
   # Only scan specific paths
   junk_files, stats = keeper.preview_junk_files(
       paths=[Path("/specific/dir")],
       recursive=True
   )
   
   # Only process specific extensions
   results = keeper.add_copyright_headers(
       recursive=True,
       extensions=["py", "js"]  # Limit to certain file types
   )
   ```

**More tips:** [Performance Guide](USER_GUIDE.md#performance-tuning)

</details>

<details>
<summary><b>❓ What's the memory usage like?</b></summary>

<br>

**Typical Memory Usage:**

<table>
<tr>
<th>Scenario</th>
<th>Memory Usage</th>
<th>Notes</th>
</tr>
<tr>
<td>Basic initialization</td>
<td>~20 MB</td>
<td>Minimum overhead</td>
</tr>
<tr>
<td>Scanning 10K files</td>
<td>~50 MB</td>
<td>File list in memory</td>
</tr>
<tr>
<td>With cache (100 MB)</td>
<td>~120 MB</td>
<td>Configurable</td>
</tr>
<tr>
<td>High-throughput mode</td>
<td>~100 MB</td>
<td>With APM enabled</td>
</tr>
</table>

**Memory Characteristics:**

- Linear memory growth with file count
- Automatic cleanup after operations
- No persistent memory leaks
- Configurable cache size

**Reduce Memory Usage:**

```python
from codekeeper.infra.config import CodeKeeperConfig

# Reduce cache directory size
config = CodeKeeperConfig(
    cache_dir=Path("/tmp/codekeeper"),
    max_workers=2  # Fewer workers = less memory
)
```

**Memory Safety:**

- ✅ Automatic cleanup with Python garbage collection
- ✅ No memory leaks (verified with memory profiling)
- ✅ Context managers for resource management

</details>

---

## Security

<div align="center">

### 🔒 Security Features

</div>

<details>
<summary><b>❓ Is CodeKeeper secure?</b></summary>

<br>

**Yes!** Security is a design consideration.

**Security Features:**

<table>
<tr>
<td width="50%">

**Implementation**

- ✅ Python with type safety (Pydantic)
- ✅ Input validation on all paths
- ✅ Path traversal protection
- ✅ Secure file operations

</td>
<td width="50%">

**Protections**

- ✅ Path validation to prevent traversal
- ✅ Permission-aware file operations
- ✅ No arbitrary code execution
- ✅ Read operations are safe by default

</td>
</tr>
</table>

**Safety Measures:**

- All paths are validated before use
- Confirmation prompts for destructive operations
- Preview modes for dangerous operations
- Configurable ignore patterns for sensitive directories

**More details:** [Security Considerations](#security)

</details>

<details>
<summary><b>❓ How do I report security vulnerabilities?</b></summary>

<br>

**Please report security issues responsibly:**

1. **DO NOT** create public GitHub issues
2. **Email:** security@example.com
3. **Include:**
    - Description of the vulnerability
    - Steps to reproduce
    - Potential impact
    - Suggested fix (if any)

**Response Timeline:**

- 📧 Initial response: 24 hours
- 🔍 Assessment: 72 hours
- 🔧 Fix (if valid): 7-30 days
- 📢 Public disclosure: After fix released

**Security Policy:** [SECURITY.md](../SECURITY.md)

</details>

<details>
<summary><b>❓ What about path safety?</b></summary>

<br>

**CodeKeeper includes path validation:**

```python
from codekeeper import CodeKeeper
from codekeeper.security import is_safe_path, InvalidPathError
from pathlib import Path

# Automatic validation
keeper = CodeKeeper(root_dir=Path.cwd())

# Check path safety manually
def safe_operation(user_path: str):
    path = Path(user_path)
    
    # Validate path
    if not is_safe_path(path, keeper.root_dir):
        raise InvalidPathError(f"Unsafe path: {user_path}")
    
    # Safe to use
    return keeper.scan_directory(path)
```

**Path Safety Rules:**

- Paths must be under root directory
- No symbolic link traversal
- No path traversal attacks (`../../../etc/passwd`)
- Permission checks where applicable

</details>

<details>
<summary><b>❓ Are there any known security issues?</b></summary>

<br>

**Current Status:** ✅ **No known security vulnerabilities**

**How we maintain security:**

1. **Input Validation:**
   - All paths validated before use
   - Path traversal protection
   - Type checking with Pydantic

2. **Safe Operations:**
   - Read-only operations are default
   - Confirmation for destructive operations
   - Preview modes for dangerous tasks

3. **Dependencies:**
   - Regular dependency updates
   - Security patches within 48 hours
   - Minimal external dependencies

**Stay Informed:**

- 🔔 Watch this repository
- 📰 Check release notes for security updates

</details>

---

## Troubleshooting

<div align="center">

### 🔧 Common Issues

</div>

<details>
<summary><b>❓ I'm getting "InvalidPathError"</b></summary>

<br>

**Problem:**

```
InvalidPathError: Invalid or unsafe file path: /path/to/file
```

**Cause:** Path validation failed.

**Solutions:**

1. **Check if path is under root directory:**
   ```python
   keeper = CodeKeeper(root_dir=Path("/project"))
   
   # This will work
   files = keeper.scan()  # Scans /project
   
   # This will raise InvalidPathError
   files = keeper.scan_directory(Path("/other/project"))
   ```

2. **Use absolute paths:**
   ```python
   from pathlib import Path
   
   # ✅ Correct
   keeper = CodeKeeper(root_dir=Path("/project").resolve())
   
   # ❌ May cause issues
   keeper = CodeKeeper(root_dir=Path("relative/path"))
   ```

3. **Validate path manually:**
   ```python
   from codekeeper.security import is_safe_path
   
   path = Path("/some/path")
   if is_safe_path(path, keeper.root_dir):
       # Safe to use
       pass
   else:
       print("⚠️ Unsafe path detected")
   ```

</details>

<details>
<summary><b>❓ Junk files are not being detected</b></summary>

<br>

**Problem:** Expected junk files are not appearing in results.

**Solutions:**

1. **Check built-in patterns:**
   ```python
   from codekeeper import CodeKeeper
   from pathlib import Path
   
   keeper = CodeKeeper(root_dir=Path.cwd())
   
   # Preview all junk files
   junk_files, stats = keeper.preview_junk_files(recursive=True)
   print(f"Found {len(junk_files)} junk files")
   ```

2. **Register custom pattern:**
   ```python
   # Add pattern for .log files
   keeper.register_junk_pattern(
       pattern=r"\.log$",
       name="log_files",
       description="Log files with .log extension"
   )
   
   # Preview again
   junk_files, stats = keeper.preview_junk_files(recursive=True)
   ```

3. **Check ignore patterns:**
   ```python
   from codekeeper.infra.config import CodeKeeperConfig
   
   config = CodeKeeperConfig(
       ignore_patterns=[
           "__pycache__",
           ".git",
           "node_modules",
       ]
   )
   ```

4. **Verify directory:**
   ```python
   # Make sure you're scanning the right directory
   keeper = CodeKeeper(root_dir=Path("/your/project"))
   ```

</details>

<details>
<summary><b>❓ Copyright headers not being added</b></summary>

<br>

**Problem:** Copyright headers are not being added to files.

**Solutions:**

1. **Check file extensions:**
   ```python
   # Only specified extensions get headers
   results = keeper.add_copyright_headers(
       recursive=True,
       extensions=["py", "rs", "java"]  # Only these types
   )
   ```

2. **Check overwrite mode:**
   ```python
   from codekeeper.core.copyright import OverwriteMode
   
   # UPDATE_YEAR - only update existing headers
   # SKIP - skip files with existing headers
   # OVERWRITE - replace existing headers
   
   results = keeper.add_copyright_headers(
       recursive=True,
       overwrite_mode=OverwriteMode.OVERWRITE  # Force update
   )
   ```

3. **Check skip_if_exists:**
   ```python
   # Set to False to process all files
   results = keeper.add_copyright_headers(
       recursive=True,
       skip_if_exists=False  # Process even with existing headers
   )
   ```

4. **Validate files:**
   ```python
   # Check existing headers
   validation = keeper.validate_copyright_headers(recursive=True)
   for result in validation:
       print(f"{result.file_path}: {result.status}")
   ```

</details>

<details>
<summary><b>❓ Annotation scanning shows no results</b></summary>

<br>

**Problem:** Annotation scanning returns no functions.

**Solutions:**

1. **Check file type:**
   ```python
   # Annotation scanning currently focuses on Python
   results = keeper.scan_function_annotations(
       recursive=True,
       extensions=["py"]  # Only Python files
   )
   ```

2. **Check private/dunder settings:**
   ```python
   # Include private functions
   results = keeper.scan_function_annotations(
       recursive=True,
       skip_private=False,  # Include _private functions
       skip_dunder=False    # Include __dunder__ methods
   )
   ```

3. **Get missing annotations directly:**
   ```python
   # Get list of functions missing comments
   missing = keeper.get_missing_annotations(recursive=True)
   for func in missing[:10]:  # Show first 10
       print(f"  - {func.file_path}:{func.line_number} {func.name}")
   ```

4. **Check summary:**
   ```python
   # Get coverage summary
   summary = keeper.annotation_summary(recursive=True)
   print(f"Coverage: {summary['annotation_coverage_percent']:.1f}%")
   print(f"Total Functions: {summary['total_functions']}")
   print(f"Missing Comments: {summary['functions_without_comments']}")
   ```

</details>

<details>
<summary><b>❓ Performance is slower than expected</b></summary>

<br>

**Checklist:**

- [ ] Are you using recursive scanning efficiently?
  ```python
  # ❌ Multiple separate scans
  for subdir in subdirs:
      files.extend(keeper.scan_directory(subdir))
  
  # ✅ Single recursive scan
  files = keeper.scan(recursive=True)
  ```

- [ ] Have you configured thread pool size?
  ```python
  from codekeeper.infra.config import CodeKeeperConfig
  
  config = CodeKeeperConfig(max_workers=8)
  ```

- [ ] Are you limiting file types?
  ```python
  # Only scan relevant files
  results = keeper.add_copyright_headers(
      recursive=True,
      extensions=["py", "rs"]  # Limit scope
  )
  ```

- [ ] Is APM affecting performance?
  ```python
  # Disable APM for faster execution
  keeper = CodeKeeper(
      root_dir=Path.cwd(),
      apm_enabled=False
  )
  ```

**Profiling:**

```python
# Get performance metrics
summary = keeper.get_performance_summary()
print(f"Operations: {summary}")

# Check which operations are slow
# APM report will show detailed timing
```

**More help:** [Performance Guide](#performance)

</details>

**More issues?** Check [User Guide](USER_GUIDE.md#troubleshooting)

---

## Contributing

<div align="center">

### 🤝 Join the Community

</div>

<details>
<summary><b>❓ How can I contribute?</b></summary>

<br>

**Ways to Contribute:**

<table>
<tr>
<td width="50%">

**Code Contributions**

- 🐛 Fix bugs
- ✨ Add features
- 📝 Improve documentation
- ✅ Write tests

</td>
<td width="50%">

**Non-Code Contributions**

- 📖 Write tutorials
- 🎨 Design assets
- 🌍 Translate docs
- 💬 Answer questions

</td>
</tr>
</table>

**Getting Started:**

1. 🍴 Fork the repository
2. 🌱 Create a branch
3. ✏️ Make changes
4. ✅ Add tests
5. 📤 Submit PR

**Guidelines:** [CONTRIBUTING.md](../CONTRIBUTING.md)

</details>

<details>
<summary><b>❓ I found a bug, what should I do?</b></summary>

<br>

**Before Reporting:**

1. ✅ Check [existing issues](../../issues)
2. ✅ Try the latest version
3. ✅ Check documentation and FAQ

**Creating a Good Bug Report:**

```markdown
### Description
Clear description of the bug

### Steps to Reproduce
1. Step one
2. Step two
3. See error

### Expected Behavior
What should happen

### Actual Behavior
What actually happens

### Environment
- OS: Ubuntu 22.04
- Python version: 3.11.0
- CodeKeeper version: 1.0.0

### Additional Context
Any other relevant information
```

**Submit:** [Create Issue](../../issues/new)

</details>

<details>
<summary><b>❓ Where can I get help?</b></summary>

<br>

<div align="center">

### 💬 Support Channels

</div>

<table>
<tr>
<td width="50%" align="center">

**🐛 Issues**

[GitHub Issues](../../issues)

Bug reports & feature requests

</td>
<td width="50%" align="center">

**💬 Discussions**

[GitHub Discussions](../../discussions)

Q&A and ideas

</td>
</tr>
</table>

**Response Times:**

- 🐛 Critical bugs: 24 hours
- 🔧 Feature requests: 1 week
- 💬 Questions: 2-3 days

</details>

---

## Licensing

<div align="center">

### 📄 License Information

</div>

<details>
<summary><b>❓ What license is CodeKeeper under?</b></summary>

<br>

**License:** MIT License

**Key Points:**

- ✅ Free to use commercially
- ✅ Can modify and distribute
- ✅ Private use allowed
- ✅ No warranty provided

**Usage in CodeKeeper:**

When adding copyright headers to your project files, CodeKeeper supports multiple license types including MIT, Apache-2.0, GPL-3.0, BSD-3-Clause, and proprietary licenses.

**Full License Text:** [LICENSE](../LICENSE)

</details>

<details>
<summary><b>❓ Can I use CodeKeeper commercially?</b></summary>

<br>

**Yes!** CodeKeeper is licensed under the MIT License, which permits:

- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

**No Restrictions On:**

- Using CodeKeeper in proprietary software
- Distributing CodeKeeper with your products
- Modifying CodeKeeper for your needs

**Only Requirement:** Include the original copyright notice and license text when distributing CodeKeeper itself.

</details>

---

<div align="center">

### Still have questions?

**Check the [User Guide](USER_GUIDE.md) or [open an issue](../../issues/new).**

---

*Last updated: 2024*
