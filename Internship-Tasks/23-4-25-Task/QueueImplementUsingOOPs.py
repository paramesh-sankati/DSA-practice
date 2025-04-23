# Online Python compiler (interpreter) to run Python online.
class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,ele):
        self.queue.append(ele)
        return self.queue
    def dequeue(self):
        if self.isEmpty():
            return "No Elements in Queue to perform dequeue"
        else:
            self.queue.pop(0)
            return self.queue
    def isEmpty(self):
        if len(self.queue)==0:
            return True
        else:
            return False
    def front(self):
        if self.isEmpty():
            return "No Elements in Queue"
        else:
            return self.queue[0]
    def rear(self):
        if self.isEmpty():
            return "No Elements in Queue"
        else:
            return self.queue[-1]
    def display(self):
        return self.queue
    
obj1=Queue()
print(obj1.enqueue(9))   #adds 9 at rear end and return resultant queue
print(obj1.enqueue(12))    #adds 12 at rear end
print(obj1.enqueue(13))      #adds 13 at rear end
print(obj1.front())         #displays element at front end without removing
print(obj1.rear())          #displays element at rear end without removing
print(obj1.display())       #displays whole queue
print(obj1.dequeue())        #removes element from front end & return resultant queue
print(obj1.dequeue())        #removes element from front end & return resultant queue
print(obj1.dequeue())        #removes element from front end & return resultant queue
print(obj1.dequeue())
print(obj1.isEmpty())       #checks if queue is empty or not
print(obj1.front())       #returns first element of front end of queue
print(obj1.rear())        #returns first element of rear end of queue




    
    
        
    
    
    
