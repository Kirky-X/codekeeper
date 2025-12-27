import re
from pathlib import Path

from codekeeper.languages.base import (
    ClassInfo,
    CommentStyle,
    CopyrightPosition,
    FunctionInfo,
    ILanguageHandler,
)


class JavaHandler(ILanguageHandler):
    SUPPORTED_EXTENSIONS = [".java"]

    METHOD_PATTERN = re.compile(
        r"^(?P<indent>\s*)(?P<visibility>public|protected|private)\s+"
        r"(?P<static>static\s+)?(?P<final>final\s+)?(?P<abstract>abstract\s+)?"
        r"(?P<return_type>[\w<>[\]]+)\s+(?P<name>\w+)\s*\("
        r"(?P<params>[^)]*)\)\s*(?P<body_start>\{)?",
        re.MULTILINE,
    )

    CONSTRUCTOR_PATTERN = re.compile(
        r"^(?P<indent>\s*)(?P<visibility>public|protected|private)\s+"
        r"(?P<static>static\s+)?(?P<final>final\s+)?"
        r"(?P<name>\w+)\s*\("
        r"(?P<params>[^)]*)\)\s*(?P<body_start>\{)?",
        re.MULTILINE,
    )

    CLASS_PATTERN = re.compile(
        r"^(?P<indent>\s*)(?P<visibility>public|protected|private)?\s*"
        r"(?P<static>static\s+)?(?P<final>final\s+)?(?P<abstract>abstract\s+)?"
        r"(?P<class_type>class|interface|enum)\s+(?P<name>\w+)"
        r"(?:\s+extends\s+[\w,\s<>]+)?(?:\s+implements\s+[\w,\s<>]+)?\s*(?P<body_start>\{)?",
        re.MULTILINE,
    )

    INNER_CLASS_PATTERN = re.compile(
        r"^(?P<indent>\s*)(?P<visibility>public|protected|private)?\s*"
        r"(?P<static>static\s+)?(?P<final>final\s+)?(?P<abstract>abstract\s+)?"
        r"(?P<class_type>class|interface|enum)\s+(?P<name>\w+)"
        r"(?:\s+extends\s+[\w,\s<>]+)?(?:\s+implements\s+[\w,\s<>]+)?\s*\{",
        re.MULTILINE,
    )

    JAVADOC_PATTERN = re.compile(r"/\*\*(.*?)\*/", re.DOTALL)
    JAVADOC_LINE_PATTERN = re.compile(r"^\s*\*\s*(.*)$", re.MULTILINE)

    CLOSE_BRACE_PATTERN = re.compile(r"^\s*\}", re.MULTILINE)

    def __init__(self, content: str = "", file_path: Path | None = None):
        self._content = content
        self._file_path = file_path

    @classmethod
    def from_file(cls, file_path: Path | str) -> "JavaHandler":
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
            "Licensed under the Apache",
        ]
        return any(pattern in content for pattern in copyright_patterns)

    def get_copyright_template(
            self,
            license: str,
            author: str | None = None,
            year_range: str | None = None,
    ) -> str:
        lines = [
            f"/* Copyright (c) {year_range or '2025'} {author or 'Author'}. All rights reserved. */",
            f"/* Licensed under the {license} License. */",
            "/* See LICENSE file in the project root for full license information. */",
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

        if lines and (lines[0].startswith("/**") or lines[0].startswith("/*")):
            doc_end = 0
            for i, line in enumerate(lines):
                if not line.strip().startswith("/*") and not line.strip().startswith("*"):
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

    def _get_javadoc(self, content: str, position: int) -> str | None:
        before_content = content[:position]
        javadoc_matches = list(self.JAVADOC_PATTERN.finditer(before_content))

        if javadoc_matches:
            last_match = javadoc_matches[-1]
            javadoc_content = last_match.group(1)
            lines = []
            for line in javadoc_content.split("\n"):
                line_match = self.JAVADOC_LINE_PATTERN.match(line)
                if line_match:
                    lines.append(line_match.group(1).strip())
                elif line.strip():
                    lines.append(line.strip())

            if lines:
                return "\n".join(lines).strip()

        return None

    def _parse_method_params(self, params_str: str) -> list[str]:
        if not params_str.strip():
            return []

        params = []
        current_param = ""
        angle_brackets = 0

        for char in params_str:
            if char == "<":
                angle_brackets += 1
                current_param += char
            elif char == ">":
                angle_brackets -= 1
                current_param += char
            elif char == "," and angle_brackets == 0:
                if current_param.strip():
                    param_name = self._extract_param_name(current_param.strip())
                    if param_name:
                        params.append(param_name)
                current_param = ""
            else:
                current_param += char

        if current_param.strip():
            param_name = self._extract_param_name(current_param.strip())
            if param_name:
                params.append(param_name)

        return params

    def _extract_param_name(self, param: str) -> str:
        parts = param.split()
        if len(parts) >= 2:
            return parts[-1]
        elif len(parts) == 1:
            if "." in param:
                return param.split(".")[-1]
            return param
        return param

    def _parse_function(
            self, match: re.Match, content: str, file_path: Path
    ) -> FunctionInfo | None:
        name = match.group("name")
        params_str = match.group("params")
        return_type = match.group("return_type")

        start_line = content[: match.start()].count("\n") + 1

        body_start = match.group("body_start")
        if body_start:
            brace_pos = match.end() - 1
        else:
            brace_pos = content.find("{", match.start())

        if brace_pos == -1:
            return None

        brace_end = self._find_matching_brace(content, brace_pos)
        end_line = content[:brace_end].count("\n") + 1

        params = self._parse_method_params(params_str)
        javadoc = self._get_javadoc(content, match.start())

        decorators = []
        if match.group("static"):
            decorators.append("static")
        if match.group("final"):
            decorators.append("final")
        if match.group("abstract"):
            decorators.append("abstract")

        return FunctionInfo(
            name=name,
            file_path=file_path,
            start_line=start_line,
            end_line=end_line,
            parameters=params,
            decorators=decorators,
            docstring=javadoc,
            return_type=return_type.strip() if return_type else None,
        )

    def _parse_constructor(
            self, match: re.Match, content: str, file_path: Path
    ) -> FunctionInfo | None:
        name = match.group("name")
        params_str = match.group("params")

        start_line = content[: match.start()].count("\n") + 1

        body_start = match.group("body_start")
        if body_start:
            brace_pos = match.end() - 1
        else:
            brace_pos = content.find("{", match.start())

        if brace_pos == -1:
            return None

        brace_end = self._find_matching_brace(content, brace_pos)
        end_line = content[:brace_end].count("\n") + 1

        params = self._parse_method_params(params_str)
        javadoc = self._get_javadoc(content, match.start())

        decorators = []
        if match.group("static"):
            decorators.append("static")
        if match.group("final"):
            decorators.append("final")

        return FunctionInfo(
            name=name,
            file_path=file_path,
            start_line=start_line,
            end_line=end_line,
            parameters=params,
            decorators=decorators,
            docstring=javadoc,
            return_type=None,
        )

    def _parse_class(self, match: re.Match, content: str, file_path: Path) -> ClassInfo | None:
        name = match.group("name")

        start_line = content[: match.start()].count("\n") + 1

        brace_pos = content.find("{", match.start())
        if brace_pos == -1:
            return None

        brace_end = self._find_matching_brace(content, brace_pos)
        end_line = content[:brace_end].count("\n") + 1

        class_content = content[brace_pos + 1: brace_end]
        methods = self._parse_methods_in_class(class_content, content, file_path, start_line)

        javadoc = self._get_javadoc(content, match.start())

        decorators = []
        if match.group("static"):
            decorators.append("static")
        if match.group("final"):
            decorators.append("final")
        if match.group("abstract"):
            decorators.append("abstract")

        return ClassInfo(
            name=name,
            file_path=file_path,
            start_line=start_line,
            end_line=end_line,
            methods=methods,
            docstring=javadoc,
            decorators=decorators,
        )

    def _parse_methods_in_class(
            self, class_content: str, full_content: str, file_path: Path, base_line: int
    ) -> list[FunctionInfo]:
        methods = []
        class_lines = class_content.split("\n")

        for i, line in enumerate(class_lines):
            method_match = self.METHOD_PATTERN.match(line)
            if method_match:
                start_line = base_line + i
                parsed = self._parse_function_with_line(
                    method_match, class_content, full_content, file_path, start_line
                )
                if parsed and parsed.name != "<init>":
                    methods.append(parsed)

            constructor_match = self.CONSTRUCTOR_PATTERN.match(line)
            if constructor_match:
                start_line = base_line + i
                parsed = self._parse_constructor_with_line(
                    constructor_match, class_content, full_content, file_path, start_line
                )
                if parsed:
                    methods.append(parsed)

        return methods

    def _parse_function_with_line(
            self,
            match: re.Match,
            class_content: str,
            full_content: str,
            file_path: Path,
            start_line: int,
    ) -> FunctionInfo | None:
        name = match.group("name")
        params_str = match.group("params")
        return_type = match.group("return_type")

        body_start = match.group("body_start")
        if body_start:
            brace_pos = match.end() - 1
        else:
            brace_pos = class_content.find("{", match.start())

        if brace_pos == -1:
            return None

        brace_end = self._find_matching_brace(class_content, brace_pos)
        end_line = start_line + class_content[:brace_end].count("\n")

        params = self._parse_method_params(params_str)
        javadoc = self._get_javadoc(full_content, match.start())

        decorators = []
        if match.group("static"):
            decorators.append("static")
        if match.group("final"):
            decorators.append("final")
        if match.group("abstract"):
            decorators.append("abstract")

        return FunctionInfo(
            name=name,
            file_path=file_path,
            start_line=start_line,
            end_line=end_line,
            parameters=params,
            decorators=decorators,
            docstring=javadoc,
            return_type=return_type.strip() if return_type else None,
        )

    def _parse_constructor_with_line(
            self,
            match: re.Match,
            class_content: str,
            full_content: str,
            file_path: Path,
            start_line: int,
    ) -> FunctionInfo | None:
        name = match.group("name")
        params_str = match.group("params")

        body_start = match.group("body_start")
        if body_start:
            brace_pos = match.end() - 1
        else:
            brace_pos = class_content.find("{", match.start())

        if brace_pos == -1:
            return None

        brace_end = self._find_matching_brace(class_content, brace_pos)
        end_line = start_line + class_content[:brace_end].count("\n")

        params = self._parse_method_params(params_str)
        javadoc = self._get_javadoc(full_content, match.start())

        decorators = []
        if match.group("static"):
            decorators.append("static")
        if match.group("final"):
            decorators.append("final")

        return FunctionInfo(
            name=name,
            file_path=file_path,
            start_line=start_line,
            end_line=end_line,
            parameters=params,
            decorators=decorators,
            docstring=javadoc,
            return_type=None,
        )

    def _parse_functions(self, content: str, file_path: Path) -> list[FunctionInfo]:
        functions = []
        for match in self.METHOD_PATTERN.finditer(content):
            parsed = self._parse_function(match, content, file_path)
            if parsed and parsed.name != "<init>":
                functions.append(parsed)

        for match in self.CONSTRUCTOR_PATTERN.finditer(content):
            parsed = self._parse_constructor(match, content, file_path)
            if parsed:
                functions.append(parsed)

        return functions

    def _parse_classes(self, content: str, file_path: Path) -> list[ClassInfo]:
        classes = []

        for match in self.CLASS_PATTERN.finditer(content):
            parsed = self._parse_class(match, content, file_path)
            if parsed:
                classes.append(parsed)

        for match in self.INNER_CLASS_PATTERN.finditer(content):
            parsed = self._parse_class(match, content, file_path)
            if parsed and not any(c.name == parsed.name for c in classes):
                classes.append(parsed)

        return classes

    def parse_functions(self, content: str, file_path: Path) -> list[FunctionInfo]:
        return self._parse_functions(content, file_path)

    def parse_classes(self, content: str, file_path: Path) -> list[ClassInfo]:
        return self._parse_classes(content, file_path)

    def parse_all(
            self, content: str, file_path: Path
    ) -> tuple[list[FunctionInfo], list[ClassInfo]]:
        functions = self._parse_functions(content, file_path)
        classes = self._parse_classes(content, file_path)
        return functions, classes

    def get_functions(self) -> list[FunctionInfo]:
        if self._content:
            file_path = self._file_path if self._file_path else Path(".")
            return self._parse_functions(self._content, file_path)
        return []

    def get_classes(self) -> list[ClassInfo]:
        if self._content:
            file_path = self._file_path if self._file_path else Path(".")
            return self._parse_classes(self._content, file_path)
        return []

    def get_copyright_header(self) -> dict | None:
        if self.has_copyright(self._content):
            return {"detected": True, "style": self.get_comment_style()}
        return None
