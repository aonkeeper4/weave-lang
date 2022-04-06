from lexer import lexer
# https://www.geeksforgeeks.org/shift-reduce-parser-compiler/?ref=lbp
# bottom up parser

def parser(tokens):

    while True:
        token_cache = []
        match = False
        while not match:
            current = next(token_gen)
            token_cache.append(current)
            match = match_grammar(token_cache)


if __name__ == "__main__":
    with open("test programs/big test.weave", "r") as f:
        tokens = lexer(f.read())
        parser(tokens)

