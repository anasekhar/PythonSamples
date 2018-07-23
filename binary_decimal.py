
"""
This program converts the bindary digits to decimal values
"""

from stack_ex import Stack

def diveby2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber %2
        remstack.push(rem)
        decNumber = decNumber //2

    binString = ''
    while not remstack.isEmpty():
        binString = binString+str(remstack.pop())
    return binString

print(diveby2(42))
