# TODO: implement shift-reduce parser

grammar = {
    'S': ['E'],
    'E': ['E', '+', 'T'],
    'E': ['T'],
    'T': ['T', '*', 'F'],
    'T': ['F'],
    'F': ['(', 'E', ')'],
    'F': ['id']
}