#Implement stack to queue conversion using linked list
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, newnode):
        newnode.next = self.top
        self.top = newnode

    def pop(self):
        if self.isempty():
            print("stack is empty")
            return None
        else:
            temp = self.top
            popped_data = temp.data
            self.top = self.top.next
            temp = None
            return popped_data

    def print(self):
        if self.isempty():
            print("stack is empty")
        else:
            print("stack contains...")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next


class lqueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, newnode):
        if self.rear:
            self.rear.next = newnode
            self.rear = newnode
        else:
            self.front = self.rear = newnode

    def print(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


def reverse_stack(s1):
    q1 = lqueue()

    while not s1.isempty():
        q1.enqueue(node(s1.pop()))

    print("Queue after reversing stack:")
    q1.print()

s1 = stack()

s1.push(node(1))
s1.push(node(2))
s1.push(node(3))
s1.push(node(4))

print("Original stack:")
s1.print()

reverse_stack(s1)
