
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

    # Delete alternate nodes
    def delete_alternate(self):
        temp = self.head

        while temp is not None and temp.next is not None:
            temp.next = temp.next.next
            temp = temp.next


ll = LinkedList()

# Create linked list
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(60)

# Display original linked list
print("Original Linked List:")
ll.display()

# Delete alternate nodes
ll.delete_alternate()

# Display updated linked list
print("After deleting alternate nodes:")
ll.display()
