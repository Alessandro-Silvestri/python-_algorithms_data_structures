'''
    STACK structure
    Algorithm and data structure
    Solved in Python by Alessandro Silvestri - 2024
    <alessandro.silvestri.work@gmail.com>

O - top
|
\/
O
|
\/

The arrows have to be towards the bottom because the
methods push() and pop() have to be O(1) (o of one)
the stack needs only self.top
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
        print(f"[length: {self.height}]")
    
    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    
    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    
    
my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)
my_stack.print_stack()
print("popped: ",my_stack.pop().value)
my_stack.print_stack()