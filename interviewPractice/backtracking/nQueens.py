"""
In chess, queens can move any number of squares vertically, horizontally, or diagonally. The n-queens puzzle is the problem of placing
n queens on an n × n chessboard so that no two queens can attack each other.

Given an integer n, print all possible distinct solutions to the n-queens puzzle. Each solution contains distinct board configurations 
of the placement of the n queens, where the solutions are arrays that contain permutations of [1, 2, 3, .. n]. The number in the ith 
position of the results array indicates that the ith column queen is placed in the row with that number. In your solution, the board 
configurations should be returned in lexicographical order.

Example
  For n = 1, the output should be
  nQueens(n) ]];

  For n = 4, the output should be
      nQueens(n) = [[2, 4, 1, 3],
                  [3, 1, 4, 2]]
"""
def nQueens(n):
  def isValidSet(arr):
    for row,col in enumerate(arr,1):
      for row1,col1 in enumerate(arr,1):
        if row1 == row and col == col1:
          pass
        elif col == col1:
          return False
        elif abs(row-row1) == abs(col-col1):
          return False
    return True
  ans = []
  def makeAns(arr):
    if len(arr) == n and isValidSet(arr):
      ans.append(arr)
      return
    for i in range(1,n+1):
      if isValidSet(arr + [i]):
        makeAns(arr+[i])
  makeAns([])
  return ans
