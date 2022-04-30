import re
from utils import Token

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

    kws = ["if", "for", "do", "end", "return", "int", "float", "str", "bool", "function", "of", "arr", "none", "program"]
    ops = ["<-", "->", ">=", "<=", ":", "\|", "\(", "\)", "\[", "\]", "<", ">", "=", "\+", "-", "\*", "/", "%", "!", ",", "and", "or", "not", "xor", "in"]

    # spent almost an hour debugging something before realising the order of these mattered
    tokens_spec = [
        ("NUM", r"\d+\.?\d*"), # number: int/float
        ("STR", r"(\".*\")|('.*')"), # string (any sequence of characters enclosed in quotes)
        ("ID", r"\b[a-zA-Z_]+\d*[a-zA-Z_]*"), # match ids before ops
        ("KW", r"|".join(kws)), # kw regex
        ("OP", r"|".join(ops)), # op regex
        ("NEWL", r"\n"), # for line counting / statement termination
        ("SPACE", r"\s"),
        ("BAD", r".") # yuh
    ]
    
    # YOO WELCOME TO THE BLACK PARADE BY GLASS BEACH IS PLAYING
    # VIBING RN
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in tokens_spec) # creates master regex with groups that have ids of the specific language features they match

    line = 1 # track lines for error msg
    line_start = 0 # track col for error msg
    for item in re.finditer(token_regex, src):
        # type and value of match
        t_type = item.lastgroup
        t_value = item.group()

        col = item.start() - line_start
        
        match [t_type, t_value]:
            case ["ID", val]:
                if val in kws: # just in case (its probably inefficient but idc)
                    t_type = "KW"
                elif val in ops:
                    t_type = "OP"
            case ["NUMBER", _]:
                t_value = float(t_value) if '.' in t_value else int(t_value) # get value of number
            case ["SPACE", _]:
                continue
            case ["NEWL", _]:
                line += 1
                line_start = item.end()
                t_value = "" # we dont need that
            case ["BAD", _]:
                raise SyntaxError(f"bad character {t_value} at line {line} col {col+1}") # informative yes

        print("DEBUG:", t_type, t_value)
        tokens.append(Token(t_type, t_value))

    return tokens

if __name__ == "__main__":
    with open("test programs/big test.weave", "r") as f: # just for test
        tokens = lexer(f.read())