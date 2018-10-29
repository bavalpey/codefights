"""
udoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and 
each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules 
described above. Note that the puzzle represented by grid does not have to be solvable.

Example

  For
    grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
            ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
            ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
            ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
            ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
            ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
            ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
  the output should be
    sudoku2(grid) = true;

  For
    grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
            ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
            ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
            ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
            ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
            ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
            ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
            ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
  the output should be
    sudoku2(grid) = false.
  The given grid is not correct because there are two 1s in the second column. Each column, each row, and each 3 × 3 subgrid can only
  contain the numbers 1 through 9 one time.
"""
def sudoku2(grid):
  # this solution uses hash tables to keep track of values that have been seen before
  # I want this solution to only have to iterate through the array once
  # I also do not want to complicate things by using numpy, although use of numpy will most likely increase performance
  keys = list(range(0,9))
  vals = list(str(i) for i in range(1,10))
  mkDict = lambda : dict(zip(keys,list(dict(zip(vals,[False]*9)) for i in range(9)))) # Instead of toying around with deepcopy
  # I just made a simple function which sets up the dictionary how I want it.
  colDict = mkDict()
  cellDict = mkDict()
  rowDict = mkDict()
  getCell = lambda r,c: 3*(r//3)+(c//3) # this function will return the cell of the row,col combination

  for row,rowList in enumerate(grid):
    for col,item in enumerate(rowList):
      if item == '.':
        continue
      cell = getCell(row,col)
      if cellDict[cell][item] or rowDict[row][item] or colDict[col][item]:
        return False
      colDict[col][item] = cellDict[cell][item] = rowDict[row][item] = True # udpate the dicts for the value we just saw
  return True
  
