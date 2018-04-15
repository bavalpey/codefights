"""
You have a long strip of paper with integers written on it in a single line from left to right. You wish to cut the paper into exactly three pieces such that each piece contains at least one integer and the sum of the integers in each piece is the same. You cannot cut through a number, i.e. each initial number will unambiguously belong to one of the pieces after cutting. How many ways can you do it?
It is guaranteed that the sum of all elements in the array is divisible by 3.
Example
For a = [0, -1, 0, -1, 0, -1], the output should be
threeSplit(a) = 4.
Here are all possible ways:
    [0, -1] [0, -1] [0, -1]
    [0, -1] [0, -1, 0] [-1]
    [0, -1, 0] [-1, 0] [-1]
    [0, -1, 0] [-1] [0, -1]
"""

def halfsplit(array,amt):
    count = 0
    cur_sum = 0
    for pos,num in enumerate(array[:len(array)-1]):
        cur_sum += num
        if cur_sum == amt:
            print(cur_sum)
            count += 1
    return count

def threeSplit(a):
    summation = sum(a)
    piece = summation/3
    curr_sum = 0
    answer = 0
    for position,number in enumerate(a):
        curr_sum += number
        if curr_sum == piece:
            answer += halfsplit(a[position+1:],piece)
    return answer
