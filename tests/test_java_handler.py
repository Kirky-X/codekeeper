"""Tests for Java language handler."""

from codekeeper.languages import JavaHandler


class TestJavaHandler:
    """Tests for JavaHandler class."""

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

    def test_get_methods(self, sample_java_code):
        """Test parsing Java methods."""
        handler = JavaHandler(sample_java_code)
        functions = handler.get_functions()

        function_names = [f.name for f in functions]
        assert "add" in function_names

    def test_get_classes(self, sample_java_code):
        """Test parsing Java classes."""
        handler = JavaHandler(sample_java_code)
        classes = handler.get_classes()

        class_names = [c.name for c in classes]
        assert "Calculator" in class_names

    def test_get_copyright_header(self, sample_java_code):
        """Test copyright header detection."""
        handler = JavaHandler(sample_java_code)
        header = handler.get_copyright_header()

        assert header is not None

    def test_get_comment_style(self):
        """Test comment style detection."""
        handler = JavaHandler("")
        assert handler.get_comment_style().value == "single_line"

    def test_get_supported_extensions(self):
        """Test supported extensions."""
        assert ".java" in JavaHandler.SUPPORTED_EXTENSIONS

    def test_constructor_parsing(self, temp_java_file):
        """Test parsing Java constructors."""
        handler = JavaHandler.from_file(temp_java_file)
        functions = handler.get_functions()

        assert len(functions) >= 2

    def test_class_methods(self, temp_java_file):
        """Test parsing class and methods."""
        handler = JavaHandler.from_file(temp_java_file)
        classes = handler.get_classes()

        assert len(classes) >= 1
        assert any(c.name == "Calculator" for c in classes)
