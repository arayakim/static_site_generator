import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_all_five_node_types(self):
        text = "Hello **world**, _how_ are you? `print()` ![cat](cat.png) [click here](example.com)"

        result = text_to_textnodes(text)

        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode(", ", TextType.TEXT),
            TextNode("how", TextType.ITALIC),
            TextNode(" are you? ", TextType.TEXT),
            TextNode("print()", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("cat", TextType.IMAGE, "cat.png"),
            TextNode(" ", TextType.TEXT),
            TextNode("click here", TextType.LINK, "example.com"),
        ]

        self.assertEqual(result, expected)

    def test_plain_text_no_markdown(self):
        text = "Just a regular sentence with no formatting."

        result = text_to_textnodes(text)

        expected = [
            TextNode("Just a regular sentence with no formatting.", TextType.TEXT)
        ]

        self.assertEqual(result, expected)

    def test_empty_string(self):
        text = ""

        result = text_to_textnodes(text)

        expected = [
            TextNode("", TextType.TEXT)
        ]

        self.assertEqual(result, expected)

    def test_multi_same_type(self):
        text = "This is **bold** and this is **also bold**."

        result = text_to_textnodes(text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and this is ", TextType.TEXT),
            TextNode("also bold", TextType.BOLD),
            TextNode(".", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
