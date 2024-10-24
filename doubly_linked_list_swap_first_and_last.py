'''
    DOUBLY LINKED LIST exercise: Swap First and Last 
    Algorithm and data structure

    Swap the values of the first and last node
    Method name:
    swap_first_last
    Note that the pointers to the nodes themselves are not swapped
    only their values are exchanged.
    
    Solved in Python by Alessandro Silvestri - 2024
    <alessandro.silvestri.work@gmail.com>
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print(f"[length: {self.length}]")
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def swap_first_last(self):
        # edge case: empty list or with 1 Node
        if self.length == 0 or self.length == 1:
            return False
        head_value = self.head.value
        self.head.value = self.tail.value
        self.tail.value = head_value
        return True



my_list = DoublyLinkedList(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.print_list()
my_list.swap_first_last()
my_list.print_list()
my_list.swap_first_last()
my_list.print_list()
