from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class CommentStyle(Enum):
    SINGLE_LINE = "single_line"
    MULTI_LINE = "multi_line"
    DOCSTRING = "docstring"


class CopyrightPosition(Enum):
    FILE_TOP = "file_top"
    AFTER_DOCSTRING = "after_docstring"
    MODULE_DOCSTRING = "module_docstring"


@dataclass
class FunctionInfo:
    name: str
    file_path: Path
    start_line: int
    end_line: int
    parameters: list[str]
    decorators: list[str]
    docstring: str | None = None
    return_type: str | None = None


@dataclass
class ClassInfo:
    name: str
    file_path: Path
    start_line: int
    end_line: int
    methods: list[FunctionInfo]
    docstring: str | None = None
    decorators: list[str] = None


class ILanguageHandler(ABC):
    @property
    @abstractmethod
    def extensions(self) -> list[str]:
        pass

    @abstractmethod
    def get_comment_style(self) -> CommentStyle:
        pass

    @abstractmethod
    def get_copyright_position(self) -> CopyrightPosition:
        pass

    @abstractmethod
    def has_copyright(self, content: str) -> bool:
        pass

    @abstractmethod
    def get_copyright_template(
            self,
            license: str,
            author: str | None = None,
            year_range: str | None = None,
    ) -> str:
        pass

    @abstractmethod
    def insert_copyright(
            self,
            content: str,
            license: str,
            author: str | None = None,
            year_range: str | None = None,
            position: CopyrightPosition | None = None,
    ) -> str:
        pass

    @abstractmethod
    def parse_functions(self, content: str, file_path: Path) -> list[FunctionInfo]:
        pass

    @abstractmethod
    def parse_classes(self, content: str, file_path: Path) -> list[ClassInfo]:
        pass

    @abstractmethod
    def parse_all(
            self, content: str, file_path: Path
    ) -> tuple[list[FunctionInfo], list[ClassInfo]]:
        pass
