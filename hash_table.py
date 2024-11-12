'''
The hash table structure
0 :  [key, value]
1 :  [[key, value], [key, value] ...]
2 :  None
3 :  None
4 :  None
5 :  None
6 :  None
'''

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        '''Given a key the function returns the position in the table'''
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    
my_hash_table = HashTable()
my_hash_table.print_table()