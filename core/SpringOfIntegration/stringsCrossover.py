"""
Define crossover operation over two equal-length strings A and B as follows:

  the result of that operation is a string of the same length as the input strings
  result[i] is either A[i] or B[i], chosen at random
  
Given array of strings inputArray and a string result, find for how many pairs of strings from inputArray the result of the crossover
operation over them may be equal to result.

Note that (A, B) and (B, A) are the same pair. Also note that the pair cannot include the same element of the array twice (however, if
there are two equal elements in the array, they can form a pair).

Example

For inputArray = ["abc", "aaa", "aba", "bab"] and result = "bbb", the output should be
  stringsCrossover(inputArray, result) = 2.
"""
import itertools
def stringsCrossover(inputArray, result):
    a = []
    ans = "0b" + "1"*len(result)
    ans = int(ans,2)
    for i in inputArray:
        this = "0b"
        for pos,char in enumerate(i):
            if char == result[pos]:
                this += "1"
            else:
                this += "0"
        a.append(int(this,2))
    this = itertools.combinations(a,2)
    count = 0
    for pair in this:
        if (pair[0]|pair[1]) == ans:
            count += 1
    return count
