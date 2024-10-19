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
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
    
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
    
    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index, end_index):
        end_first_list = self.head
        # edge case: empty list
        if self.length == 0:
            return None
        # edge case: reverse entire list
        if start_index == 0 and end_index == self.length - 1:
            left = None
            mid = self.head
            right = self.head.next
            while right:
                mid.next = left
                left = mid
                mid = right
                right = right.next
            mid.next = left
            self.head = mid
        # edge case: start_index is 0
        elif start_index == 0:
            left = self.head
            mid = self.head.next
            right = self.head.next.next    
            for _ in range(end_index - 1):
                # change direction of the arrow
                mid.next = left
                # 1 ste ahead of the pointers
                left = mid
                mid = right
                right = right.next
            end_first_list.next = mid
            self.head = left       
        # normal case and edge case when the last part of the list is reversed
        else:
            for _ in range(start_index - 1):
                end_first_list = end_first_list.next
            index_start = end_first_list.next
            left = index_start
            mid = index_start.next
            right = index_start.next.next
            for _ in range(end_index - start_index):
                # change direction of the arrow
                mid.next = left
                # 1 ste ahead of the pointers
                left = mid
                mid = right
                if right is None:
                    break
                right = right.next
            end_first_list.next = left
            index_start.next = mid









linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)


print("Original linked list: ")
linked_list.print_list()

# # Reverse a sublist within the linked list
# linked_list.reverse_between(2, 4)
# print("Reversed sublist (2, 4): ")
# linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# # Reverse a sublist of length 1 within the linked list
# linked_list.reverse_between(3, 3)
# print("Reversed sublist of length 1 (3, 3): ")
# linked_list.print_list()

# # Reverse an empty linked list
# empty_list = LinkedList(0)
# empty_list.make_empty()
# empty_list.reverse_between(0, 0)
# print("Reversed empty linked list: ")
# empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""







