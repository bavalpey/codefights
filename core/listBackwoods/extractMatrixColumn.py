"""
Given a rectangular matrix and an integer column, return an array containing the elements of the columnth column of the given matrix (the
leftmost column is the 0th one).

Example

For

  matrix = [[1, 1, 1, 2], 
            [0, 5, 0, 4], 
            [2, 1, 3, 6]]
and column = 2, the output should be
  extractMatrixColumn(matrix, column) = [1, 0, 3].
"""
def extractMatrixColumn(matrix, column):
    ans = []
    for i in matrix:
        ans.append(i[column])
    return ans
