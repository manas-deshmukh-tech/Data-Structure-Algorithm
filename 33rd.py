# Implementation of Binary Search Tree using Linked List
class node:
    def __init__(self, val):
        self.left = None
        self.data = val
        self.right = None
class bst:
    def __init__(self):
        self.root = None
    def insert(self, newnode):
        if self.root is None:
            self.root = newnode
            return
        temp = self.root
        while True:
            if newnode.data < temp.data:
                if temp.left is None:
                    temp.left = newnode
                    return
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = newnode
                    return
                else:
                    temp = temp.right
# Inorder traversal (Recursive function outside class)
def inorder(temp):
    if temp is None:
        return
    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)

btree = bst()

btree.insert(node(10))
btree.insert(node(5))
btree.insert(node(2))
btree.insert(node(25))
btree.insert(node(13))
btree.insert(node(40))

inorder(btree.root)
print()