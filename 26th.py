#Create a Stack with following operations
#1. Push
#2. Pop
#3. Display
#4. Reverse String using Stack
#5. Reverse Stack using another Stack

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "pushed into stack")

    def pop(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            print("Popped element:", self.top.data)
            self.top = self.top.next

    def print_stack(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            temp = self.top
            print("Stack elements:")

            while temp is not None:
                print(temp.data)
                temp = temp.next

    def reverse_string(self, string):
        temp_stack = Stack()

        for char in string:
            temp_stack.push_silent(char)

        result = ""

        while temp_stack.top is not None:
            result += temp_stack.top.data
            temp_stack.pop_silent()

        print("Reversed String:", result)

    def reverse_stack(self):
        temp_stack = Stack()

        while self.top is not None:
            temp_stack.push_silent(self.top.data)
            self.top = self.top.next

        while temp_stack.top is not None:
            self.push_silent(temp_stack.top.data)
            temp_stack.pop_silent()

        print("Stack reversed successfully")

    def push_silent(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop_silent(self):
        if self.top is not None:
            self.top = self.top.next


# Main program
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.print_stack()

s.pop()

s.reverse_string("HELLO")

s.reverse_stack()

s.print_stack()
