import string
import re

def lexer(src):
    # identifiers, numbers, operators, ???
    identifier = re.compile(r"/\b[a-zA-Z_]+\d*/gm")
    number = re.compile(r"/\d+\.?\d*/gm")
    # operators
    
    pass
    return tokens
