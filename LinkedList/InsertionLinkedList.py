#creating a node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None    #iniitially each node next part is None

#creating a singly linkedlist
class SinglyLinkedList:
    def __init__(self):
        self.head=None    #head is initially pointing
    def traversal(self):
        if self.head is None:
            print("Singly Linked List is Empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.next
            print()
    def insert_at_beginnning(self,data):
        nb=Node(data)  #new node 
        nb.next=self.head    #nb.next points to self.head i.e n1
        sll.head=nb
    def insert_at_end(self,data):
        pass

n1=Node(8)
n2=Node(10)
n3=Node(12)
n4=Node(13)
n1.next=n2
n2.next=n3
n3.next=n4
sll=SinglyLinkedList()  
sll.head=n1     #head is pointing to n1
sll.traversal()
sll.insert_at_beginnning(18)
sll.traversal()


