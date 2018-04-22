"""
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that
indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a
Minesweeper game setup.

Example

For
  matrix = [[true, false, false],
            [false, true, false],
            [false, false, false]]
the output should be
  minesweeper(matrix) = [[1, 2, 1],
                         [2, 1, 1],
                         [1, 1, 1]]
"""
def addAround(row, col, array):
        if row == 0 and col == 0:
            array[row+1][col+1] += 1
            array[row+1][col] += 1
            array[row][col+1] += 1
        elif row == 0 and col == (len(array[0]) - 1):
            array[row][col-1] += 1
            array[row+1][col-1] += 1
            array[row+1][col] += 1
        elif row == 0:
            array[row][col-1] += 1
            array[row][col+1] += 1
            array[row+1][col-1] += 1
            array[row+1][col] += 1
            array[row+1][col+1] += 1
        elif row == (len(array) - 1) and col == 0:
            array[row-1][col] += 1
            array[row-1][col+1] += 1
            array[row][col+1] += 1
        elif row == (len(array) - 1) and col == (len(array[0]) - 1):
            array[row-1][col] += 1
            array[row-1][col-1] += 1
            array[row][col-1] += 1
        elif row == (len(array) - 1):
            array[row][col-1] += 1
            array[row][col+1] += 1
            array[row-1][col-1] += 1
            array[row-1][col] += 1
            array[row-1][col+1] += 1
        elif col == 0:
            array[row-1][col] += 1
            array[row+1][col] += 1
            array[row-1][col+1] += 1
            array[row][col+1] += 1
            array[row+1][col+1] += 1
        elif col == (len(array[0]) - 1):
            array[row-1][col] += 1
            array[row+1][col] += 1
            array[row-1][col-1] += 1
            array[row][col-1] += 1
            array[row+1][col-1] += 1
        else:
            array[row-1][col-1] += 1
            array[row-1][col] += 1
            array[row-1][col+1] += 1
            array[row][col-1] += 1
            array[row][col+1] += 1
            array[row+1][col-1] += 1
            array[row+1][col] += 1
            array[row+1][col+1] += 1
            
def minesweeper(m):
    d = []
    for i in range(len(m)):
        d.append([0])
        for j in range(1, len(m[i])):
            d[i].append(0)
            
    for i,val1 in enumerate(m):
        for j,dummy in enumerate(val1):
            if True in val1:
                if m[i][j]:
                    addAround(i,j,d)
    return d
