# Circular Singly Linked List
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

    def print(self):
        total = 0
        if self.head == None:
            return

        temp = self.head

        while True:
            print(temp.data)
            total += temp.data
            temp = temp.next

            if temp == self.head:
                break

        print("Sum:", total)


list = linkedlist()

n1 = node(10)
n2 = node(20)
n3 = node(30)

list.append(n1)
list.append(n2)
list.append(n3)
list.append(node(40))

list.print()