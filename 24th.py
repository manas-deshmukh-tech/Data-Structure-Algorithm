#linear queue using linkedlist
class node:
    def __init__(self,val):
        self.data=val
        self.next=None
class lqueue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,newnode):
        if self.rear:
            self.rear.next=newnode
            self.rear=newnode
        else:
            self.front=self.rear=newnode
    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end="->")
            temp=temp.next
que=lqueue()
que.enqueue(node(23))
que.enqueue(node(2))
que.enqueue(node(24))
que.enqueue(node(3))
que.print()