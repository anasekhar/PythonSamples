""" This program will check if paranthesis validation"""

from stack_ex import Stack

def paracherker(symbolString):

    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced :
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(paracherker('((()))'))
print(paracherker('(()))'))

