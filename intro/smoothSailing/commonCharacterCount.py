"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
  commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""
def commonCharacterCount(s1, s2):
    d1_dict = {}
    total = 0
    for c in s1:
        if c not in d1_dict:
            d1_dict[c] = 1
        else:
            d1_dict[c] += 1
    for c in s2:
        if c in d1_dict:
            if(d1_dict[c] > 0):
                total += 1
                d1_dict[c] -= 1
    return total
    
