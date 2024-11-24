def are_anagrams(word1:str, word2:str):
    dict_chars_word1 = {}
    dict_chars_word2 = {}
    # fill dict_chars_word1 with characters
    for char in word1:
        if not char in dict_chars_word1:
            dict_chars_word1[char] = 1
        else:
            dict_chars_word1[char] += 1
    # fill dict_chars_word2 with characters
    for char in word2:
        if not char in dict_chars_word2:
            dict_chars_word2[char] = 1
        else:
            dict_chars_word2[char] += 1
    # check the 2 lengths     
    if len(dict_chars_word1) != len(dict_chars_word2):
        return False
    # compare the 2 dictionaries comparing the number of characters
    for char in dict_chars_word1:
        if char not in dict_chars_word2:
            return False
        if dict_chars_word1[char] != dict_chars_word2[char]:
            return False
    return True


def group_anagrams(strings:list):
    list_result = [[]]
    counter_list = 0
    while strings != []:
        first_word = strings[0]
        list_result[counter_list].append(first_word)
        strings.pop(0)
        index_counter = 0
        while index_counter != len(strings):
            if are_anagrams(first_word, strings[index_counter]):
                list_result[counter_list].append(strings[index_counter])
                strings.pop(index_counter)
            else:
                index_counter += 1
        counter_list += 1
        list_result.append([])
    return list_result[:-1]


# print("1st set:")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

# print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )


"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""

# remove first item
# my_list = [1, 2, 3, 4, 5]
# first_item = my_list.pop(0)  # Removes the first item

