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
        temp = self.head
        for i in range(1, self.length - 1):
            temp = temp.next
        self.tail = temp
        temp = temp.next
        self.tail.next = None
        self.length -= 1
        return temp.value
    
            

my_list = LinkedList(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.print_list()
print(my_list.pop())
print()
my_list.print_list()

