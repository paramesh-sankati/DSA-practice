#Stack implementation using collection.deque
#append and pop operations using deque are faster compared to list
from collections import deque
stack=deque()
stack.append(23)
stack.append(34)
stack.append(45)
stack.append(12)
print(stack)

#pop
print(stack.pop())
print(stack.pop())

print(stack)
