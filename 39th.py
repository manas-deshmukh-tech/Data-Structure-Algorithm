#Implementation of BST using Linked List and Level Order Traversal and show level wise output
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
    def level_order(self, rt):
        if rt is None:
            print("BST empty")
            return
        arr = []
        cnt = 0
        level = 0

        arr.append(rt)
        while cnt < len(arr):
            node_count = len(arr) - cnt  # Number of nodes in current level

            print("\nLevel:", level, "-", end=" ")
            for i in range(node_count):
                temp = arr[cnt]
                cnt += 1

                print(temp.data, end=" ")

                if temp.left is not None:
                    arr.append(temp.left)

                if temp.right is not None:
                    arr.append(temp.right)
            level += 1

btree = bst()

btree.insert(node(100))
btree.insert(node(10))
btree.insert(node(450))
btree.insert(node(4))
btree.insert(node(65))
btree.insert(node(300))
btree.insert(node(500))
btree.insert(node(50))
btree.insert(node(70))

print("Level Order Traversal:")
btree.level_order(btree.root)