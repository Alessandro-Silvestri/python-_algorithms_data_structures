'''
    HASH TABLE
    Algorithm and data structure
    Solved in Python by Alessandro Silvestri - 2024
    <alessandro.silvestri.work@gmail.com>
'''

def subarray_sum(nums:list, target:int):
    numbs_dictionary = {}
    index_counter = 0
    indexes_result = []
    for i in nums:
        numbs_dictionary[i] = index_counter
        index_counter += 1
    counter = 0
    while numbs_dictionary != {}:
        sum = 0
        for i in numbs_dictionary:
            # save the start index
            if numbs_dictionary[i] == counter:
                start_index = counter # for adding in indexes_result = []
                start_value = i # for pop() the first element
            sum += i
            if sum == target:
                indexes_result.append(start_index)
                indexes_result.append(numbs_dictionary[i])
                return indexes_result
        counter += 1
        numbs_dictionary.pop(start_value)
    return indexes_result


nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""




