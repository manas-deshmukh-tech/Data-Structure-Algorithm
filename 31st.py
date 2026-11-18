#Implement queue to stack conversion using linked list
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

    def dequeue(self):
        if self.front is None:
            print("queue is empty")
            return None
        else:
            temp = self.front
            popped_data = temp.data
            self.front = self.front.next

            if self.front is None:
                self.rear = None

            temp = None
            return popped_data

    def print(self):
        if self.front is None:
            print("queue is empty")
        else:
            temp = self.front
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")


def queue_to_stack(q1):
    s1 = stack()

    while q1.front:
        s1.push(node(q1.dequeue()))

    print("Stack after transferring queue:")
    s1.print()

que = lqueue()

que.enqueue(node(1))
que.enqueue(node(2))
que.enqueue(node(3))
que.enqueue(node(4))

print("Original queue:")
que.print()

queue_to_stack(que)
