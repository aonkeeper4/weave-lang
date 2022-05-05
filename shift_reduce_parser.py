# TODO: implement shift-reduce parser

grammar = {
    'id': 'S',
    'S+S': 'S',
    '_S_': '$'
}

input_buffer = '_id+id+id_'
stack = ''

def shift():
    global stack, input_buffer
    stack += input_buffer[0]
    input_buffer = input_buffer[1:]

def accept():
    return stack == '$'

while not accept():
    shift()
    print("SHIFT")
    print(stack)
    for key, val in grammar.items():
        if stack[-len(key):] == key:
            stack = stack[:-len(key)] + val
            print(f"REDUCE by {key} -> {val}")
            print(stack)

print("ACCEPT")