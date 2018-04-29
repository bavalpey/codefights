"""
The longest diagonals of a square matrix are defined as follows:

the first longest diagonal goes from the top left corner to the bottom right one;
the second longest diagonal goes from the top right corner to the bottom left one.
Given a square matrix, your task is to reverse the order of elements on both of its longest diagonals.

Example

For

  matrix = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
the output should be

  reverseOnDiagonals(matrix) = [[9, 2, 7],
                                [4, 5, 6],
                                [3, 8, 1]]
"""
def reverseOnDiagonals(matrix):
    diag1 = []
    diag2 = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row == col:
                diag1.append(matrix[row][col])
                diag2.append(matrix[::-1][row][col])
    diag1 = diag1[::-1]
    diag2 = diag2[::-1]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row == col:
                matrix[row][col] = diag1[row]
                matrix[::-1][row][col] = diag2[row]
    return matrix
