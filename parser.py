from lexer import lexer

def parser(tokens):
    pass

if __name__ == "__main__":
    with open("test programs/big test.weave", "r") as f:
        tokens = lexer(f.read())
        parser(tokens)

