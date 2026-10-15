# Doubly Linear Linked List insert node and position and reverse list
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
            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp
        else:
            self.head = new_node

    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            new_node.next = self.head

            if self.head:
                self.head.prev = new_node

            self.head = new_node
            return

        temp = self.head
        count = 1

        while temp and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    def print(self):
        temp = self.head
        print("List elements:", end=" ")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()

    def reverse(self):
        temp = self.head

        # Move to the last node
        if temp is None:
            print("List is empty")
            return

        while temp.next:
            temp = temp.next

        # Print from last node to first node
        print("Reverse order:", end=" ")

        while temp:
            print(temp.data, end=" ")
            temp = temp.prev

        print()


list = linkedlist()

list.append(node(10))
list.append(node(20))
list.append(node(30))
list.append(node(40))

print("Previous list:", end=" ")
list.print()

list.insert(node(25), 3)

print("Updated list:", end=" ")
list.print()

list.reverse()
