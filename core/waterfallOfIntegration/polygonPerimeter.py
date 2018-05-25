"""
You have a rectangular white board with some black cells. The black cells create a connected black figure, i.e. it is possible to get
from any black cell to any other one through connected adjacent (sharing a common side) black cells.

Find the perimeter of the black figure assuming that a single cell has unit length.

It's guaranteed that there is at least one black cell on the table.

Example

For
  matrix = [[false, true,  true ],
            [true,  true,  false],
            [true,  false, false]]
the output should be
  polygonPerimeter(matrix) = 12.
"""
def polygonPerimeter(matrix):
    peri = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col]:
                if col == 0:
                    peri+=1 + (matrix[row][col+1]==0)
                elif col == len(matrix[row])-1:
                    peri+=1 + (matrix[row][col-1] == 0)
                else:
                    peri += (matrix[row][col-1] == 0) + (matrix[row][col+1]==0)
                if row == 0:
                    peri += 1 +  (matrix[row+1][col]==0)
                elif row == len(matrix)-1:
                    peri+=1 + (matrix[row-1][col] == 0)
                else:
                    peri+=(matrix[row-1][col] == 0) + (matrix[row+1][col]==0)
    return peri
