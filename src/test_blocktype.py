import unittest
from blocktype import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block = "### Heading"

        result = block_to_block_type(block)

        expected = BlockType.HEADING

        self.assertEqual(result, expected)

    def test_code(self):
        block = '```\nprint("Hello")\n```'

        result = block_to_block_type(block)

        expected = BlockType.CODE

        self.assertEqual(result, expected)

    def test_quote(self):
        block = "> First line\n> Second line"

        result = block_to_block_type(block)

        expected = BlockType.QUOTE

        self.assertEqual(result, expected)

    def test_unordered_list(self):
        block = "- Apple\n- Orange"

        result = block_to_block_type(block)

        expected = BlockType.UNORDERED_LIST

        self.assertEqual(result, expected)

    def test_ordered_list(self):
        block = "1. Apple\n2. Orange"

        result = block_to_block_type(block)

        expected = BlockType.ORDERED_LIST

        self.assertEqual(result, expected)

    def test_regular_paragraph(self):
        block = "Regular paragraph"

        result = block_to_block_type(block)

        expected = BlockType.PARAGRAPH

        self.assertEqual(result, expected)


    def test_sequential_increment_ordered_list(self):
        block = "1. Apple\n3. Orange"

        result = block_to_block_type(block)

        expected = BlockType.PARAGRAPH

        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
