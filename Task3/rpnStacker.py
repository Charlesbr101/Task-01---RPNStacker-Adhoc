stack = []
tokens = []
f = open("Calc1.stk", "r")

class Token:
    type = ""
    lexeme = ""

    def __init__(this, type, lexeme):
        this.type = type
        this.lexeme = lexeme

    def __str__(this):
        return "Token [type=" + this.type + ", lexeme=" + this.lexeme + "]"

class Regex:
    @staticmethod
    def isNum(token):
        return token.isnumeric()
    @staticmethod
    def isOP(token):
        return True if token == "*" or token == "/" or token == "-" or token == "+" else False

def scan(source):
    
    f = open(source, "r")
    tokens = []

    for line in [l.rstrip() for l in f.readlines()]:
        if(Regex.isOP(line)):
            if(line == '*'):
                tokens.append(Token("STAR", line))
            elif(line == '/'):
                tokens.append(Token("SLASH", line))
            elif(line == '-'):
                tokens.append(Token("MINUS", line))
            elif(line == '+'):
                tokens.append(Token("PLUS", line))
        elif(Regex.isNum(line)):
            temp = int(line)
            tokens.append(Token("NUM", line))
        else:
            raise Exception("Nao eh possivel converter %s"%line + " para um token valido")

    return tokens;

tokens = scan("Calc1.stk")

for token in tokens:

    if(token.type == "STAR"):
        stack.append(stack.pop()*stack.pop())
    elif(token.type == "SLASH"):
        stack.append(int(1/stack.pop()*stack.pop()))
    elif(token.type == "MINUS"):
        stack.append(-stack.pop() + stack.pop())
    elif(token.type == "PLUS"):
        stack.append(stack.pop() + stack.pop())
    else:
        stack.append(int(token.lexeme))

if(len(stack) == 1):       
    print(str(stack.pop()))
else:
    stack.pop()
    print("Operacao incompleta na pilha\n Resultado intermediario = " + str(stack.pop()))

