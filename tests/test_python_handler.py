"""Tests for Python language handler."""

from codekeeper.languages import PythonHandler


class TestPythonHandler:
    """Tests for PythonHandler class."""

    def test_get_functions(self, sample_python_code):
        """Test parsing Python functions."""
        handler = PythonHandler(sample_python_code)
        functions = handler.get_functions()

        function_names = [f.name for f in functions]
        assert "hello_world" in function_names
        assert "add" in function_names

    def test_get_classes(self, sample_python_code):
        """Test parsing Python classes."""
        handler = PythonHandler(sample_python_code)
        classes = handler.get_classes()

        class_names = [c.name for c in classes]
        assert "Calculator" in class_names

    def test_get_copyright_header(self, sample_python_code):
        """Test copyright header detection."""
        handler = PythonHandler(sample_python_code)
        header = handler.get_copyright_header()

        assert header is not None
        assert isinstance(header, dict)

    def test_get_comment_style(self):
        """Test comment style detection."""
        handler = PythonHandler("")
        assert handler.get_comment_style().value == "single_line"

    def test_get_supported_extensions(self):
        """Test supported extensions."""
        assert ".py" in PythonHandler.SUPPORTED_EXTENSIONS
        assert ".pyw" in PythonHandler.SUPPORTED_EXTENSIONS

    def test_functions_with_annotations(self, temp_python_file):
        """Test parsing functions with type annotations."""
        handler = PythonHandler.from_file(temp_python_file)
        functions = handler.get_functions()

        assert len(functions) >= 2

    def test_classes_with_annotations(self, temp_python_file):
        """Test parsing classes with type annotations."""
        handler = PythonHandler.from_file(temp_python_file)
        classes = handler.get_classes()

        assert len(classes) >= 1
        assert any(c.name == "Calculator" for c in classes)
