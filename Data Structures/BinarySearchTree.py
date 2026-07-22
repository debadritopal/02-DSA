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
    def insert(self,node,num):
        if node is None:
            return Node(num)
        if num<node.data:
            node.left=self.insert(node.left,num)
        elif num>node.data:
            node.right=self.insert(node.right,num)
        return node
    def search(self, node, key):
        if node is None:
            return False
        if node.data == key:
            return True
        if key < node.data:
            return self.search(node.left, key)
        else:
           return self.search(node.right, key)
    def find_min(self,node):
        if node is None:
            print("Empty Tree")
            return
        if node.left is None:
            return node
        min_node=self.find_min(node.left)
        return min_node
    def delete(self,node,num):
        if node is None:
            return
        if num>node.data:
            node.right=self.delete(node.right,num)
        elif num<node.data:
            node.left=self.delete(node.left,num)
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is not None and node.right is None:
                return node.left
            if node.left is None and node.right is not None:
                return node.right
            if node.left is not None and node.right is not None:
                successor = self.find_min(node.right)
                node.data = successor.data
                node.right = self.delete(node.right, successor.data)
                return node
            return Node
tree=BinaryTree()
tree.insert(tree.root,90)
tree.insert(tree.root,89)
tree.insert(tree.root,91)
tree.insert(tree.root,96)
tree.insert(tree.root,92)
tree.insert(tree.root,10)
tree.insert(tree.root,109)
tree.insert(tree.root,46)
tree.inorder(tree.root)