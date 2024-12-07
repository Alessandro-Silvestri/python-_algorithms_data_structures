def find_pairs(arr1:list, arr2:list, target:int):
    list_result = []
    for i in arr2:
        diff = target - i
        if diff in arr1:
            item = (diff, i)
            list_result.append(item)
    return list_result


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""