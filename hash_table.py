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
    
    def set_item(self, key:str, value:int):
        index = self.__hash(key)
        item = [key, value]
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append(item)
    
    def get_item(self, key):
        '''Given a key it returns the value'''
        index = self.__hash(key)
        counter = 0
        if self.data_map[index] is not None:
            for i in self.data_map[index]:
                if i[0] == key:
                    return self.data_map[index][counter][1]
                counter += 1
        return None






my_hash_table = HashTable()
my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washer", 50)
my_hash_table.set_item("alex", 8)

my_hash_table.print_table()
print(my_hash_table.get_item("alex"))
