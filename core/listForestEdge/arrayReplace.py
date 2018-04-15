"""
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

Example

For inputArray = [1, 2, 1], elemToReplace = 1 and substitutionElem = 3, the output should be
  arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
"""
def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for i,x in enumerate(inputArray):
        if x == elemToReplace:
            inputArray[i] = substitutionElem
    return inputArray
