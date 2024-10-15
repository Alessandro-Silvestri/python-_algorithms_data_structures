'''
    LINKED LIST: partition_list() exercise
    Algorithm and data structure
    Solved in Python by Alessandro Silvestri - 2024
    <alessandro.silvestri.work@gmail.com>

The function partition_list takes an integer x as a parameter and modifies
the current linked list in place according to the specified criteria.
If the linked list is empty (i.e., head is null),
the function should return immediately without making any changes.

Example 1:
Input:
Linked List: 3 -> 8 -> 5 -> 10 -> 2 -> 1 x: 5

Process:
Values less than 5: 3, 2, 1
Values greater than or equal to 5: 8, 5, 10

Output:
Linked List: 3 -> 2 -> 1 -> 8 -> 5 -> 10


Example 2:
Input:
Linked List: 1 -> 4 -> 3 -> 2 -> 5 -> 2 x: 3

Process:
Values less than 3: 1, 2, 2
Values greater than or equal to 3: 4, 3, 5

Output:
Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5

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

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def partition_list(self, x):
        temp = self.head
        # create 2 empty lists
        list1 = LinkedList(None)
        list1.make_empty()
        list2 = LinkedList(None)
        list2.make_empty()
        # i fill the 2 lists 
        while temp:
            if temp.value < x:
                list1.append(temp.value)
            else:
                list2.append(temp.value)
            temp = temp.next
        # make the entire list empty
        self.make_empty()
        # 2 loops recreate the entire list adding list1 + list2
        temp = list1.head
        while temp:
            self.append(temp.value)
            temp = temp.next
        temp = list2.head
        while temp:
            self.append(temp.value)
            temp = temp.next
        


ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
ll.print_list() # Output: 3 5 8 10 2 1

ll.partition_list(5)

print("LL after partition_list:")
ll.print_list() # Output: 3 2 1 5 8 10


"""
    EXPECTED OUTPUT:
    ----------------
    LL before partition_list:
    3
    5
    8
    10
    2
    1
    LL after partition_list:
    3
    2
    1
    5
    8
    10
    
"""