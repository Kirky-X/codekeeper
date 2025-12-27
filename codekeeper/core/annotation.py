import ast
import logging
from dataclasses import dataclass, field
from pathlib import Path

from codekeeper.languages.base import FunctionInfo as BaseFunctionInfo
from codekeeper.languages.base import ILanguageHandler
from codekeeper.languages.factory import LanguageFactory
from codekeeper.utils.file import get_language

logger = logging.getLogger(__name__)


@dataclass
class FunctionAnnotation:
    name: str
    file_path: Path
    start_line: int
    end_line: int
    signature: str
    parameters: list[str]
    return_type: str | None
    has_docstring: bool
    has_inline_comment: bool
    is_method: bool = False
    class_name: str | None = None

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "file_path": str(self.file_path),
            "start_line": self.start_line,
            "end_line": self.end_line,
            "signature": self.signature,
            "parameters": self.parameters,
            "return_type": self.return_type,
            "has_docstring": self.has_docstring,
            "has_inline_comment": self.has_inline_comment,
            "is_method": self.is_method,
            "class_name": self.class_name,
        }


@dataclass
class AnnotationResult:
    file_path: Path
    functions_found: int
    functions_with_comments: int
    functions_without_comments: int
    functions: list[FunctionAnnotation]
    missing_comments: list[FunctionAnnotation] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "file_path": str(self.file_path),
            "functions_found": self.functions_found,
            "functions_with_comments": self.functions_with_comments,
            "functions_without_comments": self.functions_without_comments,
            "missing_comments": [f.to_dict() for f in self.missing_comments],
            "functions": [f.to_dict() for f in self.functions],
        }


