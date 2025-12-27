import re
from pathlib import Path
from typing import ClassVar

from codekeeper.languages.base import (
    ClassInfo,
    CommentStyle,
    CopyrightPosition,
    FunctionInfo,
    ILanguageHandler,
)


class RustHandler(ILanguageHandler):
    SUPPORTED_EXTENSIONS: ClassVar[list[str]] = [".rs"]

    FUNCTION_PATTERN = re.compile(
        r"^(?P<indent>\s*)#?(?P<visibility>pub\s+)?(?:async\s+)?fn\s+(?P<name>\w+)\s*\("
        r"(?P<params>[^)]*)\)"
        r"(?:\s*->\s*(?P<return_type>[^{]+))?\s*\{",
        re.MULTILINE,
    )

    STRUCT_PATTERN = re.compile(
        r"^(?P<indent>\s*)(?P<visibility>pub\s+)?struct\s+(?P<name>\w+)" r"(?:\s*<[^>]*>)?\s*\{",
        re.MULTILINE,
    )

    IMPL_PATTERN = re.compile(
        r"^(?P<indent>\s*)(?P<visibility>pub\s+)?impl\s+(?P<name>[\w\s<>]+?)\s*\{",
        re.MULTILINE,
    )

    TRAIT_PATTERN = re.compile(
        r"^(?P<indent>\s*)(?P<visibility>pub\s+)?trait\s+(?P<name>\w+)"
        r"(?:\s*<[^>]*>)?\s*(?P<where_clause>[^{]+)?\{",
        re.MULTILINE,
    )

    DOC_COMMENT_PATTERN = re.compile(r"///\s*(.*)$", re.MULTILINE)
    INNER_DOC_COMMENT_PATTERN = re.compile(r"//!\s*(.*)$", re.MULTILINE)

    CLOSE_BRACE_PATTERN = re.compile(r"^\s*\}", re.MULTILINE)

    def __init__(self, content: str = "", file_path: Path | None = None):
        self._content = content
        self._file_path = file_path

    @classmethod
    def from_file(cls, file_path: Path | str) -> "RustHandler":
        path = Path(file_path) if isinstance(file_path, str) else file_path
        content = path.read_text(encoding="utf-8")
        return cls(content=content, file_path=path)

    @property
    def extensions(self) -> list[str]:
        return self.SUPPORTED_EXTENSIONS

    def get_comment_style(self) -> CommentStyle:
        return CommentStyle.SINGLE_LINE

    def get_copyright_position(self) -> CopyrightPosition:
        return CopyrightPosition.FILE_TOP

    def has_copyright(self, content: str) -> bool:
        copyright_patterns = [
            "Copyright",
            "SPDX-License-Identifier",
            "license",
            " Licensed under ",
        ]
        return any(pattern in content for pattern in copyright_patterns)

    def get_copyright_template(
            self,
            license: str,
            author: str | None = None,
            year_range: str | None = None,
    ) -> str:
        lines = [
            f"// Copyright (c) {year_range or '2025'} {author or 'Author'}. All rights reserved.",
            f"// Licensed under the {license} License.",
            "// See LICENSE file in the project root for full license information.",
        ]
        return "\n".join(lines)

    def insert_copyright(
            self,
            content: str,
            license: str,
            author: str | None = None,
            year_range: str | None = None,
            position: CopyrightPosition | None = None,
    ) -> str:
        if position is None:
            position = self.get_copyright_position()

        template = self.get_copyright_template(license, author, year_range)

        if position == CopyrightPosition.FILE_TOP:
            return template + "\n\n" + content

        lines = content.split("\n")

        if lines and (lines[0].startswith("//!") or lines[0].startswith("///")):
            doc_end = 0
            for i, line in enumerate(lines):
                if not line.startswith("//") and line.strip():
                    doc_end = i
                    break
            return (
                    "\n".join(lines[:doc_end]) + "\n\n" + template + "\n\n" + "\n".join(lines[doc_end:])
            )

        return template + "\n\n" + content

    def _find_matching_brace(self, content: str, start_pos: int) -> int:
        depth = 0
        in_string = False
        in_char = False
        escaped = False

        i = start_pos
        while i < len(content):
            char = content[i]

            if escaped:
                escaped = False
                i += 1
                continue

            if char == "\\":
                escaped = True
                i += 1
                continue

            if char == '"' and not in_char:
                in_string = not in_string
            elif char == "'" and not in_string:
                in_char = not in_char
            elif not in_string and not in_char:
                if char == "{":
                    depth += 1
                elif char == "}":
                    depth -= 1
                    if depth == 0:
                        return i

            i += 1

        return start_pos

    def _get_docstring(self, content: str, end_line: int) -> str | None:
        lines = content.split("\n")
        if end_line > len(lines):
            return None

        doc_lines = []
        for i in range(end_line - 1, -1, -1):
            line = lines[i]
            match = re.match(r"///\s*(.*)$", line)
            if match:
                doc_lines.insert(0, match.group(1).strip())
            elif line.strip() and not line.strip().startswith("//"):
                break

        return "\n".join(doc_lines) if doc_lines else None

    def _parse_function_params(self, params_str: str) -> list[str]:
        if not params_str.strip():
            return []

        params = []
        for param in params_str.split(","):
            param = param.strip()
            if param:
                parts = param.split(":")
                if parts:
                    param_name = parts[0].strip()
                    if "_" in param_name or param_name == "self":
                        params.append(param_name)
                    else:
                        params.append(param)
        return params

    def _parse_function(
            self, match: re.Match, content: str, file_path: Path
    ) -> FunctionInfo | None:
        name = match.group("name")
        params_str = match.group("params")
        return_type = match.group("return_type")

        start_line = content[: match.start()].count("\n") + 1
        brace_end = self._find_matching_brace(content, match.end() - 1)
        end_line = content[:brace_end].count("\n") + 1

        params = self._parse_function_params(params_str)
        docstring = self._get_docstring(content, start_line)

        return FunctionInfo(
            name=name,
            file_path=file_path,
            start_line=start_line,
            end_line=end_line,
            parameters=params,
            decorators=[],
            docstring=docstring,
            return_type=return_type.strip() if return_type else None,
        )

    def _parse_struct(self, match: re.Match, content: str, file_path: Path) -> ClassInfo:
        name = match.group("name")

        start_line = content[: match.start()].count("\n") + 1
        brace_end = self._find_matching_brace(content, match.end() - 1)
        end_line = content[:brace_end].count("\n") + 1

        impl_content = content[match.end(): brace_end]
        methods = self._parse_methods_in_block(impl_content, content, file_path, start_line)

        return ClassInfo(
            name=name,
            file_path=file_path,
            start_line=start_line,
            end_line=end_line,
            methods=methods,
            docstring=None,
            decorators=[],
        )

    def _parse_methods_in_block(
            self, block_content: str, full_content: str, file_path: Path, _base_line: int
    ) -> list[FunctionInfo]:
        methods = []
        block_lines = block_content.split("\n")

        for _i, line in enumerate(block_lines):
            func_match = self.FUNCTION_PATTERN.match(line)
            if func_match:
                func_content_start = full_content.find(line)
                if func_content_start != -1:
                    parsed = self._parse_function(func_match, full_content, file_path)
                    if parsed:
                        methods.append(parsed)

        return methods

    def _parse_functions(self, content: str, file_path: Path) -> list[FunctionInfo]:
        functions = []
        for match in self.FUNCTION_PATTERN.finditer(content):
            parsed = self._parse_function(match, content, file_path)
            if parsed:
                functions.append(parsed)
        return functions

    def _parse_structs(self, content: str, file_path: Path) -> list[ClassInfo]:
        structs = []
        for match in self.STRUCT_PATTERN.finditer(content):
            parsed = self._parse_struct(match, content, file_path)
            if parsed:
                structs.append(parsed)
        return structs

    def _parse_impls(self, content: str, file_path: Path) -> list[ClassInfo]:
        impls = []
        for match in self.IMPL_PATTERN.finditer(content):
            start_line = content[: match.start()].count("\n") + 1
            brace_end = self._find_matching_brace(content, match.end() - 1)
            end_line = content[:brace_end].count("\n") + 1

            impl_name = match.group("name").strip()
            block_content = content[match.end(): brace_end]
            methods = self._parse_methods_in_block(block_content, content, file_path, start_line)

            impls.append(
                ClassInfo(
                    name=impl_name,
                    file_path=file_path,
                    start_line=start_line,
                    end_line=end_line,
                    methods=methods,
                    docstring=None,
                    decorators=[],
                )
            )
        return impls

    def parse_functions(self, content: str, file_path: Path) -> list[FunctionInfo]:
        return self._parse_functions(content, file_path)

    def parse_classes(self, content: str, file_path: Path) -> list[ClassInfo]:
        classes = []
        classes.extend(self._parse_structs(content, file_path))
        classes.extend(self._parse_impls(content, file_path))
        return classes

    def parse_all(
            self, content: str, file_path: Path
    ) -> tuple[list[FunctionInfo], list[ClassInfo]]:
        functions = self._parse_functions(content, file_path)
        classes = []
        classes.extend(self._parse_structs(content, file_path))
        classes.extend(self._parse_impls(content, file_path))
        return functions, classes

    def get_functions(self) -> list[FunctionInfo]:
        if self._content:
            file_path = self._file_path if self._file_path else Path(".")
            return self._parse_functions(self._content, file_path)
        return []

    def get_classes(self) -> list[ClassInfo]:
        if self._content:
            file_path = self._file_path if self._file_path else Path(".")
            classes = []
            classes.extend(self._parse_structs(self._content, file_path))
            classes.extend(self._parse_impls(self._content, file_path))
            return classes
        return []

    def get_copyright_header(self) -> dict | None:
        if self.has_copyright(self._content):
            return {"detected": True, "style": self.get_comment_style()}
        return None
