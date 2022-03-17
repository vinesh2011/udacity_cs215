class node:
    def __init__(self,key) :
        self.right=None
        self.left=None
        self.key=key
def Preorder(root) :
    if root :
        print(root.key,end=" ")    
        Preorder(root.left) 
        Preorder(root.right)                 
root=node(30)
root.left=node(20)
root.right=node(40)
root.left.left=node(15)
root.left.right=node(25)       
Preorder(root)
print()
