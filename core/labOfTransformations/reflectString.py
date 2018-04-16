"""
Define an alphabet reflection as follows: a turns into z, b turns into y, c turns into x, ..., n turns into m, m turns into n, ...,
z turns into a.

Define a string reflection as the result of applying the alphabet reflection to each of its characters.

Reflect the given string.

Example

For inputString = "name", the output should be
  reflectString(inputString) = "mznv".
"""
def reflectString(i):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    my_dict = {}
    for pos,j in enumerate(alphabet):
        my_dict[j] = alphabet[::-1][pos]
    ans = ""
    for char in i:
        ans += my_dict[char]
    return ans
