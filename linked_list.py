'''
    LINKED LIST
    Algorithm and data structure
    Solved in Python by Alessandro Silvestri - 2024
    <alessandro.silvestri.work@gmail.com>
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
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
    
    def debug_get_head_tail_values(self):
        print(f"\nHead object: {self.head}")
        print(f"Tail object: {self.tail}")
        try:
            print(f"Head value: {self.head.value}")
        except AttributeError as e:
            print(f"Head value ERROR: {e.args[0]}")
        try:
            print(f"Tail value: {self.tail.value}")
        except AttributeError as e:
            print(f"Tail value ERROR: {e.args[0]}")
        print()
    
    def append(self, value):
        new_node = Node(value) # create a node 
        self.length += 1 # increase the length
        if self.head is None: # edge case if the list is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def pop(self):
        if self.head is None: # edge case: empty list
            return None
        elif self.length == 1: # edge case: list with 1 item
            temp = self.head
            self.head = self.tail = None
            self.length = 0
            return temp.value       
        else: # using 2 pointers
            temp = pre = self.head
            while temp.next:
                pre = temp
                temp = temp.next
        self.tail = pre
        pre.next = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        self.length += 1
        if self.head is None: # edge case: empty list
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        return True
    
    def pop_first(self):
        if self.head is None: # edge case: empty list
            self.tail = None
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp
    
    def get(self, index):
        # edge case: index out of range or empty list
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index) # edge case: index out of range or empty list
        if temp is None:
            return False
        temp.value = value
        return True
    
    def insert(self, index, value):
        # edge case: index out of range or empty list
        if index < 0 or index > self.length or self.head is None:
            return False
        # edge case: insert at the first position
        if index == 0:
            self.prepend(value)
            return True
        new_node = Node(value)
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = new_node
        new_node.next = temp
        # edge case: new_node in the last position: I move tail to new_node
        if index == self.length: 
            self.tail = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        # edge case: index out of range or empty list
        if index < 0 or index >= self.length or self.head is None:
            return None    
        if index == 0: # remove first node
            return self.pop_first()
        if index == self.length - 1: # remove last node    
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        '''
      None       T                                   H
                 1    ->     2    ->     3    ->     4    -> None
     before     temp        after

        • invert head and tail
        • I create 3 pointers
        • I invert the direction between temp and before
        • loop until the end
       
        '''
        # edge case: empty list
        if self.head is None:
            return None
        # create 3 pointers
        temp = self.head
        before = None
        after = temp.next
        # swap head and tail
        self.head = self.tail
        self.tail = temp
        # cycling to the end for changing direction
        cycles = self.length - 1
        for _ in range(cycles):
            temp.next = before
            before = temp
            temp = after
            after = after.next
        temp.next = before
    

# testing the reverse method      
my_list = LinkedList(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.append(6)
my_list.append(7)
my_list.reverse()
my_list.print_list()


