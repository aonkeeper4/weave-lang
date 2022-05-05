from parser import SyntaxNode


class ActionNode(SyntaxNode):

    def __init__(self, type, val, subnodes, types):
        super().__init__(type, val, subnodes)
        pass

    # generate method?


def contextify(ast):
    pass
    return action_tree  # is ast with context
