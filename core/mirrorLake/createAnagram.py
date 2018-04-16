"""
You are given two strings s and t of the same length, consisting of uppercase English letters. Your task is to find the minimum
number of "replacement operations" needed to get some anagram of the string t from the string s. A replacement operation is performed
by picking exactly one character from the string s and replacing it by some other character.

Example

  For s = "AABAA" and t = "BBAAA", the output should be
    createAnagram(s, t) = 1;
  For s = "OVGHK" and t = "RPGUC", the output should be
    createAnagram(s, t) = 4.
"""
def createAnagram(s, t):
    slist = list(s)
    tlist = list(t)
    
    for char in tlist:
        if char in slist:
            slist.remove(char)
    return len(slist)
#     answer = 0
#     sdict = createDict(s)
#     tdict = createDict(t)
#     for key in sdict:
#         if key not in tdict:
#             answer += sdict[key]
#         else:
#             answer += abs(tdict[key] - sdict[key])
#     return answer
# def createDict(string):
#     to_return = {}
#     for char in string:
#         if char in to_return:
#             to_return[char] += 1
#         else:
#             to_return[char] = 1
#     return to_return
