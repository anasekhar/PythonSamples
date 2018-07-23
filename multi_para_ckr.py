"""
This module check for multiple paranthysis and return true/False
"""

from stack_ex import Stack

def paraChecker(symbolString):

    s = Stack()
    index = 0
    balanced = True

    while index < len(symbolString) and balanced :

        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not chekcer(top,symbol):
                    balanced = False
        index +=1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def chekcer(top,sym):

    tops = "([{"
    closes = ")]}"

    return tops.index(top)==closes.index(sym)

print(paraChecker("{{([][])}()}"))
print(paraChecker("[{()]"))

