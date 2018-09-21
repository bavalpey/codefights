"""
Given an array of strings, sort them in the order of increasing lengths. If two strings have the same length, their relative order must
be the same as in the initial array.

Example

  For
    inputArray = ["abc",
                  "",
                  "aaa",
                  "a",
                  "zz"]
                  
  the output should be
    sortByLength(inputArray) = ["",
                                "a",
                                "zz",
                                "abc",
                                "aaa"]
"""
def sortByLength(inputArray):
  return sorted(inputArray, key=lambda x: len(x))
