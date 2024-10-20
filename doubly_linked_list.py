'''
    DOUBLY LINKED LIST
    Algorithm and data structure
    Solved in Python by Alessandro Silvestri - 2024
    <alessandro.silvestri.work@gmail.com>
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Doubly_linked_list:
    def __init__(self, value):
        self.new_node = Node(value)
        self.head = self.new_node
        self.tail = self.new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        print(f"[length: {self.length}]")

    def append(self, value):
        new_node = Node(value)
        if self.head is None: # edge case: empty list
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        temp = self.tail
        if self.head is None: # edge case: empty list
            return None
        if self.length == 1:  # edge case: only 1 node in the list
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        if self.head is None: # edge case: empty list
            self.append(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
        return True
    
    def pop_first(self):
        if self.head is None: # edge case: empty list
            return None
        if self.length == 1:  # edge case: only 1 node in the list
            return self.pop()
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.head.pre = None
        self.length -= 1
        return temp


# testing pop_first() method
my_list = Doubly_linked_list(2)
my_list.append(1)

for _ in range(3):
    print(my_list.pop_first())


