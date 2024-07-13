import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):
    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        parent_html = node.to_html()
        test_str = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(test_str, parent_html)

    def test_nested_parents(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                ParentNode("div", [LeafNode("span", "Span text"), LeafNode("p", "lorem ipsum 1")]),
                ParentNode("div", [ParentNode("div", [LeafNode(None, "Double nested normal text")])]),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        parent_html = node.to_html()
        test_str = "<p><b>Bold text</b><div><span>Span text</span><p>lorem ipsum 1</p></div><div><div>Double nested normal text</div></div><i>italic text</i>Normal text</p>"
        self.assertEqual(test_str, parent_html)

    def test_parent_props(self):
        node = ParentNode(
            "p",
            [LeafNode("i", "italic text"), LeafNode(None, "Normal text")],
            {"style":"text-size:2px;"}
        )

        test_str = '<p style="text-size:2px;"><i>italic text</i>Normal text</p>'
        parent_html = node.to_html()
        self.assertEqual(test_str, parent_html)

    def test_inner_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                ParentNode("div", [LeafNode("span", "Span text"), LeafNode("p", "lorem ipsum 1")]),
                ParentNode("div", [ParentNode("div", [LeafNode(None, "Double nested normal text")], {"style":"margin:5px;"})]),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        parent_html = node.to_html()
        test_str = '<p><b>Bold text</b><div><span>Span text</span><p>lorem ipsum 1</p></div><div><div style="margin:5px;">Double nested normal text</div></div><i>italic text</i>Normal text</p>'
        self.assertEqual(test_str, parent_html)

    def test_parent_exceptions(self):
        with self.assertRaises(ValueError):
            ParentNode()
        
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode(None, "Text")])

        with self.assertRaises(ValueError):
            ParentNode("p", [])

    def test_assert_text(self):
        try:
            ParentNode(None, [LeafNode(None, "Text")])
        except ValueError as e:
            self.assertEqual("No tag provided.", str(e))

        try:
            ParentNode("p", [])
        except ValueError as e:
            self.assertEqual("No child elements.", str(e))

if __name__ == "__main__":
    unittest.main()