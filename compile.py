import lexer, parser, contextify, generate
import sys, os

def compile_weave(src_file, out_file):
    if not out_file.endswith(".c"):
        raise ValueError("output must be C source file")

    out_name = out_file[:2]

    with open(src_file, "r") as f:
        src = f.read()

    tokens = lexer.lexer(src)
    ast = parser.parser(tokens)
    action_tree = contextify.contextify(ast)
    c_src = generate.generate(action_tree)

    with open(out_file, "w") as f:
        f.write(c_src)

    # compile and run outputted c with gcc
    os.system(f"gcc {out_file} -o {out_name}")
    os.system(f"{out_name}.exe")

if __name__ == "__main__":
    compile_weave(sys.argv[1], sys.argv[2])