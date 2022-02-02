import string
import re

def lexer(src):
    lines = src.split("\n")
    src = "\n".join([line for line in lines if not line.startswith(";;")])

    tokens = []

    identifier = r"\b[a-zA-Z_]+\d*[a-zA-Z_]*"
    number = r"\d+\.?\d*"
    word_ops = ["and", "or", "not", "xor", "in"] # i couldnt you the logic behind the ordering of these
    ops = ["<-", ">=", "<=", ":", "\|", "\(", "\)", "\[", "\]", "<", ">", "=", "\+", "-", "\*", "/", "%", "!", "\"", "'"
    ]
    operator = r"|".join([rf"\b{op}\b" for op in word_ops]+ops)
    kws = ["if", "for", "do", "end", "return", "int", "float", "str", "bool", "function", "of", "arr", "none"]
    keyword = r"|".join(kws)

    tokens_spec = [
        ("OP", operator),
        ("KW", keyword),
        ("NUM", number),
        ("ID", identifier),
        ("SPACE", r"\W"),
        ("BAD", r".")
    ]
    
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in tokens_spec)
    for item in re.finditer(token_regex, src):
        t_type = item.lastgroup
        t_value = item.group()
        
        match t_type:
            case "NUMBER":
                t_value = float(value) if '.' in t_value else int(value)
            case "SPACE":
                continue
            case "BAD":
                raise RuntimeError("boi you did a naughty")
        
        print(t_type, t_value)
        tokens.append((t_type, t_value))
    
    pass
    return tokens

with open("test programs/big test.weave", "r") as f:
    lexer(f.read())