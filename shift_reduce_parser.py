from utils import Token


class Rule:

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs


class ShiftReduceParser:

    def __init__(self, grammar, input_buffer, stack=None):
        self.grammar = grammar
        self.input_buffer = input_buffer
        if stack is None:
            self.stack = list()

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
                if key == self.stack[-len(key):]:
                    self.stack = self.stack[:-len(key)] + [val]
                    print(f"REDUCE by {key} -> {val}")
                    print(self.stack)

        print("ACCEPT")


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
    parser.parse()
