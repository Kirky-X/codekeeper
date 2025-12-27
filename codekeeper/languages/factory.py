from pathlib import Path

from codekeeper.languages.base import ILanguageHandler
from codekeeper.languages.go_handler import GoHandler
from codekeeper.languages.java_handler import JavaHandler
from codekeeper.languages.python_handler import PythonHandler
from codekeeper.languages.rust_handler import RustHandler


class LanguageFactory:
    _handlers: dict[str, ILanguageHandler] = {}

    @classmethod
    def register(cls, handler: ILanguageHandler) -> None:
        for ext in handler.extensions:
            cls._handlers[ext.lower()] = handler
            cls._handlers[ext] = handler

    @classmethod
    def get_handler(cls, file_path: str | Path | ILanguageHandler) -> ILanguageHandler | None:
        if isinstance(file_path, ILanguageHandler):
            return file_path

        if isinstance(file_path, Path):
            ext = file_path.suffix.lower()
        elif isinstance(file_path, str):
            if "." not in file_path:
                return None
            ext = file_path.lower()
            if ext.endswith("/") or ext.endswith("\\"):
                return None
            if "." in ext:
                ext = "." + ext.split(".")[-1].lower() if not ext.startswith(".") else ext.lower()
        else:
            return None

        if not ext.startswith("."):
            ext = "." + ext

        return cls._handlers.get(ext)

    @classmethod
    def get_handler_by_extension(cls, extension: str) -> ILanguageHandler | None:
        ext = extension.lower()
        if not ext.startswith("."):
            ext = "." + ext
        return cls._handlers.get(ext)

    @classmethod
    def is_supported(cls, file_path: str | ILanguageHandler) -> bool:
        return cls.get_handler(file_path) is not None

    @classmethod
    def supported_extensions(cls) -> list[str]:
        return list(cls._handlers.keys())

    @classmethod
    def supported_extensions_unique(cls) -> list[str]:
        seen = set()
        extensions = []
        for ext in cls._handlers.keys():
            lower_ext = ext.lower()
            if lower_ext not in seen:
                seen.add(lower_ext)
                extensions.append(lower_ext)
        return sorted(extensions)


LanguageFactory.register(PythonHandler())
LanguageFactory.register(RustHandler())
LanguageFactory.register(JavaHandler())
LanguageFactory.register(GoHandler())
