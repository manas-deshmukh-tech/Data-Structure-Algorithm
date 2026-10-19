
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

    def delete(self, pos):
        if self.head is None:
            return

        temp = self.head

        # Delete first node
        if pos == 1:
            self.head = temp.next

            if self.head is not None:
                self.head.prev = None

            return

        # Move to the node at the given position
        for i in range(pos - 1):
            if temp is None:
                return
            temp = temp.next

        if temp is None:
            return

        # Connect previous and next nodes
        temp.prev.next = temp.next

        if temp.next is not None:
            temp.next.prev = temp.prev


dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)

print("Before deletion:")
dll.display()

dll.delete(3)

print("After deletion:")
dll.display()
