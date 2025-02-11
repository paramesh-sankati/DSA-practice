#Stack implementation using list
#append()-----as push()
#pop()

class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        print(self.stack.pop())
    def dispStack(self):
        print(self.stack)

sobj=Stack()
sobj.push(12)
sobj.push(22)
sobj.push(32)
sobj.push(42)
sobj.dispStack()
sobj.pop()
