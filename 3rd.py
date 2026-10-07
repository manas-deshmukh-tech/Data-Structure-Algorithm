#linked list and inserting node at position using append and position 
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
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert_at_position(self, new_node, position):
        # Insert at first position
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        count = 1

        # Move to node before the required position
        while temp and count < position - 1:
            temp = temp.next
            count += 1

        if temp == None:
            print("Invalid position")
        else:
            new_node.next = temp.next
            temp.next = new_node

    def print(self):
        total = 0
        temp = self.head

        while temp:
            total += temp.data
            print(temp.data)
            temp = temp.next

        print("sum:", total)


list = linkedlist()

n1 = node(10)
n2 = node(20)
n3 = node(30)

list.append(n1)
list.append(n2)
list.append(n3)
list.append(node(40))

list.insert_at_position(node(25), 3)

list.print()