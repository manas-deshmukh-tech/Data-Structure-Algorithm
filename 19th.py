
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

    def count_occurrence(self, num):
        count = 0
        temp = self.head

        while temp is not None:
            if temp.data == num:
                count += 1

            temp = temp.next

        return count


dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(10)
dll.append(30)
dll.append(10)
dll.append(20)

print("Doubly Linked List:")
dll.display()

num = 10
print("Occurrence of", num, ":", dll.count_occurrence(num))
