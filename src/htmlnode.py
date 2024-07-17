class HTMLNode:
    def __init__(self, tag, value, children, props):
        """
            tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
            An HTMLNode without a tag will just render as raw text

            value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
            An HTMLNode without a value will be assumed to have children

            children - A list of HTMLNode objects representing the children of this node
            An HTMLNode without children will be assumed to have a value

            props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag)
            An HTMLNode without props simply won't have any attributes

        """

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        prop_str = ""
        for key, value in self.props.items():
            prop_str += f' {key}="{value}"'
        return prop_str

    def __repr__(self):
        return (
            f"""HTMLNode(
                tag:{self.tag}
                value:{self.value}
                children:{self.children}
                props:{self.props}
            )
            """
        )
    
    def __eq__(self, node):
        return self.tag == node.tag and self.value == node.value and self.children == node.children and self.props == node.props

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("No leaf node value.")
        super().__init__(tag, value, [], props)
    
    def to_html(self):
        if not self.tag:
            return self.value

        if self.props:
            props_str = self.props_to_html()
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
        
        return f"<{self.tag}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if tag is None:
            raise ValueError("No tag provided.")
        if children is None or not children:
            raise ValueError("No child elements.")
            
        super().__init__(tag, None, children, props)

    def to_html(self):
        html = f"<{self.tag}{self.props_to_html() if self.props else ''}>"
        for child in self.children:
            html += child.to_html()
        return html + f"</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode(tag:{self.tag}, children:{self.children}, props:{self.props})"

    
    