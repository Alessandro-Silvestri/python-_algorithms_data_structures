'''
    Hash table / Exercise:  first_non_repeating_char 
    Algorithm and data structure.
    Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).
    Solved in Python by Alessandro Silvestri - 2024
    <alessandro.silvestri.work@gmail.com>
'''

def first_non_repeating_char(text:str):
    dict_chars = {}
    for char in text:
        if not char in dict_chars:
            dict_chars[char] = 1
        else:
            dict_chars[char] += 1
    for char in dict_chars:
        if dict_chars[char] == 1:
            return char 
    return None


print( first_non_repeating_char('leetcode') )
print( first_non_repeating_char('hello') )
print( first_non_repeating_char('aabbcc') )

"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""