# Linear queue using linked list

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

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
        if self.front == None:
            print("Queue is empty")
        else:
            print("Deleted:", self.front.data)
            self.front = self.front.next

            if self.front == None:
                self.rear = None

    def print(self):
        temp = self.front
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")


que = lqueue()

que.enqueue(node(23))
que.enqueue(node(2))
que.enqueue(node(24))
que.enqueue(node(3))

print("Before deletion:")
que.print()

que.dequeue()

print("After deletion:")
que.print()