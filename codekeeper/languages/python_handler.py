import ast
from pathlib import Path

from codekeeper.languages.base import (
    ClassInfo,
    CommentStyle,
    CopyrightPosition,
    FunctionInfo,
    ILanguageHandler,
)


class PythonHandler(ILanguageHandler):
    SUPPORTED_EXTENSIONS = [".py", ".pyw"]

    def __init__(self, content: str = "", file_path: Path | None = None):
        self._content = content
        self._file_path = file_path

    @classmethod
    def from_file(cls, file_path: Path | str) -> "PythonHandler":
        path = Path(file_path) if isinstance(file_path, str) else file_path
        content = path.read_text(encoding="utf-8")
        return cls(content=content, file_path=path)

    @property
    def extensions(self) -> list[str]:
        return self.SUPPORTED_EXTENSIONS

    def get_comment_style(self) -> CommentStyle:
        return CommentStyle.SINGLE_LINE

    def get_copyright_position(self) -> CopyrightPosition:
        return CopyrightPosition.AFTER_DOCSTRING

    def has_copyright(self, content: str) -> bool:
        copyright_patterns = [
            "Copyright",
            "copyright",
            "SPDX-License-Identifier",
            "license",
        ]
        return any(pattern in content for pattern in copyright_patterns)

    def get_copyright_template(
            self,
            license: str,
            author: str | None = None,
            year_range: str | None = None,
    ) -> str:
        lines = [
            f"# Copyright (c) {year_range or '2025'} {author or 'Author'}. All rights reserved.",
            f"# Licensed under the {license} License.",
            "# See LICENSE file in the project root for full license information.",
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

        lines = content.split("\n")

        if position == CopyrightPosition.FILE_TOP:
            return template + "\n\n" + content

        docstring_end = 0
        if (lines and lines[0].startswith('"""')) or lines[0].startswith("'''"):
            quote_char = lines[0][:3]
            for i, line in enumerate(lines[1:], start=1):
                if quote_char in line:
                    docstring_end = i
                    break

        if docstring_end > 0:
            return (
                    "\n".join(lines[: docstring_end + 1])
                    + "\n\n"
                    + template
                    + "\n\n"
                    + "\n".join(lines[docstring_end + 1:])
            )

        return template + "\n\n" + content

    def _get_node_line_range(self, node: ast.AST) -> tuple[int, int]:
        start_line = node.lineno
        end_line = node.end_lineno if hasattr(node, "end_lineno") else start_line
        return start_line, end_line

    def _get_decorators(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> list[str]:
        decorators = []
        for decorator in node.decorator_list:
            if isinstance(decorator, ast.Name):
                decorators.append(f"@{decorator.id}")
            elif isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Name):
                decorators.append(f"@{decorator.func.id}(...)")
            elif isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Attribute):
                base = (
                    decorator.func.value.id
                    if isinstance(decorator.func.value, ast.Name)
                    else "..."
                )
                decorators.append(f"@{base}.{decorator.func.attr}(...)")
            elif isinstance(decorator, ast.Attribute):
                base = decorator.value.id if isinstance(decorator.value, ast.Name) else "..."
                decorators.append(f"@{base}.{decorator.attr}")
        return decorators

    def _get_docstring(
            self, node: ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef
    ) -> str | None:
        if node.body and isinstance(node.body[0], ast.Expr):
            expr = node.body[0]
            if isinstance(expr.value, (ast.Constant, ast.Str)):
                docstring = expr.value.s if isinstance(expr.value, ast.Str) else expr.value.value
                if isinstance(docstring, str):
                    return docstring.strip()
        return None

    def _get_parameters(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> list[str]:
        params = []
        for arg in node.args.args:
            param_name = arg.arg
            if arg.annotation:
                if isinstance(arg.annotation, ast.Name):
                    param_name += f": {arg.annotation.id}"
                elif isinstance(arg.annotation, ast.Attribute):
                    module = (
                        arg.annotation.value.id
                        if isinstance(arg.annotation.value, ast.Name)
                        else "..."
                    )
                    param_name += f": {module}.{arg.annotation.attr}"
            params.append(param_name)
        if node.args.vararg:
            params.append(f"*{node.args.vararg.arg}")
        if node.args.kwarg:
            params.append(f"**{node.args.kwarg.arg}")
        return params

    def _parse_function(
            self, node: ast.FunctionDef | ast.AsyncFunctionDef, file_path: Path
    ) -> FunctionInfo:
        start_line, end_line = self._get_node_line_range(node)
        decorators = self._get_decorators(node)
        parameters = self._get_parameters(node)
        docstring = self._get_docstring(node)

        return_type = None
        if node.returns:
            if isinstance(node.returns, ast.Name):
                return_type = node.returns.id
            elif isinstance(node.returns, ast.Attribute):
                module = (
                    node.returns.value.id if isinstance(node.returns.value, ast.Name) else "..."
                )
                return_type = f"{module}.{node.returns.attr}"

        return FunctionInfo(
            name=node.name,
            file_path=file_path,
            start_line=start_line,
            end_line=end_line,
            parameters=parameters,
            decorators=decorators,
            docstring=docstring,
            return_type=return_type,
        )

    def _parse_class(self, node: ast.ClassDef, file_path: Path) -> ClassInfo:
        start_line, end_line = self._get_node_line_range(node)
        docstring = self._get_docstring(node)

        methods = []
        for item in node.body:
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                methods.append(self._parse_function(item, file_path))

        decorators = []
        for decorator in node.decorator_list:
            if isinstance(decorator, ast.Name):
                decorators.append(f"@{decorator.id}")
            elif isinstance(decorator, ast.Call):
                if isinstance(decorator.func, ast.Name):
                    decorators.append(f"@{decorator.func.id}(...)")

        return ClassInfo(
            name=node.name,
            file_path=file_path,
            start_line=start_line,
            end_line=end_line,
            methods=methods,
            docstring=docstring,
            decorators=decorators,
        )

    def parse_functions(self, content: str, file_path: Path) -> list[FunctionInfo]:
        functions = []
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and (
                        not isinstance(node, ast.FunctionDef) or not node.name.startswith("_")
                ):
                    functions.append(self._parse_function(node, file_path))
        except SyntaxError:
            pass
        return functions

    def parse_classes(self, content: str, file_path: Path) -> list[ClassInfo]:
        classes = []
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    classes.append(self._parse_class(node, file_path))
        except SyntaxError:
            pass
        return classes

    def parse_all(
            self, content: str, file_path: Path
    ) -> tuple[list[FunctionInfo], list[ClassInfo]]:
        functions = self.parse_functions(content, file_path)
        classes = self.parse_classes(content, file_path)
        return functions, classes

    def get_functions(self) -> list[FunctionInfo]:
        if self._content:
            file_path = self._file_path if self._file_path else Path(".")
            return self.parse_functions(self._content, file_path)
        return []

    def get_classes(self) -> list[ClassInfo]:
        if self._content:
            file_path = self._file_path if self._file_path else Path(".")
            return self.parse_classes(self._content, file_path)
        return []

    def get_copyright_header(self) -> dict | None:
        if self.has_copyright(self._content):
            return {"detected": True, "style": self.get_comment_style()}
        return None
