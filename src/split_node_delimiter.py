from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        if old_node.text.count(delimiter) % 2 != 0:
            raise Exception("invalid Markdown syntax")
        split_nodes = old_node.text.split(delimiter)
        temp_list = []
        for index, node in enumerate(split_nodes):
            if node == "":
                continue
            if index % 2 == 0:
                temp_list.append(TextNode(node, TextType.TEXT))
            else:
                temp_list.append(TextNode(node, text_type))
        new_nodes.extend(temp_list)
    return new_nodes
