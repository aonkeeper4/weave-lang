import string
import re

# lexer is such a cool word honestly
def lexer(src):
    # remove comments
    lines = src.split("\n")
    src = []
    for line in lines:
        if ";;" in line: # line contains comment
            line = line[:line.find(";;")] # remove comment
        src.append(line)
    src = "\n".join(src)

    tokens = []

    # regexes for language components
    word_ops = ["and", "or", "not", "xor", "in"] # operators that are words are handled differently
    ops = ["<-", ">=", "<=", ":", "\|", "\(", "\)", "\[", "\]", "<", ">", "=", "\+", "-", "\*", "/", "%", "!", ","] # other operators

    word_ops = [rf"\b{op}\b" for op in word_ops] # processing for word operators
    operator = r"|".join(word_ops + ops) # combined regex for operators

    kws = ["if", "for", "do", "end", "return", "int", "float", "str", "bool", "function", "of", "arr", "none"]
    keyword = r"|".join(kws) # combined regex for keywords

    tokens_spec = [ # spent almost an hour debugging something before realising the order of these mattered
        ("STR", r"(\".*\")|('.*')"), # string (any sequence of characters enclosed in quotes)
        ("OP", operator),
        ("KW", keyword),
        ("NUM", r"\d+\.?\d*"), # number: int/float
        ("ID", r"\b[a-zA-Z_]+\d*[a-zA-Z_]*"), # ids
        ("NEWL", r"\n"), # for line counting / statement termination
        ("SPACE", r"\s"),
        ("BAD", r".")
    ]
    
    # YOO WELCOME TO THE BLACK PARADE BY GLASS BEACH IS PLAYING
    # VIBING RN
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in tokens_spec) # creates master regex with groups that have ids of the specific language features they match

    line = 1 # track lines for error msg
    line_start = 0 # track col
    for item in re.finditer(token_regex, src):
        # type and value of match
        t_type = item.lastgroup
        t_value = item.group()

        col = item.start() - line_start
        
        match [t_type, t_value]:
            case ["NUMBER", _]:
                t_value = float(t_value) if '.' in t_value else int(t_value) # get value of number
            case ["SPACE", _]:
                continue
            case ["NEWL", _]:
                line += 1
                line_start = item.end()
                t_value = "" # we dont need that
            case ["BAD", _]:
                raise SyntaxError(f"bad character {t_value} at line {line} col {col+1}")

        print("DEBUG:", t_type, t_value)
        tokens.append((t_type, t_value))

    return tokens

if __name__ == "__main__":
    with open("test programs/big test.weave", "r") as f: # just for test
        lexer(f.read())