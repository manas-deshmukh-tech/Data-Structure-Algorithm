
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List
    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # 2. Traverse and print
    def print(self):
        temp = self.head
        print("Linked List data:")

        while temp:
            print(temp.data)
            temp = temp.next

    # 3. Insert node at a specific position
    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        p = 1

        while temp and p < pos - 1:
            temp = temp.next
            p += 1

        if temp == None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 4. Find Middle Node using length // 2
    def middle(self):
        temp = self.head
        length = 0

        while temp:
            length += 1
            temp = temp.next

        if length == 0:
            print("Linked List is empty")
            return

        mid = length // 2
        temp = self.head

        for i in range(mid):
            temp = temp.next

        print("Middle node:", temp.data)

    # 5. Delete node by value
    def del_node(self, value):
        temp = self.head

        if temp == None:
            print("Linked List is empty")
            return

        if temp.data == value:
            self.head = self.head.next
            return

        while temp.next:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next

        print("Value is not in the list")

    # 6. Reverse Linked List
    def reverse(self):
        prev = None
        temp = self.head

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev

    # 7. Sum of every two consecutive node values
    def sum(self):
        temp = self.head

        while temp and temp.next:
            total = temp.data + temp.next.data
            print(temp.data, "+", temp.next.data, "=", total)
            temp = temp.next


# Main Program
list = LinkedList()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(50)

# Create Linked List
list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)

list.print()

# Insert nodes
print("\nList after insertion:")
list.insert(Node(100), 3)
list.insert(Node(70), 4)
list.print()

# Find Middle Node
print("\nMiddle node:")
list.middle()

# Delete node
list.del_node(100)
print("\nLinked List after deleting:")
list.print()

# Reverse Linked List
print("\nReversed list:")
list.reverse()
list.print()

# Sum of consecutive pairs
print("\nSum of consecutive pairs:")
list.sum()
