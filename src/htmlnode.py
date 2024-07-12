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

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if not value:
            raise ValueError("No leaf node value.")
        super().__init__(tag, value, [], props)
    
    def to_html(self):
        if not self.tag:
            return value

        if self.props:
            props_str = self.props_to_html()
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
        
        return f"<{self.tag}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if not tag:
            raise ValueError("No tag provided.")
        if not children:
            raise ValueError("No child elements.")
            
        super().__init__(tag, None, children, props)

    def generate_html(tag, text=None):
        return f"<{tag}>text</{tag}>"
    
    def to_html(self):
        pass

    
    