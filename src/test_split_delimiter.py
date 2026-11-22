import unittest
from split_node_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitDelimiter(unittest.TestCase):
    def test_basic_split(self):
        node = TextNode("This is **bold** text", TextType.TEXT)

        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_entire_string_formatted(self):
        node = TextNode("**This whole sentence is bold**", TextType.TEXT)

        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected = [
            TextNode("This whole sentence is bold", TextType.BOLD)
        ]

        self.assertEqual(result, expected)

    def test_multiple_formatted_sections(self):
        node = TextNode("**bold** and **more bold**", TextType.TEXT)

        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("more bold", TextType.BOLD),
        ]

        self.assertEqual(result, expected)

    def test_no_delimiters(self):
        node = TextNode("This is plain text", TextType.TEXT)

        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected = [
            TextNode("This is plain text", TextType.TEXT)
        ]

        self.assertEqual(result, expected)

    def test_non_text_nodes(self):
        nodes = [
            TextNode("bold", TextType.BOLD),
            TextNode("italic", TextType.ITALIC),
            TextNode("code", TextType.CODE),
        ]

        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)

        self.assertEqual(result, nodes)

    def test_unmatched_delimiter(self):
        node = TextNode("This is **bold text", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_delimiter_at_beginning(self):
        node = TextNode("**bold** text", TextType.TEXT)

        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)


    def test_delimiter_at_end(self):
        node = TextNode("text **bold**", TextType.TEXT)

        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected = [
            TextNode("text ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
        ]

        self.assertEqual(result, expected)

    def test_italic_delimiter(self):
        node = TextNode("This is _italic_ text", TextType.TEXT)

        result = split_nodes_delimiter([node], "_", TextType.ITALIC)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)


    def test_code_delimiter(self):
        node = TextNode("This is `code` text", TextType.TEXT)

        result = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_multiple_old_nodes(self):
        nodes = [
            TextNode("This is **bold**", TextType.TEXT),
            TextNode("This is plain text", TextType.TEXT),
            TextNode("Another **bold**", TextType.TEXT),
        ]

        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode("This is plain text", TextType.TEXT),
            TextNode("Another ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
        ]

        self.assertEqual(result, expected)

    def test_successive_passes(self):
        node = TextNode("This is **bold** and `code`", TextType.TEXT)

        bold_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        result = split_nodes_delimiter(bold_nodes, "`", TextType.CODE)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ]

        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
