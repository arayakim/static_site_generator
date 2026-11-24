from blocktype import block_to_block_type, BlockType
from markdown_to_blocks import markdown_to_blocks
from textnode import text_node_to_html_node, TextNode, TextType
from text_to_textnodes import text_to_textnodes
from htmlnode import ParentNode

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    children = []
    for textnode in textnodes:
        child = text_node_to_html_node(textnode)
        children.append(child)
    return children

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        blocktype = block_to_block_type(block)

        if blocktype == BlockType.HEADING:
            heading_level = 0
            while heading_level < len(block) and block[heading_level] == "#":
                heading_level += 1

            heading_text = block[heading_level + 1:]
            children = text_to_children(heading_text)

            heading_node = ParentNode(tag=f"h{heading_level}", children=children)
            html_nodes.append(heading_node)

        elif blocktype == BlockType.PARAGRAPH:
            paragraph_text = block.replace("\n", " ")
            children = text_to_children(paragraph_text)

            paragraph_node = ParentNode(tag="p", children=children)
            html_nodes.append(paragraph_node)

        elif blocktype == BlockType.CODE:
            lines = block.split("\n")
            code_text = "\n".join(lines[1:-1]) + "\n"
            code_text_node = TextNode(code_text, TextType.TEXT)
            code_node = text_node_to_html_node(code_text_node)
            code_parent = ParentNode(tag="code", children=[code_node])
            pre_parent = ParentNode(tag="pre", children=[code_parent])
            html_nodes.append(pre_parent)

        elif blocktype == BlockType.QUOTE:
            lines = block.split("\n")
            quote_lines = []

            for line in lines:
                quote_lines.append(line.lstrip("> "))

            quote_text = " ".join(quote_lines)
            children = text_to_children(quote_text)

            quote_node = ParentNode(tag="blockquote", children=children)
            html_nodes.append(quote_node)

        elif blocktype == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            list_items = []

            for line in lines:
                item_text = line[2:]
                children = text_to_children(item_text)
                list_item = ParentNode(tag="li", children=children)
                list_items.append(list_item)

            unordered_list = ParentNode(tag="ul", children=list_items)
            html_nodes.append(unordered_list)

        elif blocktype == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            list_items = []

            for line in lines:
                item_text = line.split(". ", 1)[1]
                children = text_to_children(item_text)
                list_item = ParentNode(tag="li", children=children)
                list_items.append(list_item)

            ordered_list = ParentNode(tag="ol", children=list_items)
            html_nodes.append(ordered_list)

    return ParentNode(tag="div", children=html_nodes)
