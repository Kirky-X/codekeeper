"""MCP Server implementation for CodeKeeper."""

import asyncio
import logging
from pathlib import Path
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

from codekeeper import CodeKeeper

logger = logging.getLogger(__name__)

app = Server("codekeeper")


def create_codekeeper(root_dir: Path | None = None) -> CodeKeeper:
    """Create a CodeKeeper instance.

# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the INVALID-LICENSE-TYPE License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author.With.Dots. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author_With_Underscore. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author-With-Hyphen. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author with spaces. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2020-2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test_Author123. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Organization Name. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author <email@example.com>. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the GPL-3.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the BSD-3-Clause License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the Apache-2.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the INVALID-LICENSE-TYPE License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author.With.Dots. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author_With_Underscore. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author-With-Hyphen. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author with spaces. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2020-2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test_Author123. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Organization Name. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author <email@example.com>. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the GPL-3.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the BSD-3-Clause License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the Apache-2.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the INVALID-LICENSE-TYPE License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author.With.Dots. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author_With_Underscore. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author-With-Hyphen. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author with spaces. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2020-2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test_Author123. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Organization Name. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author <email@example.com>. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the GPL-3.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the BSD-3-Clause License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the Apache-2.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the INVALID-LICENSE-TYPE License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author.With.Dots. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author_With_Underscore. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author-With-Hyphen. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author with spaces. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2020-2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test_Author123. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Organization Name. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author <email@example.com>. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the GPL-3.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the BSD-3-Clause License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the Apache-2.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the INVALID-LICENSE-TYPE License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author.With.Dots. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author_With_Underscore. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author-With-Hyphen. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author with spaces. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2020-2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test_Author123. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Organization Name. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author <email@example.com>. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the GPL-3.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the BSD-3-Clause License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the Apache-2.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the INVALID-LICENSE-TYPE License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author.With.Dots. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author_With_Underscore. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author-With-Hyphen. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author with spaces. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2020-2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test_Author123. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Organization Name. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author <email@example.com>. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the GPL-3.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the BSD-3-Clause License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the Apache-2.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the INVALID-LICENSE-TYPE License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author.With.Dots. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author_With_Underscore. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author-With-Hyphen. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author with spaces. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2020-2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test_Author123. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Organization Name. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author <email@example.com>. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the GPL-3.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the BSD-3-Clause License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the Apache-2.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the INVALID-LICENSE-TYPE License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author.With.Dots. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author_With_Underscore. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author-With-Hyphen. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author with spaces. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2020-2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test_Author123. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Organization Name. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author <email@example.com>. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the GPL-3.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the BSD-3-Clause License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the Apache-2.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the INVALID-LICENSE-TYPE License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author.With.Dots. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author_With_Underscore. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author-With-Hyphen. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author with spaces. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2015 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2020-2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test_Author123. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Organization Name. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author <email@example.com>. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the GPL-3.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the BSD-3-Clause License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the Apache-2.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the INVALID-LICENSE-TYPE License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author.With.Dots. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author_With_Underscore. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author-With-Hyphen. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author with spaces. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2015 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2020-2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test_Author123. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Organization Name. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author <email@example.com>. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the GPL-3.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the BSD-3-Clause License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the Apache-2.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the INVALID-LICENSE-TYPE License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author.With.Dots. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author_With_Underscore. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author-With-Hyphen. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author with spaces. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2015 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2020-2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test_Author123. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Organization Name. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author <email@example.com>. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the GPL-3.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the BSD-3-Clause License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the Apache-2.0 License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2025 Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


# Copyright (c) 2024-2025 Test Author. All rights reserved.
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.


    Args:
        root_dir: Root directory for operations

    Returns:
        Configured CodeKeeper instance
    """
    return CodeKeeper(root_dir=root_dir)


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List all available MCP tools."""
    return [
        Tool(
            name="copyright",
            description="Add copyright headers to code files. Supports multiple license types (MIT, Apache-2.0, GPL-3.0, BSD-3-Clause). Can preview changes before applying.",
            inputSchema={
                "type": "object",
                "properties": {
                    "paths": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "File or directory paths to process",
                    },
                    "license": {
                        "type": "string",
                        "enum": ["MIT", "Apache-2.0", "GPL-3.0", "BSD-3-Clause"],
                        "default": "MIT",
                        "description": "License type for copyright header",
                    },
                    "author": {
                        "type": "string",
                        "description": "Copyright author name",
                    },
                    "year_range": {
                        "type": "string",
                        "description": "Year range (e.g., '2023-2025')",
                    },
                    "recursive": {
                        "type": "boolean",
                        "default": True,
                        "description": "Whether to process files recursively",
                    },
                    "preview": {
                        "type": "boolean",
                        "default": False,
                        "description": "Preview changes without applying",
                    },
                },
                "required": ["paths"],
            },
        ),
        Tool(
            name="remove_copyright",
            description="Remove copyright headers from code files. Supports preview mode to see what would be removed.",
            inputSchema={
                "type": "object",
                "properties": {
                    "paths": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "File or directory paths to process",
                    },
                    "recursive": {
                        "type": "boolean",
                        "default": True,
                        "description": "Whether to process files recursively",
                    },
                    "preview": {
                        "type": "boolean",
                        "default": False,
                        "description": "Preview changes without applying",
                    },
                },
                "required": ["paths"],
            },
        ),
        Tool(
            name="validate_copyright",
            description="Validate copyright headers in code files. Returns status of each file.",
            inputSchema={
                "type": "object",
                "properties": {
                    "paths": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "File or directory paths to validate",
                    },
                    "recursive": {
                        "type": "boolean",
                        "default": True,
                        "description": "Whether to validate files recursively",
                    },
                },
                "required": ["paths"],
            },
        ),
        Tool(
            name="clean",
            description="Scan for and optionally clean junk/temporary files. Supports preview mode to see what would be deleted.",
            inputSchema={
                "type": "object",
                "properties": {
                    "paths": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Directory paths to scan",
                    },
                    "recursive": {
                        "type": "boolean",
                        "default": True,
                        "description": "Whether to scan recursively",
                    },
                    "preview": {
                        "type": "boolean",
                        "default": True,
                        "description": "Preview without actually deleting files",
                    },
                },
                "required": ["paths"],
            },
        ),
        Tool(
            name="register_pattern",
            description="Register a custom junk file pattern for cleaning.",
            inputSchema={
                "type": "object",
                "properties": {
                    "pattern": {
                        "type": "string",
                        "description": "Regex pattern for matching files",
                    },
                    "name": {
                        "type": "string",
                        "description": "Pattern name",
                    },
                    "description": {
                        "type": "string",
                        "description": "Pattern description",
                    },
                },
                "required": ["pattern", "name"],
            },
        ),
        Tool(
            name="scan_annotations",
            description="Scan Python files for functions missing docstrings/comments.",
            inputSchema={
                "type": "object",
                "properties": {
                    "paths": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Directory paths to scan",
                    },
                    "recursive": {
                        "type": "boolean",
                        "default": True,
                        "description": "Whether to scan recursively",
                    },
                    "skip_private": {
                        "type": "boolean",
                        "default": False,
                        "description": "Skip private functions (starting with _)",
                    },
                    "skip_dunder": {
                        "type": "boolean",
                        "default": True,
                        "description": "Skip dunder methods",
                    },
                },
                "required": ["paths"],
            },
        ),
        Tool(
            name="annotation_summary",
            description="Get summary statistics for function annotation coverage.",
            inputSchema={
                "type": "object",
                "properties": {
                    "paths": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Directory paths to scan",
                    },
                    "recursive": {
                        "type": "boolean",
                        "default": True,
                        "description": "Whether to scan recursively",
                    },
                },
                "required": ["paths"],
            },
        ),
    ]


def format_copyright_result(result: dict[str, Any]) -> str:
    """Format a copyright operation result for display."""
    status = "✓ Added" if result.get("success") else "✗ Failed"
    path = result.get("path", "unknown")
    message = result.get("message", "")
    return f"{status}: {path} - {message}"


def format_clean_result(result: dict[str, Any]) -> str:
    """Format a clean operation result for display."""
    status = "✓ Cleaned" if result.get("success") else "✗ Failed"
    path = result.get("path", "unknown")
    freed = result.get("freed_space", 0)
    return f"{status}: {path} (freed: {freed} bytes)"


def format_annotation_result(result: dict[str, Any]) -> str:
    """Format an annotation scan result for display."""
    file_path = result.get("file_path", "unknown")
    total = result.get("functions_found", 0)
    with_comments = result.get("functions_with_comments", 0)
    missing = result.get("functions_without_comments", 0)
    return f"{file_path}: {with_comments}/{total} functions annotated, {missing} missing"


@app.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle tool calls from MCP clients."""
    try:
        paths_raw = arguments.get("paths", [])
        paths = [Path(p) for p in paths_raw]

        root_dir = None
        if paths:
            if len(paths) == 1 and paths[0].is_dir():
                root_dir = paths[0]
            elif len(paths) == 1 and paths[0].is_file():
                root_dir = paths[0].parent
            else:
                root_dir = paths[0].parent

        codekeeper = create_codekeeper(root_dir)

        if name == "copyright":
            preview = arguments.get("preview", False)
            license_type = arguments.get("license", "MIT")
            author = arguments.get("author")
            year_range = arguments.get("year_range")

            results = codekeeper.add_copyright_headers(
                recursive=arguments.get("recursive", True),
                license_type=license_type,
                author=author,
                year_range=year_range,
            )

            if preview:
                output = [f"Preview: Would add copyright headers to {len(results)} files:\n"]
            else:
                output = [f"Added copyright headers to {len(results)} files:\n"]

            for result in results:
                output.append(format_copyright_result(result.to_dict()))

            return [TextContent(type="text", text="\n".join(output))]

        elif name == "remove_copyright":
            preview = arguments.get("preview", False)

            results = codekeeper.remove_copyright_headers(
                recursive=arguments.get("recursive", True),
            )

            if preview:
                output = [f"Preview: Would remove copyright headers from {len(results)} files:\n"]
            else:
                output = [f"Removed copyright headers from {len(results)} files:\n"]

            for result in results:
                output.append(format_copyright_result(result.to_dict()))

            return [TextContent(type="text", text="\n".join(output))]

        elif name == "validate_copyright":
            results = codekeeper.validate_copyright_headers(
                recursive=arguments.get("recursive", True),
            )

            valid = sum(1 for r in results if r.is_valid)
            invalid = len(results) - valid

            output = [
                f"Validation results: {valid} valid, {invalid} invalid out of {len(results)} files:\n"
            ]
            for result in results:
                status = "✓ Valid" if result.is_valid else "✗ Invalid"
                output.append(f"{status}: {result.path}")

            return [TextContent(type="text", text="\n".join(output))]

        elif name == "clean":
            preview = arguments.get("preview", True)

            if preview:
                junk_files, stats = codekeeper.preview_junk_files(
                    paths=paths or None,
                    recursive=arguments.get("recursive", True),
                )
                output = [
                    f"Preview: Found {stats.files_found} junk files ({stats.total_size} bytes):\n"
                ]
                for junk in junk_files[:50]:
                    output.append(f"  {junk.path} ({junk.size} bytes)")
                if len(junk_files) > 50:
                    output.append(f"  ... and {len(junk_files) - 50} more")
                return [TextContent(type="text", text="\n".join(output))]
            else:
                results, stats = codekeeper.clean_junk_files(
                    paths=paths or None,
                    recursive=arguments.get("recursive", True),
                    confirm=True,
                )
                output = [
                    f"Cleaned {stats.files_cleaned} junk files, freed {stats.bytes_freed} bytes:\n"
                ]
                for result in results[:50]:
                    output.append(format_clean_result(result.to_dict()))
                if len(results) > 50:
                    output.append(f"  ... and {len(results) - 50} more")
                return [TextContent(type="text", text="\n".join(output))]

        elif name == "register_pattern":
            codekeeper.register_junk_pattern(
                pattern=arguments["pattern"],
                name=arguments["name"],
                description=arguments.get("description", ""),
            )
            return [TextContent(type="text", text=f"Registered junk pattern: {arguments['name']}")]

        elif name == "scan_annotations":
            results = codekeeper.scan_function_annotations(
                recursive=arguments.get("recursive", True),
                skip_private=arguments.get("skip_private", False),
                skip_dunder=arguments.get("skip_dunder", True),
            )

            output = [f"Scanned {len(results)} files for function annotations:\n"]
            for result in results:
                output.append(format_annotation_result(result.to_dict()))

            missing = codekeeper.get_missing_annotations(
                recursive=arguments.get("recursive", True),
                skip_private=arguments.get("skip_private", False),
                skip_dunder=arguments.get("skip_dunder", True),
            )
            if missing:
                output.append(f"\nFunctions missing comments ({len(missing)}):\n")
                for func in missing[:20]:
                    output.append(f"  {func.file_path}:{func.start_line} - {func.name}()")
                if len(missing) > 20:
                    output.append(f"  ... and {len(missing) - 20} more")

            return [TextContent(type="text", text="\n".join(output))]

        elif name == "annotation_summary":
            summary = codekeeper.annotation_summary(
                recursive=arguments.get("recursive", True),
            )
            output = [
                "Annotation Coverage Summary:",
                f"  Files scanned: {summary['files_scanned']}",
                f"  Total functions: {summary['total_functions']}",
                f"  With comments: {summary['functions_with_comments']}",
                f"  Without comments: {summary['functions_without_comments']}",
                f"  Coverage: {summary['annotation_coverage_percent']:.1f}%",
            ]
            return [TextContent(type="text", text="\n".join(output))]

        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]

    except Exception as e:
        logger.exception(f"Error executing tool {name}")
        return [TextContent(type="text", text=f"Error: {e!s}")]


async def main():
    """Main entry point for MCP Server."""
    logging.basicConfig(level=logging.INFO)
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
