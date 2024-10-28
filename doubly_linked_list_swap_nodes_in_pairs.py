'''
    DOUBLY LINKED LIST exercise: Swap Nodes in Pairs
    Algorithm and data structure

    Implement a method called swap_pairs within the class that swaps the values of adjacent
    nodes in the linked list. The method should not take any input parameters.
    
    Example:
    1 <-> 2 <-> 3 <-> 4 should become 2 <-> 1 <-> 4 <-> 3
    Edge cases: empty list, and list with 1 node
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
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True
    
    def swap_pairs(self):
        # edge case: empty or list with 1 node
        if self.length == 0 or self.length == 1:
            return False
        # create 4 pointers
        first = None
        before = self.head
        after = self.head.next
        end = after.next
        self.head = after
        cycles = self.length // 2
        # swap in pairs
        for i in range(cycles):
            after.prev = first
            after.next = before
            before.prev = after
            before.next = end
            if end:
                end.prev = before
            if i > 0:
                first.next = after
            if end is None:
                break
            # moving pointers
            if end.next is None:
                break
            first = before
            before = end
            after = end.next
            end = after.next
        return True


my_list = DoublyLinkedList(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.print_list()
my_list.swap_pairs()
my_list.print_list()
