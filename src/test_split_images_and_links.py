import unittest
from textnode import TextNode, TextType
from split_images_and_links import split_nodes_image, split_nodes_link


class TestSplitNodes(unittest.TestCase):

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](image.png) and another ![second](second.png)",
            TextType.TEXT,
        )
        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "image.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second", TextType.IMAGE, "second.png"),
            ],
        )

    def test_split_image_at_start(self):
        node = TextNode("![cat](cat.png) is here", TextType.TEXT)
        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode("cat", TextType.IMAGE, "cat.png"),
                TextNode(" is here", TextType.TEXT),
            ],
        )

    def test_split_image_at_end(self):
        node = TextNode("Look at this ![cat](cat.png)", TextType.TEXT)
        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode("Look at this ", TextType.TEXT),
                TextNode("cat", TextType.IMAGE, "cat.png"),
            ],
        )

    def test_no_images(self):
        node = TextNode("Just ordinary text", TextType.TEXT)
        self.assertEqual(split_nodes_image([node]), [node])

    def test_preserve_non_text_node(self):
        node = TextNode("already an image", TextType.IMAGE, "cat.png")
        self.assertEqual(split_nodes_image([node]), [node])

    def test_split_links(self):
        node = TextNode(
            "Visit [Boot.dev](https://boot.dev) and [YouTube](https://youtube.com)",
            TextType.TEXT,
        )
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode("Visit ", TextType.TEXT),
                TextNode("Boot.dev", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("YouTube", TextType.LINK, "https://youtube.com"),
            ],
        )

    def test_split_link_at_start(self):
        node = TextNode("[Boot.dev](https://boot.dev) is useful", TextType.TEXT)
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode("Boot.dev", TextType.LINK, "https://boot.dev"),
                TextNode(" is useful", TextType.TEXT),
            ],
        )

    def test_split_link_at_end(self):
        node = TextNode("Visit [Boot.dev](https://boot.dev)", TextType.TEXT)
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode("Visit ", TextType.TEXT),
                TextNode("Boot.dev", TextType.LINK, "https://boot.dev"),
            ],
        )

    def test_no_links(self):
        node = TextNode("Just ordinary text", TextType.TEXT)
        self.assertEqual(split_nodes_link([node]), [node])

    def test_preserve_non_text_link_node(self):
        node = TextNode("already a link", TextType.LINK, "https://boot.dev")
        self.assertEqual(split_nodes_link([node]), [node])


if __name__ == "__main__":
    unittest.main()
