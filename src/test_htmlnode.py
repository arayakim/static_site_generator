import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_is_none(self):
        node = HTMLNode()
        self.assertIsNone(node.props)

    def test_props_is_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_has_attributes(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank"
        })
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )

if __name__ == "__main__":
    unittest.main()
