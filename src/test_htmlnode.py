import unittest
from htmlnode import HTMLNode, LeafNode

class  TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html_node1 = HTMLNode(tag="h1", 
                            value="Hello There", 
                            children=[], 
                            props={"font":"verdana", "color":"black"})
        prop_str = html_node1.props_to_html()
        self.assertEqual(prop_str, ' font="verdana" color="black"')

class TestLeafNode(unittest.TestCase):
    def test_to_html_no_props(self):
        leaf_node = LeafNode(tag="p",
                            value="Hello World",)
        test_str = f"<p>Hello World</p>"
        self.assertEqual(test_str, leaf_node.to_html())

    def test_to_html_props(self):
        leaf_node = LeafNode(tag="a",
                            value="Hello World",
                            props={"href":"https://www.boot.dev/lessons/ac96cd47-bf01-4599-8291-cd69534f288f", "target":"_blank"})
        test_str = f'<a href="https://www.boot.dev/lessons/ac96cd47-bf01-4599-8291-cd69534f288f" target="_blank">Hello World</a>'
        self.assertEqual(test_str, leaf_node.to_html())

    def test_leaf_exception(self):
        with self.assertRaises(ValueError):
            LeafNode()

        with self.assertRaises(ValueError):
            LeafNode(tag="p")

        with self.assertRaises(ValueError):
            LeafNode(props={"style":"text-align:right"})


if __name__ == "__main__":
    unittest.main()