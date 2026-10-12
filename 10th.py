
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    def delete_first(self):
        if self.head is not None:
            self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        temp.next = None


ll = LinkedList()

# Create linked list
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

# Display original linked list
print("Original Linked List:")
ll.display()

# Delete first and last nodes
ll.delete_first()
ll.delete_last()

# Display updated linked list
print("After deleting first and last nodes:")
ll.display()
