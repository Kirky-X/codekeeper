"""Tests for C++ language handler."""

from codekeeper.languages import CppHandler


class TestCppHandler:
    """Tests for CppHandler class."""

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

    def test_get_functions(self, sample_cpp_code):
        """Test parsing C++ functions."""
        handler = CppHandler(sample_cpp_code)
        functions = handler.get_functions()

        function_names = [f.name for f in functions]
        assert "standaloneFunction" in function_names
        assert "maxValue" in function_names

    def test_get_classes(self, sample_cpp_code):
        """Test parsing C++ classes."""
        handler = CppHandler(sample_cpp_code)
        classes = handler.get_classes()

        class_names = [c.name for c in classes]
        assert "Calculator" in class_names

    def test_get_structs(self, sample_cpp_code):
        """Test parsing C++ structs."""
        handler = CppHandler(sample_cpp_code)
        classes = handler.get_classes()

        struct_names = [c.name for c in classes if "struct" in c.decorators]
        assert "Point" in struct_names

    def test_get_namespaces(self, sample_cpp_code):
        """Test parsing C++ namespaces."""
        handler = CppHandler(sample_cpp_code)
        classes = handler.get_classes()

        namespace_names = [c.name for c in classes if "namespace" in c.decorators]
        assert "MathUtils" in namespace_names

    def test_get_copyright_header(self, sample_cpp_code):
        """Test copyright header detection."""
        handler = CppHandler(sample_cpp_code)
        header = handler.get_copyright_header()

        assert header is not None

    def test_get_comment_style(self):
        """Test comment style detection."""
        handler = CppHandler("")
        assert handler.get_comment_style().value == "single_line"

    def test_get_supported_extensions(self):
        """Test supported extensions."""
        assert ".cpp" in CppHandler.SUPPORTED_EXTENSIONS
        assert ".cc" in CppHandler.SUPPORTED_EXTENSIONS
        assert ".cxx" in CppHandler.SUPPORTED_EXTENSIONS
        assert ".h" in CppHandler.SUPPORTED_EXTENSIONS
        assert ".hpp" in CppHandler.SUPPORTED_EXTENSIONS
        assert ".hh" in CppHandler.SUPPORTED_EXTENSIONS
        assert ".hxx" in CppHandler.SUPPORTED_EXTENSIONS

    def test_class_methods(self, temp_cpp_file):
        """Test parsing class methods."""
        handler = CppHandler.from_file(temp_cpp_file)
        classes = handler.get_classes()

        assert len(classes) >= 1
        calculator_class = next((c for c in classes if c.name == "Calculator"), None)
        assert calculator_class is not None
        method_names = [m.name for m in calculator_class.methods]
        assert "add" in method_names
        assert "subtract" in method_names
        assert "getValue" in method_names

    def test_static_method(self, sample_cpp_code):
        """Test parsing static methods."""
        handler = CppHandler(sample_cpp_code)
        classes = handler.get_classes()

        calculator_class = next((c for c in classes if c.name == "Calculator"), None)
        assert calculator_class is not None
        static_methods = [m for m in calculator_class.methods]
        assert any(m.name == "multiply" for m in static_methods)

    def test_struct_methods(self, sample_cpp_code):
        """Test parsing struct methods."""
        handler = CppHandler(sample_cpp_code)
        classes = handler.get_classes()

        point_struct = next((c for c in classes if c.name == "Point"), None)
        assert point_struct is not None
        method_names = [m.name for m in point_struct.methods]
        assert "distance" in method_names

    def test_function_with_params(self, sample_cpp_code):
        """Test function parameter parsing."""
        handler = CppHandler(sample_cpp_code)
        functions = handler.get_functions()

        standalone_func = next((f for f in functions if f.name == "standaloneFunction"), None)
        assert standalone_func is not None
        assert len(standalone_func.parameters) == 0

        template_func = next((f for f in functions if f.name == "maxValue"), None)
        assert template_func is not None
        assert len(template_func.parameters) == 2

    def test_return_type_parsing(self, sample_cpp_code):
        """Test return type extraction."""
        handler = CppHandler(sample_cpp_code)
        functions = handler.get_functions()

        standalone_func = next((f for f in functions if f.name == "standaloneFunction"), None)
        assert standalone_func is not None
        assert standalone_func.return_type is not None
        assert "int" in standalone_func.return_type

    def test_const_method(self, sample_cpp_code):
        """Test const method detection."""
        handler = CppHandler(sample_cpp_code)
        classes = handler.get_classes()

        calculator_class = next((c for c in classes if c.name == "Calculator"), None)
        assert calculator_class is not None
        const_methods = calculator_class.methods
        assert any(m.name == "getValue" for m in const_methods)

    def test_empty_content(self):
        """Test handling empty content."""
        handler = CppHandler("")
        functions = handler.get_functions()
        classes = handler.get_classes()

        assert functions == []
        assert classes == []

    def test_parse_from_file(self, temp_cpp_file):
        """Test parsing from file."""
        handler = CppHandler.from_file(temp_cpp_file)
        functions = handler.get_functions()
        classes = handler.get_classes()

        assert len(functions) >= 1
        assert len(classes) >= 1

    def test_extensions_property(self):
        """Test extensions property."""
        handler = CppHandler("")
        assert handler.extensions == CppHandler.SUPPORTED_EXTENSIONS

    def test_namespace_functions(self, sample_cpp_code):
        """Test parsing functions inside namespace."""
        handler = CppHandler(sample_cpp_code)
        classes = handler.get_classes()

        math_utils = next((c for c in classes if c.name == "MathUtils"), None)
        assert math_utils is not None
        assert len(math_utils.methods) >= 1
