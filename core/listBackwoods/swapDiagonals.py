"""
The longest diagonals of a square matrix are defined as follows:

  the first longest diagonal goes from the top left corner to the bottom right one;
  the second longest diagonal goes from the top right corner to the bottom left one.
  
Given a square matrix, your task is to swap its longest diagonals by exchanging their elements at the corresponding positions.

Example

For

  matrix = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
the output should be

  swapDiagonals(matrix) = [[3, 2, 1],
                           [4, 5, 6],
                           [9, 8, 7]]
"""
def swapDiagonals(matrix):
    diag1 = []
    diag2 = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row == col:
                diag1.append(matrix[row][col])
                diag2.append(matrix[::-1][row][col])
    diag2 = diag2[::-1]
    diag1 = diag1[::-1]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row == col:
                matrix[row][col] = diag2[row]
                matrix[::-1][row][col] = diag1[row]
    return matrix
