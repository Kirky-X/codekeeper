"""Tests for Java language handler."""

from codekeeper.languages import JavaHandler


class TestJavaHandler:
    """Tests for JavaHandler class."""

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
