import lexer, parser, contextify, generate
import sys, os

def compile(src_file, out_file):
    with open(src_file, "r") as f:
        src = f.read()

    tokens = lexer.lexer(src)
    ast = parser.parser(tokens)
    action_tree = contextify.contextify(ast)
    urcl_src = generate.generate(action_tree)

    with open(out_file, "w") as f:
        f.write(urcl_src)

if __name__ == "__main__":
    compile(sys.argv[1], "out.c")
    os.system("gcc out.c -o out")
    os.system("out.exe")