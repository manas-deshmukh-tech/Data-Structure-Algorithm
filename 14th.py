# Circular linked list and delete node at position

class node:
    def __init__(self, val):
        self.data = val
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    def delete_at_position(self, position):
        if self.head == None:
            print("List is empty")
            return

        # Delete first node
        if position == 1:
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next

                self.head = self.head.next
                temp.next = self.head
            return

        temp = self.head
        count = 1

        while temp.next != self.head and count < position - 1:
            temp = temp.next
            count += 1

        if count != position - 1 or temp.next == self.head:
            print("Invalid position")
        else:
            temp.next = temp.next.next

    def print(self):
        total = 0

        if self.head == None:
            print("List is empty")
            return

        temp = self.head

        while True:
            total += temp.data
            print(temp.data)
            temp = temp.next

            if temp == self.head:
                break

        print("sum:", total)


list = linkedlist()

list.append(node(10))
list.append(node(20))
list.append(node(30))
list.append(node(40))

list.delete_at_position(3)

list.print()