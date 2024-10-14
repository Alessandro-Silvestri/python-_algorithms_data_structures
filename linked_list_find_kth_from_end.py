'''
    LINKED LIST: find_kth_from_end()
    Algorithm and data structure
    Solved in Python by Alessandro Silvestri - 2024
    <alessandro.silvestri.work@gmail.com>

LL: Find Kth Node From End ( ** Interview Question)
Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.

Given this LinkedList:

1 -> 2 -> 3 -> 4

If k=1 then return the first node from the end (the last node) which contains the value of 4.
If k=2 then return the second node from the end which contains the value of 3, etc.
If the index is out of bounds, the program should return None.
The find_kth_from_end function should follow these requirements:
The fast pointer should move k nodes ahead in the list.
If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.
The slow and fast pointers should then move forward in the list at the same time until the fast pointer reaches the end of the list.
The function should return the slow pointer, which will be at the k-th position from the end of the list.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  
  
linked_list = LinkedList(1)
linked_list.append(2)   
linked_list.append(3)   
linked_list.append(4)   
linked_list.append(5)   
linked_list.append(6)   
linked_list.append(7)   
linked_list.append(8)   

def find_kth_from_end(llist, value):
    slow = llist.head
    fast = llist.head
    # fast ahead for value steps
    # and check if value is out of range
    for _ in range(value):
        if fast is None:
            return None
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    return slow

print(find_kth_from_end(linked_list, 6))


