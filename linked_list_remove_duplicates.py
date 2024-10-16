'''
    LINKED LIST: remove_duplicates()
    Algorithm and data structure
    Solved in Python by Alessandro Silvestri - 2024
    <alessandro.silvestri.work@gmail.com>

Procedure adopted:
using set() temp iterates all the list and puts all the values in a set()
I make empty the linked list and I recreate it iterating along the set variables

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next  
            
    def print_all(self):
        if self.length == 0:
            print("Head: None")
        else:
            print("Head: ", self.head.value)
        print("Length: ", self.length)
        print("\nLinked List:")
        if self.length == 0:
            print("empty")
        else:
            self.print_list()

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1

    def remove_duplicates(self):
        '''using set()
        temp iterates all the list and puts all the values in a set()
        I make empty the linked list and I recreate it iterating along the set variable
        '''
        temp = self.head
        set_no_duplicates = set()
        while temp:
            set_no_duplicates.add(temp.value)
            temp = temp.next
        self.head = None
        self.length = 0
        for i in set_no_duplicates:
            self.append(i)


my_linked_list = LinkedList(1)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.remove_duplicates()

my_linked_list.print_all()



