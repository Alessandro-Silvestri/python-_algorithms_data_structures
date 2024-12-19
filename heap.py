class Heap():
    def __init__(self):
        self.heap_list = [None]
    
    def print_heap(self):
        print(self.heap_list)
    
    def insert(self, value):
        # edge case: empty heap_list
        if self.heap_list == [None]:
            self.heap_list.append(value)
            return True
        # regular case
        self.heap_list.append(value)
        # loop for changing position between parent and son
        value_index = self.heap_list.index(value)
        parent_index = self.heap_list.index(value) // 2

        while value_index > 1 and self.heap_list[value_index] > self.heap_list[parent_index]:
            temp = self.heap_list[parent_index]
            self.heap_list[parent_index] = value
            self.heap_list[value_index] = temp
            
            value_index = self.heap_list.index(value)
            parent_index = self.heap_list.index(value) // 2


my_heap = Heap()
my_heap.insert(3)
my_heap.insert(3)
my_heap.insert(4)
my_heap.insert(2)
my_heap.print_heap()

