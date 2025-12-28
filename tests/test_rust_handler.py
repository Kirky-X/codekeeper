"""Tests for Rust language handler."""

from codekeeper.languages import RustHandler


class TestRustHandler:
    """Tests for RustHandler class."""

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

    def test_get_functions(self, sample_rust_code):
        """Test parsing Rust functions."""
        handler = RustHandler(sample_rust_code)
        functions = handler.get_functions()

        function_names = [f.name for f in functions]
        assert "new" in function_names
        assert "add" in function_names

    def test_get_classes(self, sample_rust_code):
        """Test parsing Rust structs."""
        handler = RustHandler(sample_rust_code)
        classes = handler.get_classes()

        class_names = [c.name for c in classes]
        assert "Calculator" in class_names

    def test_get_copyright_header(self, sample_rust_code):
        """Test copyright header detection."""
        handler = RustHandler(sample_rust_code)
        header = handler.get_copyright_header()

        assert header is not None

    def test_get_comment_style(self):
        """Test comment style detection."""
        handler = RustHandler("")
        assert handler.get_comment_style().value == "single_line"

    def test_get_supported_extensions(self):
        """Test supported extensions."""
        assert ".rs" in RustHandler.SUPPORTED_EXTENSIONS

    def test_struct_methods(self, temp_rust_file):
        """Test parsing struct and impl methods."""
        handler = RustHandler.from_file(temp_rust_file)
        handler.get_functions()
        classes = handler.get_classes()

        assert len(classes) >= 1
        assert any(c.name == "Calculator" for c in classes)
