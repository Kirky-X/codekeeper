"""Tests for TypeScript language handler."""

from codekeeper.languages import TypeScriptHandler


class TestTypeScriptHandler:
    """Tests for TypeScriptHandler class."""

    def test_get_functions(self, sample_typescript_code):
        """Test parsing TypeScript functions."""
        handler = TypeScriptHandler(sample_typescript_code)
        functions = handler.get_functions()

        function_names = [f.name for f in functions]
        assert "standaloneFunction" in function_names
        assert "withCallback" in function_names

    def test_get_classes(self, sample_typescript_code):
        """Test parsing TypeScript classes."""
        handler = TypeScriptHandler(sample_typescript_code)
        classes = handler.get_classes()

        class_names = [c.name for c in classes]
        assert "Calculator" in class_names

    def test_get_interfaces(self, sample_typescript_code):
        """Test parsing TypeScript interfaces."""
        handler = TypeScriptHandler(sample_typescript_code)
        classes = handler.get_classes()

        interface_names = [c.name for c in classes if "interface" in c.decorators]
        assert "CalculatorInterface" in interface_names

    def test_get_types(self, sample_typescript_code):
        """Test parsing TypeScript types."""
        handler = TypeScriptHandler(sample_typescript_code)
        classes = handler.get_classes()

        type_names = [c.name for c in classes if "type" in c.decorators]
        assert "CalculatorState" in type_names

    def test_get_copyright_header(self, sample_typescript_code):
        """Test copyright header detection."""
        handler = TypeScriptHandler(sample_typescript_code)
        header = handler.get_copyright_header()

        assert header is not None

    def test_get_comment_style(self):
        """Test comment style detection."""
        handler = TypeScriptHandler("")
        assert handler.get_comment_style().value == "single_line"

    def test_get_supported_extensions(self):
        """Test supported extensions."""
        assert ".ts" in TypeScriptHandler.SUPPORTED_EXTENSIONS
        assert ".tsx" in TypeScriptHandler.SUPPORTED_EXTENSIONS
        assert ".js" in TypeScriptHandler.SUPPORTED_EXTENSIONS
        assert ".jsx" in TypeScriptHandler.SUPPORTED_EXTENSIONS
        assert ".mjs" in TypeScriptHandler.SUPPORTED_EXTENSIONS

    def test_class_methods(self, temp_typescript_file):
        """Test parsing class methods."""
        handler = TypeScriptHandler.from_file(temp_typescript_file)
        classes = handler.get_classes()

        assert len(classes) >= 1
        calculator_class = next((c for c in classes if c.name == "Calculator"), None)
        assert calculator_class is not None
        method_names = [m.name for m in calculator_class.methods]
        assert "add" in method_names
        assert "subtract" in method_names
        assert "getValue" in method_names

    def test_async_function(self, sample_typescript_code):
        """Test parsing async functions."""
        handler = TypeScriptHandler(sample_typescript_code)
        functions = handler.get_functions()

        async_functions = [f for f in functions if "async" in f.decorators]
        assert len(async_functions) >= 1

    def test_function_with_params(self, sample_typescript_code):
        """Test function parameter parsing."""
        handler = TypeScriptHandler(sample_typescript_code)
        functions = handler.get_functions()

        standalone_func = next((f for f in functions if f.name == "standaloneFunction"), None)
        assert standalone_func is not None
        assert len(standalone_func.parameters) == 0

        callback_func = next((f for f in functions if f.name == "withCallback"), None)
        assert callback_func is not None
        assert len(callback_func.parameters) == 1

    def test_return_type_parsing(self, sample_typescript_code):
        """Test return type extraction."""
        handler = TypeScriptHandler(sample_typescript_code)
        functions = handler.get_functions()

        standalone_func = next((f for f in functions if f.name == "standaloneFunction"), None)
        assert standalone_func is not None
        assert standalone_func.return_type is not None
        assert "string" in standalone_func.return_type

    def test_empty_content(self):
        """Test handling empty content."""
        handler = TypeScriptHandler("")
        functions = handler.get_functions()
        classes = handler.get_classes()

        assert functions == []
        assert classes == []

    def test_parse_from_file(self, temp_typescript_file):
        """Test parsing from file."""
        handler = TypeScriptHandler.from_file(temp_typescript_file)
        functions = handler.get_functions()
        classes = handler.get_classes()

        assert len(functions) >= 1
        assert len(classes) >= 1

    def test_extensions_property(self):
        """Test extensions property."""
        handler = TypeScriptHandler("")
        assert handler.extensions == TypeScriptHandler.SUPPORTED_EXTENSIONS
