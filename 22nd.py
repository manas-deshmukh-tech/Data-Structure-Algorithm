class node:
    def __init__(self,val):
        self.data=val
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def append(self,newnode):
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newnode
    def insert_pos(self,newnode,pos):
        if pos==1:
            newnode.next=self.head
            self.head=newnode
        else:
            temp=self.head
            for i in range(pos-2):
                temp=temp.next
            newnode.next=temp.next
            temp.next=newnode
    def delete_node(self,pos):
        if self.head==None:
            print("list empty")
            return
        if pos==1:
            self.head=self.head.next
        else:
            temp=self.head
            for i in range(pos-2):
                if temp.next==None: #checks before moving 
                    print("invalid position")
                    return
                temp=temp.next
            if temp.next==None: #checks after reaching previous
                    print("invalid position")
                    return
            temp.next=temp.next.next
    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
list=linkedlist()
n1=node(10)
n2=node(20)
list.append(n1)
list.append(n2)
list.append(node(30))
print("before")
list.print()
list.insert_pos(node(25),3)
print("after")
list.print()
list.delete_node(3)
print("delete")
list.print()

    
