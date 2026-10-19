
class Node:
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def swap_first_last(self):
        if self.head is None or self.head.next is None:
            return

        first = self.head
        last = self.head

        while last.next is not None:
            last = last.next

        first.data, last.data = last.data, first.data


dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)

print("Before swapping:")
dll.display()

dll.swap_first_last()

print("After swapping:")
dll.display()
