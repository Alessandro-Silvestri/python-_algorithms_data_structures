def longest_consecutive_sequence(arr:list):
    #edge cases
    if len(arr) == 1:
        return 1
    if arr == []:
        return 0
    # normal case
    series_lengths = []
    for i in arr:
        following_num = i + 1
        if following_num in arr:
            current_serie_length = 2
            while True:
                following_num += 1
                if following_num in arr:
                    current_serie_length += 1
                else:
                    series_lengths.append(current_serie_length)
                    break
    if series_lengths == []:
        return 1
    # retrieve the migger number
    max = 0
    for i in series_lengths:      
        if i > max:
            max = i 
    return max


# print( longest_consecutive_sequence([100, 99, 4, 200, 1, 3, 2]) )
print( longest_consecutive_sequence([3,6,9]) )




"""
    EXPECTED OUTPUT:
    ----------------
    4

"""
