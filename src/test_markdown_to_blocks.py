import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkDownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_file(self):
        with open("markdown_test_file.md", "r") as file:
            md = file.read()

        result = markdown_to_blocks(md)

        expected = [
            "# My Static Website",
            "This is a paragraph with some **bold text** and _italic text_.",
            "This is another paragraph with `inline code` inside it.\nThis sentence belongs to the same paragraph.",
            "- First list item\n- Second list item\n- Third list item",
            "## Learning Python",
            "Python is a programming language.",
            "It supports:\n- Variables\n- Functions\n- Classes",
            "This is the final paragraph."
        ]

        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
