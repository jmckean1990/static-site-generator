from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    # text_node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # text_node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # html_node1 = HTMLNode("p", "Hello World", [], {"color":"red", "text-size":"5em"})
    # leaf_node = LeafNode(tag="a",
    #                         value="Hello World",
    #                         props={"href":"https://www.boot.dev/lessons/ac96cd47-bf01-4599-8291-cd69534f288f", "target":"_blank"})
    # # print(text_node1)
    # # print(text_node1 == text_node2)

    # print(html_node1)
    # print(html_node1.props_to_html())
    # print(leaf_node.to_html())
    html_node1 = HTMLNode("p", "Hello World", [], {"color":"red", "text-size":"5em"})
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            ParentNode("div", [LeafNode("p", "lorem ipsum"), LeafNode(None, "Some text in this inner div"), ParentNode("div", [LeafNode("p", "lorem ipsum2"), LeafNode("p", "lorem ipsum3")], {"prop-val":"val"})]),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text", {"font-size":"3em"}),
            LeafNode(None, "Normal text"),
        ],
        {"color":"red", "text-size":"5em"}
    )
    # print(node.to_html())
    print(node)


if __name__ == "__main__":
    main()
