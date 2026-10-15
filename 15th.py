# Doubly Linear Linked List
class node:
    def __init__(self, value):
        self.prev = None
        self.data = value
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def append(self, new_node):
        temp = self.head
        if temp:
            while temp.next:  # Finding last node
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

        else:  # First node
            self.head = new_node
    def print(self):
        temp = self.head
        print("List elements:", end=" ")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next  # Move to next node

        print()


list = linkedlist()

n1 = node(10)
n2 = node(20)
n3 = node(30)

list.append(n1)
list.append(n2)
list.append(n3)
list.append(node(40))

list.print()
