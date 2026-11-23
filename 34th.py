# Implementation of Binary Search Tree using Linked List and traversal using inorder inside class recursive method and count nodes
class node:
    def __init__(self, val):
        self.left = None
        self.data = val
        self.right = None

    def inorder(self):  # Recursive method
        if self is None:
            return
        else:
            if self.left is not None:
                self.left.inorder()
            print(self.data, end=" ")
            if self.right is not None:
                self.right.inorder()

    def count_nodes(self):  # Recursive method to count nodes
        count = 1

        if self.left is not None:
            count += self.left.count_nodes()

        if self.right is not None:
            count += self.right.count_nodes()

        return count

class bst:
    def __init__(self):
        self.root = None

    def insert(self, newnode):
        if self.root is None:
            self.root = newnode
            return
        else:
            temp = self.root
            while True:
                if newnode.data < temp.data:  # Left subtree
                    if temp.left is None:
                        temp.left = newnode
                        return
                    else:
                        temp = temp.left

                else:  # Right subtree
                    if temp.right is None:
                        temp.right = newnode
                        return
                    else:
                        temp = temp.right

btree = bst()

btree.insert(node(10))
btree.insert(node(50))
btree.insert(node(20))
btree.insert(node(25))
btree.insert(node(13))
btree.insert(node(47))

print("Inorder Traversal:")
btree.root.inorder()

print("Total Nodes:",btree.root.count_nodes())
