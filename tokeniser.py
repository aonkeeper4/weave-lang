#made by muffn :D
class TokenType:
    Identifier=0
    Number=1
    Punctuation=2
    String=3
    Space=4

class Token:
    def __init__(self,type,value):
        self.type=type
        self.value=value


tokentests=[
    [TokenType.Number,lambda x:x.isdigit()],
    [TokenType.Punctuation,lambda x:x in ['.','<','>',';','/','+','-','*']],
    [TokenType.Space,lambda x:x.isspace()]
]

def determineToken(c):
    for test in tokentests:
        if (test[1](c)):
            print("Found test",test[0],":",c)
            return test[0]
    return TokenType.Identifier

def tokenise(prgm):
    tokl=[]
    tokstr=''
    pt=None
    pc=''
    prevc=''
    instr=False;
    for c in prgm:
        if c=='"':
            instr=not instr
            if (instr):
                tokl.append(Token(TokenType.String,tokstr))
                tokstr=''
            else:
                tokl.append(Token(pt,tokstr))
                tokstr=''
        else:
            if not instr:
                t=determineToken(c);
                if ((t!=pt or t==TokenType.Punctuation)and not(pt==TokenType.Identifier and t==TokenType.Number)and not(
                    #special use case double punctuation
                    ((pc=='*')and(c=='*')) or
                    ((pc=='/')and(c=='/')) or
                    ((pc=='=')and(c=='='))
                )):
                    tokl.append(Token(pt,tokstr))
                    tokstr=''
                    pt=t;
            tokstr+=c
            #:D
        prevc=c;
    return tokl

def test():
    totok='void test() == 123 int32'
    for i in tokenise(totok):
        print(i.type,":",i.value)
test()