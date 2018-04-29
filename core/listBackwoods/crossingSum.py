"""
Given a rectangular matrix and integers a and b, consider the union of the ath row and the bth (both 0-based) column of the matrix (i.e.
all cells that belong either to the ath row or to the bth column, or to both). Return sum of all elements of that union.

Example

For

  matrix = [[1, 1, 1, 1], 
            [2, 2, 2, 2], 
            [3, 3, 3, 3]]
a = 1 and b = 3, the output should be
  crossingSum(matrix, a, b) = 12.

Here (2 + 2 + 2 + 2) + (1 + 3) = 12.
"""
def crossingSum(matrix, a, b):
    sm = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row == a:
                sm += matrix[row][col]
            elif col == b:
                sm += matrix[row][col]
    return sm
