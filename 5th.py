#deleting nodes
class node:
    def __init__(self, val):
        self.data = val
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_position(self, new_node, position):

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        count = 1

        while temp and count < position - 1:
            temp = temp.next
            count += 1

        if temp == None:
            print("Invalid position")
        else:
            new_node.next = temp.next
            temp.next = new_node

    def delete_at_position(self, position):

        if self.head == None:
            print("List is empty")
            return

        if position == 1:
            self.head = self.head.next
            return

        temp = self.head
        count = 1

        while temp and count < position - 1:
            temp = temp.next
            count += 1

        if temp == None or temp.next == None:
            print("Invalid position")
        else:
            temp.next = temp.next.next

    def print(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next


list = linkedlist()

list.insert_at_position(node(10), 1)
list.insert_at_position(node(20), 2)
list.insert_at_position(node(30), 3)
list.insert_at_position(node(40), 4)

print("Before deletion:")
list.print()

list.delete_at_position(3)

print("After deletion:")
list.print()