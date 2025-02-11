#Queue module contains the LIFO queue
'''it is having some additional functions and works same as stack'''

#put function is used to insert the data in queue
#get function is used to remove the element

from queue import LifoQueue
stack=LifoQueue(maxsize=3)
stack.put(12)
stack.put(13)
stack.put(14)
print(stack)
stack.get()  #removing last element
print(stack.qsize())   #size of stack or elements in it 
print(stack.full())   #is the stack full
