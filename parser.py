from lexer import lexer
# https://www.geeksforgeeks.org/shift-reduce-parser-compiler/?ref=lbp
# bottom up parser

def parser(tokens):
    pass


if __name__ == "__main__":
    with open("test programs/big test.weave", "r") as f:
        tokens = lexer(f.read())
        parser(tokens)

