# TODO: fix
import re

class AST:
    pass

grammar = {
    r"\d": "E",
    r"E[+*-/]E": "E",
    r"^E$": "$"
}

class ShiftReduceParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.tree = AST()
    
    def parse(self, data):
        """
        Performs the shift-reduce parsing algorithm.
        """
        # may need to not cheat in order to get ast to generate properly
        new_data = data
        while new_data != "$":
            for k, v in self.grammar.items():
                new_data = re.sub(k, v, new_data)

        return self.tree

parser = ShiftReduceParser(grammar)
print(parser.parse("3+2+5"))