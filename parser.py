from lexer import lexer

def parser(token_gen):

    while True:
        token_cache = []
        match = False
        while not match:
            current = next(token_gen)
            token_cache.append(current)
            match = match_grammar(token_cache)


if __name__ == "__main__":
    with open("test programs/big test.weave", "r") as f:
        token_gen = lexer(f.read())
        parser(tokens)

