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
    
    def reverse(self):
        # edge case: empty list
        if self.head is None:
            return False
        # normal case
        temp1 = self.head
        temp2 = self.head.next       
        while temp2:
            temp1.next = temp1.prev
            temp1.prev = temp2
            temp1 = temp2
            temp2 = temp2.next
        temp1.next = temp1.prev
        temp1.prev = None 
        self.tail = self.head
        self.head = temp1


my_list = DoublyLinkedList(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.append(6)
my_list.append(7)
my_list.print_list()
my_list.reverse()
my_list.print_list()

