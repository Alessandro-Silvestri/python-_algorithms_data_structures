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
        return temp.value
    
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
            return temp.value

        
        

            
            

my_list = LinkedList(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.print_list()
print("pop: ", my_list.pop_first())
my_list.print_list()

# my_list.debug_get_head_tail_values()


