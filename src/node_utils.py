from htmlnode import LeafNode 

def text_node_to_html_node(text_node):
    text_type = text_node.text_type
    leaf_node = None

    if text_type == "text":
        leaf_node = LeafNode(None, text_node.text)
    elif text_type == "bold":
        leaf_node = LeafNode("b", text_node.text)
    elif text_type == "italic":
        leaf_node = LeafNode("i", text_node.text)
    elif text_type == "code":
        leaf_node = LeafNode("code", text_node.text)
    elif text_type == "link":
        leaf_node = LeafNode("a", text_node.text, {"href":text_node.url})
    elif text_type == "image":
        leaf_node = LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
    else:
        raise Exception("Text node type is not valid.")
    
    return leaf_node