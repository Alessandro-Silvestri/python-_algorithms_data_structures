'''
Structure:
parent 47
childrenon the right are higher
childrenon the left are lower

      47       
    /    \
  21      76
 /  \    /  \
18  27   52 82

in this case to calculate the number of nodes:
2^3 - 1
(3 is the number of steps to the bottom)
for the search is very efficient as it is O(n)
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

class Binary_search_tree:
    '''Using 2 pointers'''
    # this time the constructor creates an empty data structure
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        # empty tree
        if self.root is None:
            self.root = new_node
            return
        # create 2 pointers 
        temp = before = self.root
        # loop until the end and add the node
        while True:
          # going right
          if value > temp.value:
              temp = temp.right
              if temp is None:
                  temp = new_node
                  before.right = temp
                  return
          # going left
          elif value < temp.value:
              temp = temp.left
              if temp is None:
                  temp = new_node
                  before.left = temp
                  return
          else:
              return False
          
          # step forward
          before = temp
         
'''
      47       
    /    \ 
  21      76
 /  \    /  \
18  27   52 82

'''
my_tree = Binary_search_tree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(76)
my_tree.insert(18)
# my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.root.right.right.value)