# stack implementation using linkedlist
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
            print("pop element:", temp.data)
            self.top = self.top.next
            temp = None
    def print(self):
        if self.isempty():
            print("stack is empty")
        else:
            print("stack contains...")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next
    def rev(self):
        prev = None
        temp = self.top
        while temp:
            nextnode = temp.next
            temp.next = prev
            prev = temp
            temp = nextnode
        self.top = prev
st = stack()
st.push(node(10))
st.push(node(20))
st.push(node(30))
st.push(node(40))

print("Original stack:")
st.print()

st.rev()

print("Reversed stack:")
st.print()