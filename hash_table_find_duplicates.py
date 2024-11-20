'''
    Hash table / dictionary
    Algorithm and data structure.
    Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).
    Solved in Python by Alessandro Silvestri - 2024
    <alessandro.silvestri.work@gmail.com>
'''

def find_duplicates(li:list):
    '''using a dictionary '''
    dict_duplicates = {}
    list_duplicates = []
    # I iterate the list and I fill the dictionary
    for i in li:
        if not i in dict_duplicates:
            dict_duplicates[i] = 1
        else:
            dict_duplicates[i] += 1
    # I iterate the dictionary and I fill list_duplicates with the duplicates 
    for i in dict_duplicates:
        if dict_duplicates[i] > 1:
            list_duplicates.append(i)
    return list_duplicates


print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""
