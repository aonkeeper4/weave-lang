class SyntaxNode:
    def __init__(self, type, val, subnodes):
        self.type = type
        self.val = val
        self.subnodes = subnodes

def parser(tokens):
    tokens = map(lambda token: SyntaxNode(token[0], token[1], []), tokens)
    # build tree top-down?
    # ok but how
    
    pass # ill figure it out later

    return ast
