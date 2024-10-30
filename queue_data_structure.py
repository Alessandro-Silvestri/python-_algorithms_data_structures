'''
    QUEUE structure
    Algorithm and data structure
    
    first          last
      1 -> 2 -> 3 -> 4 -> None
      <-------queue direction----------
      as rule enqueue and dequeue have to be O(1)

    Solved in Python by Alessandro Silvestri - 2024
    <alessandro.silvestri.work@gmail.com>
'''

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = self.last = new_node
        self.length = 1
    
    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next
        print(f"[length: {self.length}]")
    
    def enqueue(self, value):
        new_node = Node(value)
        # edge case: empty queue
        if self.first is None:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
    
    def dequeue(self):
        # edge case: empty queue
        if self.first is None:
            return None
        # edge case: one node in queue
        if self.length == 1:
            temp = self.first
            self.first = self.last = None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp     
    

my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.print_queue()
print("dequeue: ", my_queue.dequeue())
print("dequeue: ", my_queue.dequeue())
print("dequeue: ", my_queue.dequeue())
print("dequeue: ", my_queue.dequeue())
print("dequeue: ", my_queue.dequeue())
my_queue.print_queue()
print(my_queue.first)
print(my_queue.last)
