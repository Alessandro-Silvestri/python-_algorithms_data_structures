'''
    LINKED LIST: find_middle_node()
    Algorithm and data structure
    Solved in Python by Alessandro Silvestri - 2024
    <alessandro.silvestri.work@gmail.com>


LL: Find Middle Node ( ** Interview Question)
Implement the find_middle_node method for the LinkedList class.
Note: this LinkedList implementation does not have a length member variable.
If the linked list has an even number of nodes, return the first node of the second half of the list.
Keep in mind the following requirements:
The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.
When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.
The method should return the middle node when the number of nodes is odd or the first node of the second half of the list if the list has an even number of nodes.
The method should only traverse the linked list once.  In other words, you can only use one loop.
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
    
    def find_middle_node(self):
        slow = self.head
        fast = self.head.next
        while fast:
            if fast.next is None:
                return slow.next
            slow = slow.next
            fast = fast.next.next
        return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
print( my_linked_list.find_middle_node().value )
