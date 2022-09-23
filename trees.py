class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

 #INORDER

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

#PREORDER

    def preorder(self,root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

#POSTORDER
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

#NORMAL TREE

    def display(self):
        if self.left:
            self.left.display()
        print(self.data)
        if self.right:
            self.right.display()


root=Node(10)
root.left=Node(15)
root.right=Node(20)
root.left.left=Node(30)
root.right.right=Node(40)
root.left.right=Node(45)
#root.display()
#root.inorder(root)
#root.preorder(root)
root.postorder(root)