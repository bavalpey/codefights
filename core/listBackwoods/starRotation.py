"""
Consider a (2k+1) × (2k+1) square subarray of an integer integers matrix. Let's call the union of the square's two longest diagonals,
middle column and middle row a star. Given the coordinates of the star's center in the matrix and its width, rotate it 45 · t degrees
clockwise preserving position of all matrix elements that do not belong to the star.

Example

  For

    matrix = [[1, 0, 0, 2, 0, 0, 3],
              [0, 1, 0, 2, 0, 3, 0],
              [0, 0, 1, 2, 3, 0, 0],
              [8, 8, 8, 9, 4, 4, 4],
              [0, 0, 7, 6, 5, 0, 0],
              [0, 7, 0, 6, 0, 5, 0],
              [7, 0, 0, 6, 0, 0, 5]]
  width = 7, center = [3, 3] and t = 1, the output should be
    starRotation(matrix, width, center, t) = [[8, 0, 0, 1, 0, 0, 2],
                                              [0, 8, 0, 1, 0, 2, 0],
                                              [0, 0, 8, 1, 2, 0, 0],
                                              [7, 7, 7, 9, 3, 3, 3],
                                              [0, 0, 6, 5, 4, 0, 0],
                                              [0, 6, 0, 5, 0, 4, 0],
                                              [6, 0, 0, 5, 0, 0, 4]]
  For

    matrix = [[1, 0, 0, 2, 0, 0, 3],
              [0, 1, 0, 2, 0, 3, 0],
              [0, 0, 1, 2, 3, 0, 0],
              [8, 8, 8, 9, 4, 4, 4],
              [0, 0, 7, 6, 5, 0, 0]]
  width = 3, center = [1, 5] and t = 81, the output should be
    starRotation(matrix, width, center, t) = [[1, 0, 0, 2, 0, 0, 0],
                                              [0, 1, 0, 2, 3, 3, 3],
                                              [0, 0, 1, 2, 0, 0, 0],
                                              [8, 8, 8, 9, 4, 4, 4],
                                              [0, 0, 7, 6, 5, 0, 0]]
"""
def starRotation(matrix, width, center, t):
    r = center[0]
    c = center[1]
    t %= 8
    if t == 0:
        return matrix
    while t != 0:
        t-=1
        for i in range(1,math.ceil(width/2)):
            temp = matrix[r-i][c-i]
            matrix[r-i][c-i] = matrix[r][c-i]
            temp2 = matrix[r-i][c]
            matrix[r-i][c] = temp
            temp = matrix[r-i][c+i]
            matrix[r-i][c+i] = temp2
            temp2 = matrix[r][c+i]
            matrix[r][c+i] = temp
            temp = matrix[r+i][c+i]
            matrix[r+i][c+i] = temp2
            temp2 = matrix[r+i][c]
            matrix[r+i][c] = temp
            temp = matrix[r+i][c-i]
            matrix[r+i][c-i] = temp2
            temp2 = matrix[r][c-i]
            matrix[r][c-i] = temp
            matrix[r-i][c-i] = temp2
    return matrix
