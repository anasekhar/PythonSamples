""" 
This program will  explain all stack operations
"""

class Stack:
    
    def __init__(self):
        self.item=[]
    
    def isEmpty(self):
        return self.item==[]

    def push(self,item):
        self.item.append(item)

    def pop(self):
        if len(self.item)==0:
            return "size of stack is zero"
        else: return self.item.pop()

    def peek(self):
        if not(len(self.item)==0):
            return self.item[len(self.item)-1]

    def size(self):
        return len(self.item)



#s = Stack()
#
#print(s.isEmpty())
#s.push(40)
#s.push('dog')
#print(s.peek())
#s.push(True)
#print(s.size())
#print(s.isEmpty())
#print(s.pop())
#print(s.pop())
#print(s.pop())
#print(s.pop())
#print(s.size())
#print(s.peek())
