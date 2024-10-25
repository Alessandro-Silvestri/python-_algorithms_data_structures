'''
    DOUBLY LINKED LIST exercise: Swap First and Last 
    Algorithm and data structure

    Write a method to determine whether a given doubly linked list reads the same forwards and backwards.
    For example, if the list contains the values [1, 2, 3, 2, 1],
    then the method should return True, since the list is a palindrome.
    If the list contains the values [1, 2, 3, 4, 5], then the method should
    return False, since the list is not a palindrome.
    
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
    
    def is_palindrome(self):
        temp1 = self.head
        temp2 = self.tail
        steps = self.length // 2

        for _ in range(steps):
            if temp1.value != temp2.value:
                return False
            temp1 = temp1.next
            temp2 =  temp2.prev
        return True


my_list = DoublyLinkedList(1)
my_list.append(2)
my_list.append(3)
my_list.append(2)
my_list.append(1)
print(my_list.is_palindrome())