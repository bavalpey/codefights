"""
Given an array of integers a and an integer sum, find all of the unique combinations in a that add up to sum.
The same number from a can be used an unlimited number of times in a combination.
Elements in a combination (a1 a2 … ak) must be sorted in non-descending order, while the combinations themselves must be sorted in 
ascending order.
If there are no possible combinations that add up to sum, the output should be the string "Empty".
Example
  For a = [2, 3, 5, 9] and sum = 9, the output should be
    combinationSum(a, sum) = "(2 2 2 3)(2 2 5)(3 3 3)(9)".
"""
def combinationSum(arr, num):
  arr = set(arr)
  arr = sorted(arr)
  if num == 0:
    return [[]]
  ans = []
  def tryS(pos,sm,taken):
    if pos >= len(arr):
      return
    if sm + arr[pos] == num:
      ans.append("(" + " ".join([str(i) for i in (taken+[arr[pos]])]) + ")")
      return
    if arr[pos] + sm > num:
      return
    cntitem = 1
    while not (sm + arr[pos]*cntitem > num):
      if sm + arr[pos]*cntitem == num:
         ans.append("(" + " ".join([str(i) for i in (taken+[arr[pos]]*cntitem)]) + ")")
      tryS(pos+1,sm+(cntitem*arr[pos]),taken+[arr[pos]]*cntitem)
      cntitem +=1
    tryS(pos+1,sm,taken)
  tryS(0,0,[])
  if len(ans) == 0:
    return "Empty"
  return "".join(sorted(ans))
