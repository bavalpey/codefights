"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
"""
def allLongestStrings(inputArray):
    mx = len(max(inputArray, key=len))
    return list(i for i in inputArray if len(i) == mx)
