from utils import Token


class Rule:

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs


class ASTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add(self, top, sub, *, _dir=0):
        # add a new node to the top in the direction
        if _dir == 0: # left
            node = ASTNode(top, self, sub)
        elif _dir == 1:
            node = ASTNode(top, sub, self)
        
        return node

    def __str__(self, level=0):
        print('\t' * level + repr(self.value))
        for child in self.left, self.right:
            if isinstance(child, ASTNode):
                child.other_name(level+1)
            else:
                print('\t' * (level+1) + str(child))

    def __repr__(self):
        return self.__str__()
        

class ShiftReduceParser:

    def __init__(self, grammar, input_buffer, stack=None):
        self.grammar = grammar
        self.input_buffer = input_buffer
        if stack is None:
            self.stack = list()
        self.ast = None

    def shift(self):
        self.stack += [self.input_buffer[0]]
        self.input_buffer = self.input_buffer[1:]

    def accept(self):
        return self.stack == [Token("STOP")]

    def parse(self):
        while not self.accept():
            self.shift()
            print("SHIFT")
            print(self.stack)
            for rule in self.grammar:
                key = rule.lhs
                val = rule.rhs
                prev = self.stack[-len(key):]
                if key == prev:
                    self.stack = self.stack[:-len(key)] + [val]
                    if self.ast is None:
                        
                        self.ast = ASTNode(*prev)
                    else:
                        try:
                            self.ast.add(prev[1], prev[2], _dir=0)
                        except IndexError:
                            self.ast.add(ASTNode(*prev), None, _dir=0)
                    print(f"REDUCE by {key} -> {val}")
                    print(self.stack)

        print("ACCEPT")
        return self.ast


if __name__ == "__main__":
    shift_reduce_grammar = [
        Rule([Token("ID")], Token("S")),
        Rule([Token("NUM")], Token("S")),
        Rule([Token("S"), Token("OP"), Token("S")], Token("S")),
        Rule([Token("PARSE_START"),
              Token("S"), Token("PARSE_END")], Token("STOP")),
    ]
    input_buffer = [
        Token('PARSE_START'),
        Token('NUM', '7'),
        Token('OP', '+'),
        Token('ID', 'id'),
        Token('OP', '*'),
        Token('NUM', 32),
        Token('PARSE_END')
    ]

    parser = ShiftReduceParser(shift_reduce_grammar, input_buffer)
    ast = parser.parse()
    print(ast)
