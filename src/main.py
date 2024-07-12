from textnode import TextNode
from htmlnode import HTMLNode, LeafNode

def main():
    text_node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    text_node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    html_node1 = HTMLNode("p", "Hello World", [], {"color":"red", "text-size":"5em"})
    leaf_node = LeafNode(tag="a",
                            value="Hello World",
                            props={"href":"https://www.boot.dev/lessons/ac96cd47-bf01-4599-8291-cd69534f288f", "target":"_blank"})
    # print(text_node1)
    # print(text_node1 == text_node2)

    print(html_node1)
    print(html_node1.props_to_html())
    print(leaf_node.to_html())


if __name__ == "__main__":
    main()
