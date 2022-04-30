# TODO: fix

from utils import Token

class AST:
    pass

grammar = {
    ("NUM", "OP", "NUM"): Token("EXPR"),
    ("EXPR", "OP", "EXPR"): Token("END"),
}

class ShiftReduceParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.tree = AST()
    
    def parse(self, data):
        """
        Performs the shift-reduce parsing algorithm.
        """
        stack = []
        input_buffer = data

        def find_sub_list(sl,l):
            sll=len(sl)
            for ind in (i for i,e in enumerate(l) if e==sl[0]):
                if l[ind:ind+sll]==sl:
                    return ind,ind+sll
            return None

        while input_buffer:
            stack += [input_buffer[0]]
            input_buffer = input_buffer[1:]
            for key, value in grammar.items():
                indices = find_sub_list(key, [tok.type for tok in stack])
                if indices is not None:
                    stack[indices[0]:indices[1]] = value
                    print("Stack:", stack)
                    print("Input buffer:", input_buffer)

            
        return stack

parser = ShiftReduceParser(grammar)
print(parser.parse(
    [Token("NUM", 3), Token("OP", "+"), Token("NUM", 3), Token("OP", "+"), Token("NUM", 3)]
))