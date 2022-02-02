import string
import re

def lexer(src):
    identifier = r"\b[a-zA-Z_]+\d*[a-zA-Z_]* 
    number = r"\d+\.?\d*"
    ops = ["and", "or", "not", "xor", "in", # i couldnt you the logic behind the ordering of these
        "<-", ">=", "<=",
        ":", "|", "(", ")", "\[", "\]", "<", ">", "=", "\+", "-", "\*", "/", "%", "!", "\"", "'"
    ]
    operator = r"|".join(ops)
    kws = ["if", "for", "do", "end", "return", "int", "float", "str", "bool", "function"]
    keyword = r"|".join(ops)

    tokens_spec = [
        ("ID", identifier),
        ("NUM", number),
        ("OP", operator),
        ("KW", keyword)
        ("NEWL", newline)
    ]
    
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in tokens_spec)
    for item in re.finditer(token_regex, src):
        pass
    
    pass
    return tokens

# def tokenize(code):
#     keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
#     token_specification = [
#         ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
#         ('ASSIGN',   r':='),           # Assignment operator
#         ('END',      r';'),            # Statement terminator
#         ('ID',       r'[A-Za-z]+'),    # Identifiers
#         ('OP',       r'[+\-*/]'),      # Arithmetic operators
#         ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
#         ('MISMATCH', r'.'),            # Any other character
#     ]
#     tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
#     line_num = 1
#     line_start = 0
#     for mo in re.finditer(tok_regex, code):
#         kind = mo.lastgroup
#         value = mo.group()
#         column = mo.start() - line_start
#         if kind == 'NUMBER':
#             value = float(value) if '.' in value else int(value)
#         elif kind == 'ID' and value in keywords:
#             kind = value
#         elif kind == 'NEWLINE':
#             line_start = mo.end()
#             line_num += 1
#             continue
#         elif kind == 'SKIP':
#             continue
#         elif kind == 'MISMATCH':
#             raise RuntimeError(f'{value!r} unexpected on line {line_num}')
#         yield Token(kind, value, line_num, column)