#Write a program to perform the following operations on a Linear Queue 
# 1. Enqueue an element into the queue 
# 2. Dequeue an element from the queue 
# 3. Display 
# 4. Reverse the queue using stack 
# 5. Merge two queues into one. 
# 6. Check if two queues are identical
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        print(data, "inserted into queue")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            print("Deleted element:", self.queue.pop(0))

    def print_queue(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            print("Queue elements:", self.queue)

    def reverse_queue(self):
        stack = []

        while len(self.queue) > 0:
            stack.append(self.queue.pop(0))

        while len(stack) > 0:
            self.queue.append(stack.pop())

        print("Queue reversed successfully")

    def merge(self, q2):
        merged_queue = Queue()
        merged_queue.queue = self.queue + q2.queue
        return merged_queue

    def identical(self, q2):
        if self.queue == q2.queue:
            print("Both queues are Identical")
        else:
            print("Both queues are Not Identical")


q1 = Queue()
q2 = Queue()

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)

q2.enqueue(40)
q2.enqueue(50)

q1.print_queue()

q1.dequeue()

q1.print_queue()

q1.reverse_queue()

q1.print_queue()

q3 = q1.merge(q2)

print("Merged Queue:")
q3.print_queue()

q1.identical(q2)
