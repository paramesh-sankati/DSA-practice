class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,item):
        self.queue.append(item)     #adds element at last 
    def dequeue(self):
        if len(self.queue)<1:
            return None
        return self.queue.pop(0)    #removes element at index 0 i.e front end
    def display(self):
        print(self.queue)

qobj=Queue()
qobj.enqueue(12)
qobj.enqueue(13)
qobj.enqueue(14)
qobj.enqueue("hi")
print(qobj.dequeue())
qobj.display()