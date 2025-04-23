class Node:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
class BST:
    def __init__(self):
        self.root=None
    def insert_root(self,key):
        if self.root==None:
            self.root=Node(key)
        else:
            self.insert_inner(self.root,key)
    def insert_inner(self,root,key):
        if key<root.key:
            if root.left==None:
                root.left=Node(key)
            else:
                self.insert_inner(root.left,key)
        elif key>root.key:
            if root.right==None:
                root.right=Node(key)
            else:
                self.insert_inner(root.right,key)
    


        
