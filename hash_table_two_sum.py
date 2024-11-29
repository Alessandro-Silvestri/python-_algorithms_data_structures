# It pass all the tests but not the duplicate numbers line: print(two_sum([3, 3], 6))

def two_sum(ints:list, target:int):
    list_result = []
    dict_numbers = {}
    index_key = 0

    for num in ints:
    

        dict_numbers[num] = target - num


    found = False
    for key_num in dict_numbers:

        # edge case if number is the half of the target
        if key_num == target / 2:
            index_key += 1
            continue
        
        if dict_numbers[key_num] in dict_numbers and found == False:
            list_result.append(index_key)
            found = True
            first_number = key_num    



        if found:
            if key_num == target - first_number:
                list_result.append(index_key)
                break
       
        index_key += 1



    return list_result

    
# print(two_sum([5, 1, 7, 2, 9, 3], 10))  
# print(two_sum([4, 2, 11, 7, 6, 3], 9)) 
# print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
# print(two_sum([1, 3, 5, 7, 9], 10))  
# print ( two_sum([1, 2, 3, 4, 5], 10) )
# print ( two_sum([1, 2, 3, 4, 5], 7) )
# print ( two_sum([1, 2, 3, 4, 5], 3) )
# print ( two_sum([], 0) )

print(two_sum([3, 3], 6))


"""
    EXPECTED OUTPUT:
    ----------------
    [1, 4]
    [1, 3]
    [0, 3]
    [1, 3]
    []
    [2, 3]
    [0, 1]
    []

"""


# O(1)
# my_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "a": 3}
# print("a" in my_dict)

