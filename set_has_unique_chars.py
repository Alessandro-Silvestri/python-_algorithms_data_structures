def has_unique_chars(text:str):
    unique_chars = set()
    for i in text:
        unique_chars.add(i)
    return len(unique_chars) == len(text)



print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""