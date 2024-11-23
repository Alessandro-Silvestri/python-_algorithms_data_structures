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
    pass




# print("1st set:")
# print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

# print("\n2nd set:")
# print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

# print("\n3rd set:")
# print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



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
print(are_anagrams("a", "ab"))
