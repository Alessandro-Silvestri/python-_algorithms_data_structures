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

    



print(two_sum([6, 1, 7, 6, 2, 9, 3], 12))  

# print(two_sum([3, 3], 6))

