class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def preorder(self,node):
        if node is None:
            return
        print(node.data,end=' ')
        self.preorder(node.left)
        self.preorder(node.right)
    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data,end=' ')
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data,end=' ')
        self.inorder(node.right)
    def search(self, node, key):
        if node is None:
            return False
        if node.data == key:
            return True
        if key < node.data:
            return self.search(node.left, key)
        else:
           return self.search(node.right, key)
    def insert(self,node,num):
        if node is None:
            return Node(num)
        if num<node.data:
            node.left=self.insert(node.left,num)
        elif num>node.data:
            node.right=self.insert(node.right,num)
        return node

tree=BinaryTree()
tree.root=Node(10)
tree.root.left=Node(5)
tree.root.right=Node(20)
tree.root.left.left=Node(3)
tree.root.left.right=Node(7)
tree.preorder(tree.root)
print()
tree.postorder(tree.root)
print()
tree.inorder(tree.root)
print(tree.search(tree.root,11))
tree.insert(tree.root,6)
tree.inorder(tree.root)