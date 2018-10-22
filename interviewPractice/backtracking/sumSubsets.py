"""
Given a sorted array of integers arr and an integer num, find all possible unique subsets of arr that add up to num. Both the array of
subsets and the subsets themselves should be sorted in lexicographical order.

Example
  For arr = [1, 2, 3, 4, 5] and num = 5, the output should be
    sumSubsets(arr, num) = [[1, 4], [2, 3], [5]].
"""
def sumSubsets(arr, num):
  if num == 0:
    return [[]]
  ans = []
  ttl = sum(arr)
  def tryS(pos,sm,ttl,taken):
    if pos >= len(arr):
      return
    if sm + arr[pos] == num:
      ans.append(taken+[arr[pos]])
      return
    if arr[pos] + sm > num:
      return
    if arr[pos]+sm + ttl < num:
      return
    else:
      tryS(pos+1,sm+arr[pos],ttl-arr[pos],taken+[arr[pos]])
      val = arr[pos]
      while(val == arr[pos] and pos < len(arr)-1):
        pos +=1
      tryS(pos,sm,ttl-arr[pos],taken)
  tryS(0,0,ttl,[])
  return ans
