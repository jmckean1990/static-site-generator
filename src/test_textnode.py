import unittest
from textnode import TextNode
from htmlnode import LeafNode
from node_utils import text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_none(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.url, None)

    def test_text_conversion(self):
        text_node = TextNode("Some text", "text")
        test_leaf = LeafNode(None, "Some text")
        self.assertEqual(test_leaf, text_node_to_html_node(text_node))

    def test_bold_conversion(self):
        text_node = TextNode("bold text", "bold")
        test_leaf = LeafNode("b", "bold text")
        self.assertEqual(test_leaf, text_node_to_html_node(text_node))

    def test_italic_conversion(self):
        text_node = TextNode("italic text", "italic")
        test_leaf = LeafNode("i", "italic text")
        self.assertEqual(test_leaf, text_node_to_html_node(text_node))
    
    def test_code_conversion(self):
        text_node = TextNode("code text", "code")
        test_leaf = LeafNode("code", "code text")
        self.assertEqual(test_leaf, text_node_to_html_node(text_node))
    
    def test_link_conversion(self):
        text_node = TextNode("link text", "link", "www.google.com")
        test_leaf = LeafNode("a", "link text", {"href":text_node.url})
        self.assertEqual(test_leaf, text_node_to_html_node(text_node))
    
    def test_image_conversion(self):
        text_node = TextNode("link text", "image", "https://letsenhance.io/MainAfter.jpg")
        test_leaf = LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
        self.assertEqual(test_leaf, text_node_to_html_node(text_node))


if __name__ == "__main__":
    unittest.main()