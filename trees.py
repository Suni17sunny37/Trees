class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

 #INORDER

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)

#PREORDER

    def preorder(self,root):
        if root:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

#POSTORDER
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")

#NORMAL TREE

    def display(self):
        if self.left:
            self.left.display()
        print(self.data,end=" ")
        if self.right:
            self.right.display()


root=Node(10)
root.left=Node(15)
root.right=Node(20)
root.left.left=Node(30)
root.right.right=Node(40)
root.left.right=Node(45)
print("Normal Traversal")
root.display()
print("/n")
print("Inorder Traversal")
root.inorder(root)
print("/n")
print("Preorder Traversal")
root.preorder(root)
print("/n")
print("Postorder Traversal")
root.postorder(root)
