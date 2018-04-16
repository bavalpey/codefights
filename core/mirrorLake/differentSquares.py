"""
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

  matrix = [[1, 2, 1],
            [2, 2, 2],
            [2, 2, 2],
            [1, 2, 3],
            [2, 2, 1]]
the output should be
  differentSquares(matrix) = 6.

Here are all 6 different 2 × 2 squares:

  1 2
  2 2
  2 1
  2 2
  2 2
  2 2
  2 2
  1 2
  2 2
  2 3
  2 3
  2 1
"""
def differentSquares(matrix):
    if len(matrix) < 2:
        return 0
    elif len(matrix[0]) < 2:
        return 0
    answer = []
    for row,i in enumerate(matrix[:-1]):
        for col, num in enumerate(i[:-1]):
            j = []
            j.append(num)
            j.append(matrix[row][col+1])
            j.append(matrix[row+1][col])
            j.append(matrix[row+1][col+1])
            if j not in answer:
                answer.append(j)
    return len(answer)
