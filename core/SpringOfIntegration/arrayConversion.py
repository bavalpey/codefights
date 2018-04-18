"""
Given an array of 2^k integers (for some integer k), perform the following operations until the array contains only one element:

  On the 1st, 3rd, 5th, etc. iterations (1-based) replace each pair of consecutive elements with their sum;
  On the 2nd, 4th, 6th, etc. iterations replace each pair of consecutive elements with their product.
  
After the algorithm has finished, there will be a single element left in the array. Return that element.

Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8], the output should be
  arrayConversion(inputArray) = 186.

We have [1, 2, 3, 4, 5, 6, 7, 8] -> [3, 7, 11, 15] -> [21, 165] -> [186], so the answer is 186.
"""
def arrayConversion(inputArray):
    count = 1
    while len(inputArray) > 1:
        newArray = list(zip(inputArray[::2],inputArray[1::2]))
        print(newArray)
        inputArray = []
        for pair in newArray:
            if count % 2:
                inputArray.append(pair[0]+pair[1])
            else:
                inputArray.append(pair[0]*pair[1])
        count += 1
    return inputArray[0]
