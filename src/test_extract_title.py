import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_no_title(self):
        markdown = "This is a markdown text with no title"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_title_at_start(self):
        markdown = "# Welcome to My Website\n\nBody content here."
        result = extract_title(markdown)
        expected = "Welcome to My Website"
        self.assertEqual(result, expected)

    def test_with_intro_text(self):
        markdown = "Some introductory text\n\n# My First Blog Post\n\nMore content here."
        result = extract_title(markdown)
        expected = "My First Blog Post"
        self.assertEqual(result, expected)

    def test_subtitle_no_title(self):
        markdown = "## This is a subtitle, not a title"
        with self.assertRaises(Exception):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()
