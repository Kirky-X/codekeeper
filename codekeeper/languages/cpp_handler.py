import re
from pathlib import Path
from typing import Optional

from codekeeper.languages.base import (
    ClassInfo,
    CommentStyle,
    CopyrightPosition,
    FunctionInfo,
    ILanguageHandler,
)


class CppHandler(ILanguageHandler):
    SUPPORTED_EXTENSIONS = [".c", ".cpp", ".cc", ".cxx", ".h", ".hpp", ".hh", ".hxx", ".c++", ".h++"]

    FUNC_PATTERN = re.compile(
        r"^(?P<indent>\s*)"
        r"(?P<return_type>[\w\s*&]+?)\s+"
        r"(?P<name>\w+)\s*"
        r"\((?P<params>[^)]*)\)"
        r"(?:\s*const)?\s*(?:override|nfinal)?\s*\{",
        re.MULTILINE,
    )

    METHOD_PATTERN = re.compile(
        r"^(?P<indent>\s*)(?:static\s+)?"
        r"(?P<return_type>[\w\s*&]+?)\s+"
        r"(?P<name>\w+)\s*"
        r"\((?P<params>[^)]*)\)"
        r"(?:\s*const)?\s*(?:override|nfinal)?\s*\{",
        re.MULTILINE,
    )

    CLASS_PATTERN = re.compile(
        r"^(?P<indent>\s*)(?:template\s*<[^>]*>\s*)?"
        r"(?:class|struct)\s+"
        r"(?P<name>\w+)"
        r"(?:\s*:\s*(?:public|private|protected)\s+[\w:]+(?:\s*,\s*(?:public|private|protected)\s+[\w:]+)*)?"
        r"\s*\{",
        re.MULTILINE,
    )

    STRUCT_PATTERN = re.compile(
        r"^(?P<indent>\s*)struct\s+(?P<name>\w+)\s*\{",
        re.MULTILINE,
    )

    NAMESPACE_PATTERN = re.compile(
        r"^(?P<indent>\s*)namespace\s+(?P<name>[\w:]+)?\s*\{",
        re.MULTILINE,
    )

    ENUM_PATTERN = re.compile(
        r"^(?P<indent>\s*)(?:enum\s+class\s+)?(?P<name>\w+)\s*=\{",
        re.MULTILINE,
    )

    COMMENT_PATTERN = re.compile(r"//\s*(.*)$", re.MULTILINE)

    @property
    def extensions(self) -> list[str]:
        return self.SUPPORTED_EXTENSIONS

    def __init__(self, content: str = "", file_path: Path | None = None):
        self._content = content
        self._file_path = file_path

    @classmethod
    def from_file(cls, file_path: Path | str) -> "CppHandler":
        path = Path(file_path) if isinstance(file_path, str) else file_path
        content = path.read_text(encoding="utf-8")
        return cls(content=content, file_path=path)

    def get_functions(self) -> list[FunctionInfo]:
        if self._content:
            file_path = self._file_path if self._file_path else Path(".")
            return self._parse_functions(self._content, file_path)
        return []

    def get_classes(self) -> list[ClassInfo]:
        if self._content:
            file_path = self._file_path if self._file_path else Path(".")
            classes = []
            classes.extend(self._parse_classes(self._content, file_path))
            classes.extend(self._parse_structs(self._content, file_path))
            classes.extend(self._parse_namespaces(self._content, file_path))
            return classes
        return []

    def get_copyright_header(self) -> dict | None:
        if self.has_copyright(self._content):
            return {"detected": True, "style": self.get_comment_style()}
        return None

    def get_comment_style(self) -> CommentStyle:
        return CommentStyle.SINGLE_LINE

    def get_copyright_position(self) -> CopyrightPosition:
        return CopyrightPosition.FILE_TOP

    def has_copyright(self, content: str) -> bool:
        copyright_patterns = [
            "Copyright",
            "SPDX-License-Identifier",
            "license",
            "Licensed under the MIT",
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

        if lines and (lines[0].startswith("//") or lines[0].startswith("/*")):
            doc_end = 0
            for i, line in enumerate(lines):
                if line.strip() and not line.strip().startswith("//") and not line.strip().startswith("/*"):
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
                elif char == ";" and depth == 0:
                    return i

            i += 1

        return start_pos

    def _get_docstring(self, content: str, start_line: int) -> str | None:
        lines = content.split("\n")
        if start_line > len(lines):
            return None

        doc_lines = []
        for i in range(start_line - 2, -1, -1):
            if i < 0:
                break
            line = lines[i]
            match = re.match(r"//\s*(.*)$", line)
            if match:
                doc_lines.insert(0, match.group(1).strip())
            elif line.strip() and not line.strip().startswith("//"):
                break

        return "\n".join(doc_lines) if doc_lines else None

    def _parse_function_params(self, params_str: str) -> list[str]:
        if not params_str.strip():
            return []

        params = []
        current_param = ""
        paren_depth = 0
        template_depth = 0

        for char in params_str:
            if char == "(":
                paren_depth += 1
                current_param += char
            elif char == ")":
                paren_depth -= 1
                current_param += char
            elif char == "<":
                template_depth += 1
                current_param += char
            elif char == ">":
                template_depth -= 1
                current_param += char
            elif char == "," and paren_depth == 0 and template_depth == 0:
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

    def _extract_param_name(self, param: str) -> Optional[str]:
        param = param.strip()
        parts = param.split()
        if len(parts) >= 2:
            param_type = parts[-2]
            param_name = parts[-1]
            if param_name not in ["const", "*", "&", "**"]:
                return param_name.rstrip(";*&")
            elif param_type not in ["const", "*", "&", "**"]:
                return param_type.rstrip(";*&")
        elif len(parts) == 1:
            name = parts[0].rstrip(";*&")
            if name and not name[0].isdigit():
                return name
        return None

    def _parse_function(
            self, match: re.Match, content: str, file_path: Path
    ) -> FunctionInfo | None:
        name = match.group("name")
        params_str = match.group("params")
        return_type = match.group("return_type")

        start_line = content[: match.start()].count("\n") + 1

        brace_pos = content.find("{", match.start())
        if brace_pos == -1:
            return None

        brace_end = self._find_matching_brace(content, brace_pos)
        end_line = content[:brace_end].count("\n") + 1

        params = self._parse_function_params(params_str)
        docstring = self._get_docstring(content, start_line)

        return_type_str = None
        if return_type:
            return_type_str = return_type.strip()

        return FunctionInfo(
            name=name,
            file_path=file_path,
            start_line=start_line,
            end_line=end_line,
            parameters=params,
            decorators=[],
            docstring=docstring,
            return_type=return_type_str,
        )

    def _parse_class(self, match: re.Match, content: str, file_path: Path) -> ClassInfo:
        name = match.group("name")

        start_line = content[: match.start()].count("\n") + 1

        brace_pos = content.find("{", match.start())
        if brace_pos == -1:
            return ClassInfo(
                name=name,
                file_path=file_path,
                start_line=start_line,
                end_line=start_line,
                methods=[],
                docstring=None,
                decorators=[],
            )

        brace_end = self._find_matching_brace(content, brace_pos)
        end_line = content[:brace_end].count("\n") + 1

        class_content = content[brace_pos + 1: brace_end]
        methods = self._parse_methods_in_class(class_content, content, file_path, start_line)

        docstring = self._get_docstring(content, start_line)

        return ClassInfo(
            name=name,
            file_path=file_path,
            start_line=start_line,
            end_line=end_line,
            methods=methods,
            docstring=docstring,
            decorators=["class"],
        )

    def _parse_struct(self, match: re.Match, content: str, file_path: Path) -> ClassInfo:
        name = match.group("name")

        start_line = content[: match.start()].count("\n") + 1

        brace_pos = content.find("{", match.start())
        if brace_pos == -1:
            return ClassInfo(
                name=name,
                file_path=file_path,
                start_line=start_line,
                end_line=start_line,
                methods=[],
                docstring=None,
                decorators=[],
            )

        brace_end = self._find_matching_brace(content, brace_pos)
        end_line = content[:brace_end].count("\n") + 1

        struct_content = content[brace_pos + 1: brace_end]
        methods = self._parse_methods_in_struct(struct_content, content, file_path, start_line)

        docstring = self._get_docstring(content, start_line)

        return ClassInfo(
            name=name,
            file_path=file_path,
            start_line=start_line,
            end_line=end_line,
            methods=methods,
            docstring=docstring,
            decorators=["struct"],
        )

    def _parse_namespace(self, match: re.Match, content: str, file_path: Path) -> ClassInfo:
        name = match.group("name") or "anonymous"

        start_line = content[: match.start()].count("\n") + 1

        brace_pos = content.find("{", match.start())
        if brace_pos == -1:
            return ClassInfo(
                name=name,
                file_path=file_path,
                start_line=start_line,
                end_line=start_line,
                methods=[],
                docstring=None,
                decorators=[],
            )

        brace_end = self._find_matching_brace(content, brace_pos)
        end_line = content[:brace_end].count("\n") + 1

        namespace_content = content[brace_pos + 1: brace_end]
        methods = self._parse_functions_in_content(namespace_content, content, file_path, start_line)

        docstring = self._get_docstring(content, start_line)

        return ClassInfo(
            name=name,
            file_path=file_path,
            start_line=start_line,
            end_line=end_line,
            methods=methods,
            docstring=docstring,
            decorators=["namespace"],
        )

    def _parse_methods_in_class(
            self, class_content: str, full_content: str, file_path: Path, _base_line: int
    ) -> list[FunctionInfo]:
        methods = []
        class_lines = class_content.split("\n")

        for line in class_lines:
            method_match = self.METHOD_PATTERN.match(line)
            if method_match:
                full_line_start = full_content.find(line)
                if full_line_start != -1:
                    parsed = self._parse_function(method_match, full_content, file_path)
                    if parsed:
                        methods.append(parsed)

        return methods

    def _parse_methods_in_struct(
            self, struct_content: str, full_content: str, file_path: Path, _base_line: int
    ) -> list[FunctionInfo]:
        return self._parse_methods_in_class(struct_content, full_content, file_path, _base_line)

    def _parse_functions_in_content(
            self, block_content: str, full_content: str, file_path: Path, _base_line: int
    ) -> list[FunctionInfo]:
        functions = []
        lines = block_content.split("\n")

        for line in lines:
            func_match = self.FUNC_PATTERN.match(line)
            if func_match:
                full_line_start = full_content.find(line)
                if full_line_start != -1:
                    parsed = self._parse_function(func_match, full_content, file_path)
                    if parsed:
                        functions.append(parsed)

        return functions

    def _parse_functions(self, content: str, file_path: Path) -> list[FunctionInfo]:
        functions = []
        for match in self.FUNC_PATTERN.finditer(content):
            parsed = self._parse_function(match, content, file_path)
            if parsed:
                functions.append(parsed)
        return functions

    def _parse_classes(self, content: str, file_path: Path) -> list[ClassInfo]:
        classes = []
        for match in self.CLASS_PATTERN.finditer(content):
            parsed = self._parse_class(match, content, file_path)
            if parsed:
                classes.append(parsed)
        return classes

    def _parse_structs(self, content: str, file_path: Path) -> list[ClassInfo]:
        structs = []
        for match in self.STRUCT_PATTERN.finditer(content):
            parsed = self._parse_struct(match, content, file_path)
            if parsed:
                structs.append(parsed)
        return structs

    def _parse_namespaces(self, content: str, file_path: Path) -> list[ClassInfo]:
        namespaces = []
        for match in self.NAMESPACE_PATTERN.finditer(content):
            parsed = self._parse_namespace(match, content, file_path)
            if parsed:
                namespaces.append(parsed)
        return namespaces

    def parse_functions(self, content: str, file_path: Path) -> list[FunctionInfo]:
        return self._parse_functions(content, file_path)

    def parse_classes(self, content: str, file_path: Path) -> list[ClassInfo]:
        classes = []
        classes.extend(self._parse_classes(content, file_path))
        classes.extend(self._parse_structs(content, file_path))
        classes.extend(self._parse_namespaces(content, file_path))
        return classes

    def parse_all(
            self, content: str, file_path: Path
    ) -> tuple[list[FunctionInfo], list[ClassInfo]]:
        functions = self._parse_functions(content, file_path)
        classes = []
        classes.extend(self._parse_classes(content, file_path))
        classes.extend(self._parse_structs(content, file_path))
        classes.extend(self._parse_namespaces(content, file_path))
        return functions, classes
