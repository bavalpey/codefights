"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
  allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
"""
def allLongestStrings(inputArray):
    # longest = len(max(inputArray))
    # for string in inputArray:
    #     if longest > len(string):
    #         inputArray.remove(string)
    # return inputArray
    max_array = []
    max_len = 0
    for string in inputArray:
        if len(string) > max_len:
            max_len = len(string)
    for string in inputArray:
        if len(string) == max_len:
            max_array.append(string)
    return max_array
