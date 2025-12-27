"""Tests for Go language handler."""

from codekeeper.languages import GoHandler


class TestGoHandler:
    """Tests for GoHandler class."""

    def test_get_functions(self, sample_go_code):
        """Test parsing Go functions."""
        handler = GoHandler(sample_go_code)
        functions = handler.get_functions()

        function_names = [f.name for f in functions]
        assert "NewCalculator" in function_names
        assert "standaloneFunction" in function_names

    def test_get_classes(self, sample_go_code):
        """Test parsing Go structs."""
        handler = GoHandler(sample_go_code)
        classes = handler.get_classes()

        class_names = [c.name for c in classes]
        assert "Calculator" in class_names

    def test_get_copyright_header(self, sample_go_code):
        """Test copyright header detection."""
        handler = GoHandler(sample_go_code)
        header = handler.get_copyright_header()

        assert header is not None

    def test_get_comment_style(self):
        """Test comment style detection."""
        handler = GoHandler("")
        assert handler.get_comment_style().value == "single_line"

    def test_get_supported_extensions(self):
        """Test supported extensions."""
        assert ".go" in GoHandler.SUPPORTED_EXTENSIONS

    def test_receiver_methods(self, temp_go_file):
        """Test parsing receiver methods."""
        handler = GoHandler.from_file(temp_go_file)
        functions = handler.get_functions()

        assert len(functions) >= 2
        assert any(f.name == "Add" for f in functions)

    def test_struct_and_methods(self, temp_go_file):
        """Test parsing struct and methods."""
        handler = GoHandler.from_file(temp_go_file)
        classes = handler.get_classes()

        assert len(classes) >= 1
        assert any(c.name == "Calculator" for c in classes)
