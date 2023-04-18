stack = []
f = open("Calc1.stk", "r")

for line in [l.rstrip() for l in f.readlines()]:

    if(line == '*'):
        stack.append(stack.pop()*stack.pop())
    elif(line == '/'):
        stack.append(int(1/stack.pop()*stack.pop()))
    elif(line == '-'):
        stack.append(-stack.pop() + stack.pop())
    elif(line == '+'):
        stack.append(stack.pop() + stack.pop())
    else:
        stack.append(int(line))

if(len(stack) == 1):       
    print(str(stack.pop()))
else:
    stack.pop()
    print("Operacao incompleta na pilha\n Resultado intermediario = " + str(stack.pop()))