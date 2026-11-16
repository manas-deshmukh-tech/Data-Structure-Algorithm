#Priority Queue
class node:
    def __init__(self, val, pr):
        self.data = val
        self.priority = pr
        self.next = None
class priority_queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, newnode):
        # Case 1: Queue is empty
        if self.front is None:
            self.front = self.rear = newnode
            return

        # Case 2: Insert at beginning
        if newnode.priority < self.front.priority:
            newnode.next = self.front
            self.front = newnode
            return

        # Case 3: Insert at correct position
        temp = self.front

        while temp.next and temp.next.priority <= newnode.priority:
            temp = temp.next

        newnode.next = temp.next
        temp.next = newnode

        # Update rear if inserted at end
        if newnode.next is None:
            self.rear = newnode

    def display(self):
        temp = self.front

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


pq = priority_queue()

pq.enqueue(node(100, 2))
pq.enqueue(node(200, 6))
pq.enqueue(node(300, 3))
pq.enqueue(node(400, 1))
pq.enqueue(node(500, 7))

pq.display()