class AnnotationScanner:
    def __init__(
            self,
            skip_private: bool = False,
            skip_dunder: bool = True,
            languages: list[str] | None = None,
    ):
        self.skip_private = skip_private
        self.skip_dunder = skip_dunder
        self.supported_languages = languages or ["python", "rust", "java", "go"]
        self._handlers: dict[str, ILanguageHandler] = {}

    def register_handler(self, language: str, handler: ILanguageHandler) -> None:
        self._handlers[language] = handler

    def get_handler(self, file_path: Path) -> ILanguageHandler | None:
        return LanguageFactory.get_handler(file_path)

    def _get_comment_before_line(self, lines: list[str], line_num: int) -> str | None:
        comment_lines = []
        current_line = line_num - 1

        while current_line >= 0:
            stripped = lines[current_line].strip()
            if not stripped:
                current_line -= 1
                continue

            if stripped.startswith("#"):
                comment_lines.insert(0, stripped[1:].strip())
                current_line -= 1
            elif stripped.startswith('"""') or stripped.startswith("'''"):
                comment_lines.insert(0, stripped)
                break
            else:
                break

        if comment_lines:
            return "\n".join(comment_lines)
        return None

    def _get_docstring(self, node: ast.AST) -> str | None:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if node.body and isinstance(node.body[0], (ast.Str, ast.Constant)):
                return node.body[0].s if isinstance(node.body[0], ast.Str) else node.body[0].value
            elif hasattr(ast, "get_docstring") and callable(getattr(ast, "get_docstring", None)):
                try:
                    return ast.get_docstring(node)
                except Exception:
                    pass
        return None

    def _has_inline_comment(self, lines: list[str], node: ast.AST) -> bool:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and hasattr(node, "lineno"):
            line_idx = min(node.lineno - 1, len(lines) - 1)
            if line_idx >= 0:
                for i in range(max(0, line_idx - 5), line_idx):
                    if lines[i].strip().startswith("#"):
                        return True
        return False

    def _get_function_signature(self, node: ast.FunctionDef) -> str:
        args = []
        defaults = []

        for _i, arg in enumerate(node.args.args):
            arg_name = arg.arg
            if arg.annotation:
                if isinstance(arg.annotation, ast.Name):
                    arg_name += f": {arg.annotation.id}"
                elif isinstance(arg.annotation, ast.Attribute):
                    arg_name += f": {arg.annotation.value.id}.{arg.annotation.attr}"
            args.append(arg_name)

        for default in node.args.defaults:
            if isinstance(default, ast.Constant):
                defaults.append(str(default.value))
            elif isinstance(default, ast.Name):
                defaults.append(default.id)

        defaults_offset = len(args) - len(defaults)
        for i, default in enumerate(defaults):
            args[defaults_offset + i] += f"={default}"

        if node.args.vararg:
            args.append(f"*{node.args.vararg.arg}")
        if node.args.kwarg:
            args.append(f"**{node.args.kwarg.arg}")

        func_name = node.name
        if node.returns:
            if isinstance(node.returns, ast.Name):
                return_type = f" -> {node.returns.id}"
            elif isinstance(node.returns, ast.Attribute):
                return_type = f" -> {node.returns.value.id}.{node.returns.attr}"
            elif isinstance(node.returns, ast.Constant):
                return_type = f" -> {node.returns.value}"
            else:
                return_type = ""
        else:
            return_type = ""

        return f"{func_name}({', '.join(args)}){return_type}"

    def _convert_function_info_to_annotation(
            self,
            func_info: BaseFunctionInfo,
            lines: list[str],
            is_method: bool = False,
            class_name: str | None = None,
    ) -> FunctionAnnotation:
        docstring = func_info.docstring
        has_docstring = docstring is not None and len(docstring.strip()) > 0

        has_inline = self._has_inline_comment_before(lines, func_info.start_line)

        return FunctionAnnotation(
            name=func_info.name,
            file_path=func_info.file_path,
            start_line=func_info.start_line,
            end_line=func_info.end_line,
            signature=func_info.name,
            parameters=func_info.parameters,
            return_type=func_info.return_type,
            has_docstring=has_docstring,
            has_inline_comment=has_inline,
            is_method=is_method,
            class_name=class_name,
        )

    def _has_inline_comment_before(self, lines: list[str], line_num: int) -> bool:
        if line_num <= 1:
            return False
        start_idx = max(0, line_num - 6)
        return any(lines[i].strip().startswith("#") for i in range(start_idx, line_num - 1))

    def scan_python_file(self, file_path: Path) -> AnnotationResult:
        try:
            with open(file_path, encoding="utf-8", errors="replace") as f:
                content = f.read()

            lines = content.split("\n")

            try:
                tree = ast.parse(content)
            except SyntaxError as e:
                logger.warning(f"Cannot parse {file_path}: {e}")
                return AnnotationResult(
                    file_path=file_path,
                    functions_found=0,
                    functions_with_comments=0,
                    functions_without_comments=0,
                    functions=[],
                )

            functions: list[FunctionAnnotation] = []
            missing_comments: list[FunctionAnnotation] = []

            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    func_name = node.name

                    if self.skip_dunder and func_name.startswith("__") and func_name.endswith("__"):
                        continue

                    if self.skip_private and func_name.startswith("_"):
                        continue

                    start_line = node.lineno
                    end_line = node.end_lineno or start_line

                    docstring = self._get_docstring(node)
                    has_inline = self._has_inline_comment(lines, node)
                    has_docstring = docstring is not None
                    has_comment = has_docstring or has_inline

                    signature = self._get_function_signature(node)

                    parameters = [arg.arg for arg in node.args.args]
                    return_annotation = None
                    if node.returns:
                        if isinstance(node.returns, ast.Name):
                            return_annotation = node.returns.id
                        elif isinstance(node.returns, ast.Attribute):
                            return_annotation = f"{node.returns.value.id}.{node.returns.attr}"
                        elif isinstance(node.returns, ast.Constant):
                            return_annotation = str(node.returns.value)

                    func_annotation = FunctionAnnotation(
                        name=func_name,
                        file_path=file_path,
                        start_line=start_line,
                        end_line=end_line,
                        signature=signature,
                        parameters=parameters,
                        return_type=return_annotation,
                        has_docstring=has_docstring,
                        has_inline_comment=has_inline,
                    )

                    functions.append(func_annotation)

                    if not has_comment:
                        missing_comments.append(func_annotation)

                elif isinstance(node, ast.ClassDef):
                    class_name = node.name
                    for item in node.body:
                        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            func_name = item.name

                            if (
                                    self.skip_dunder
                                    and func_name.startswith("__")
                                    and func_name.endswith("__")
                            ):
                                continue

                            if self.skip_private and func_name.startswith("_"):
                                continue

                            start_line = item.lineno
                            end_line = item.end_lineno or start_line

                            docstring = self._get_docstring(item)
                            has_inline = self._has_inline_comment(lines, item)
                            has_docstring = docstring is not None
                            has_comment = has_docstring or has_inline

                            signature = self._get_function_signature(item)

                            parameters = [arg.arg for arg in item.args.args]
                            return_annotation = None
                            if item.returns:
                                if isinstance(item.returns, ast.Name):
                                    return_annotation = item.returns.id
                                elif isinstance(item.returns, ast.Attribute):
                                    return_annotation = (
                                        f"{item.returns.value.id}.{item.returns.attr}"
                                    )
                                elif isinstance(item.returns, ast.Constant):
                                    return_annotation = str(item.returns.value)

                            func_annotation = FunctionAnnotation(
                                name=func_name,
                                file_path=file_path,
                                start_line=start_line,
                                end_line=end_line,
                                signature=signature,
                                parameters=parameters,
                                return_type=return_annotation,
                                has_docstring=has_docstring,
                                has_inline_comment=has_inline,
                                is_method=True,
                                class_name=class_name,
                            )

                            functions.append(func_annotation)

                            if not has_comment:
                                missing_comments.append(func_annotation)

            with_comments = len(functions) - len(missing_comments)

            return AnnotationResult(
                file_path=file_path,
                functions_found=len(functions),
                functions_with_comments=with_comments,
                functions_without_comments=len(missing_comments),
                functions=functions,
                missing_comments=missing_comments,
            )

        except Exception as e:
            logger.error(f"Error scanning {file_path}: {e}")
            return AnnotationResult(
                file_path=file_path,
                functions_found=0,
                functions_with_comments=0,
                functions_without_comments=0,
                functions=[],
            )

    def scan_with_handler(self, file_path: Path, handler: ILanguageHandler) -> AnnotationResult:
        try:
            content = file_path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            logger.warning(f"Cannot read {file_path}: {e}")
            return AnnotationResult(
                file_path=file_path,
                functions_found=0,
                functions_with_comments=0,
                functions_without_comments=0,
                functions=[],
            )

        try:
            functions = handler.parse_functions(content, file_path)
            classes = handler.parse_classes(content, file_path)
        except Exception as e:
            logger.warning(f"Handler failed to parse {file_path}: {e}")
            return AnnotationResult(
                file_path=file_path,
                functions_found=0,
                functions_with_comments=0,
                functions_without_comments=0,
                functions=[],
            )

        lines = content.split("\n")
        annotations: list[FunctionAnnotation] = []
        missing_comments: list[FunctionAnnotation] = []

        for func in functions:
            if self.skip_dunder and func.name.startswith("__") and func.name.endswith("__"):
                continue
            if self.skip_private and func.name.startswith("_"):
                continue

            annotation = self._convert_function_info_to_annotation(func, lines)
            annotations.append(annotation)

            if not annotation.has_docstring and not annotation.has_inline_comment:
                missing_comments.append(annotation)

        for cls in classes:
            for method in cls.methods:
                if self.skip_dunder and method.name.startswith("__") and method.name.endswith("__"):
                    continue
                if self.skip_private and method.name.startswith("_"):
                    continue

                annotation = self._convert_function_info_to_annotation(
                    method, lines, True, cls.name
                )
                annotations.append(annotation)

                if not annotation.has_docstring and not annotation.has_inline_comment:
                    missing_comments.append(annotation)

        with_comments = len(annotations) - len(missing_comments)

        return AnnotationResult(
            file_path=file_path,
            functions_found=len(annotations),
            functions_with_comments=with_comments,
            functions_without_comments=len(missing_comments),
            functions=annotations,
            missing_comments=missing_comments,
        )

    def scan_file(self, file_path: Path) -> AnnotationResult:
        language = get_language(file_path)

        if language == "python":
            return self.scan_python_file(file_path)

        handler = self.get_handler(file_path)
        if handler:
            return self.scan_with_handler(file_path, handler)

        logger.debug(f"No handler for language: {language}, skipping {file_path}")
        return AnnotationResult(
            file_path=file_path,
            functions_found=0,
            functions_with_comments=0,
            functions_without_comments=0,
            functions=[],
        )

    def scan_files(
            self,
            file_paths: list[Path],
            skip_private: bool = False,
            skip_dunder: bool = True,
    ) -> list[AnnotationResult]:
        results = []
        for file_path in file_paths:
            original_skip_private = self.skip_private
            original_skip_dunder = self.skip_dunder

            self.skip_private = skip_private
            self.skip_dunder = skip_dunder

            result = self.scan_file(file_path)
            results.append(result)

            self.skip_private = original_skip_private
            self.skip_dunder = original_skip_dunder

        return results

    def get_summary(self, results: list[AnnotationResult]) -> dict:
        total_functions = 0
        total_with_comments = 0
        total_without_comments = 0
        files_scanned = 0
        files_with_issues = 0

        missing_by_file: dict[str, int] = {}

        for result in results:
            if result.functions_found > 0:
                files_scanned += 1
                total_functions += result.functions_found
                total_with_comments += result.functions_with_comments
                total_without_comments += result.functions_without_comments

                if result.functions_without_comments > 0:
                    files_with_issues += 1
                    missing_by_file[str(result.file_path)] = result.functions_without_comments

        return {
            "total_files_scanned": files_scanned,
            "total_functions": total_functions,
            "functions_with_comments": total_with_comments,
            "functions_without_comments": total_without_comments,
            "comment_coverage": (
                round(total_with_comments / total_functions * 100, 2)
                if total_functions > 0
                else 100
            ),
            "files_with_issues": files_with_issues,
            "missing_comments_by_file": dict(
                sorted(missing_by_file.items(), key=lambda x: x[1], reverse=True)
            ),
        }
