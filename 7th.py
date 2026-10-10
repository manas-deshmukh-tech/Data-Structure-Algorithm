
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            val = int(input("Enter value: "))
            new_node = Node(val)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = new_node

    # 2. Traverse and print
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 3. Insert at specific position
    def insert(self, val, pos):
        new_node = Node(val)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(pos - 2):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    # 4. Find middle node
    def middle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        if slow is not None:
            print("Middle node:", slow.data)

    # 5. Delete node
    def delete(self, pos):
        if self.head is None:
            return

        if pos == 1:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(pos - 2):
            temp = temp.next

        temp.next = temp.next.next

    # 6. Reverse Linked List
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # 7. Sum of consecutive nodes
    def pair_sum(self):
        temp = self.head

        while temp is not None and temp.next is not None:
            total = temp.data + temp.next.data
            print(temp.data, "+", temp.next.data, "=", total)
            temp = temp.next


def solution():
    ll = LinkedList()

    # Create
    ll.create()

    # Traverse
    print("Linked List:")
    ll.display()

    # Insert
    val = int(input("Enter value to insert: "))
    pos = int(input("Enter position: "))
    ll.insert(val, pos)
    print("After insertion:")
    ll.display()

    # Middle
    ll.middle()

    # Delete
    pos = int(input("Enter position to delete: "))
    ll.delete(pos)
    print("After deletion:")
    ll.display()

    # Reverse
    ll.reverse()
    print("Reversed Linked List:")
    ll.display()

    # Sum consecutive nodes
    print("Sum of consecutive nodes:")
    ll.pair_sum()


solution()
