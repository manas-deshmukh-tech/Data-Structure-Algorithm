# Implementation of Binary Search Tree using Linked List & Delete Node and Count Leaf Nodes and search node
class node:
    def __init__(self, val):
        self.left = None
        self.data = val
        self.right = None

    def inorder(self):  # Recursive method
        if self.left is not None:
            self.left.inorder()

        print(self.data, end=" ")

        if self.right is not None:
            self.right.inorder()

    def count_nodes(self):  # Count total nodes
        count = 1

        if self.left is not None:
            count += self.left.count_nodes()

        if self.right is not None:
            count += self.right.count_nodes()

        return count

    def count_leaf(self):  # Count leaf nodes
        if self.left is None and self.right is None:
            return 1

        count = 0

        if self.left is not None:
            count += self.left.count_leaf()

        if self.right is not None:
            count += self.right.count_leaf()

        return count


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

    def del_node(self, rt, val):
        if rt is None:
            return rt

        if val < rt.data:
            rt.left = self.del_node(rt.left, val)

        elif val > rt.data:
            rt.right = self.del_node(rt.right, val)

        else:
            # Node has no left child
            if rt.left is None:
                return rt.right

            # Node has no right child
            if rt.right is None:
                return rt.left

            # Node has both children
            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.del_node(rt.right, succ.data)

        return rt

    def search(self,key):
        temp=self.root
        while temp:
            if temp.data==key:
                return True
            elif key<temp.data:
                temp=temp.left
            else:
                temp=temp.right
        return False
    def get_successor(self, temp):
        temp = temp.right

        while temp.left is not None:
            temp = temp.left

        return temp


# Creating BST
btree = bst()

btree.insert(node(10))
btree.insert(node(15))
btree.insert(node(23))
btree.insert(node(55))
btree.insert(node(73))
btree.insert(node(70))

print("Inorder Traversal:")
btree.root.inorder()

# Deletion
btree.root = btree.del_node(btree.root, 23)

print("\nAfter Deletion:")
btree.root.inorder()

print("\nTotal Nodes:", btree.root.count_nodes())
print("Total Leaf Nodes:", btree.root.count_leaf())
if btree.search(15):
    print("node found")
else:
    print("node not found")