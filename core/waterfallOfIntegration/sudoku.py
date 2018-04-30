"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the
nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.
"""
def sudoku(grid):
    box1 = grid[0][:3] + grid[1][:3] + grid[2][:3]
    if len(set(box1)) != 9:
        return False
    box2 = grid[0][3:6] + grid[1][3:6] + grid[2][3:6]
    if len(set(box2)) != 9:
        return False
    box3 = grid[0][6:] + grid[1][6:] + grid[2][6:]
    if len(set(box3)) != 9:
        return False
    box4 = grid[3][:3] + grid[4][:3] + grid[5][:3]
    if len(set(box4)) != 9:
        return False
    box5 = grid[3][3:6] + grid[4][3:6] + grid[5][3:6]
    if len(set(box5)) != 9:
        return False
    box6 = grid[3][6:] + grid[4][6:] + grid[5][6:]
    if len(set(box6)) != 9:
        return False
    box7 = grid[6][:3] + grid[7][:3] + grid[8][:3]
    if len(set(box7)) != 9:
        return False
    box8 = grid[6][3:6] + grid[7][3:6] + grid[8][3:6]
    if len(set(box8)) != 9:
        return False
    box9 = grid[6][6:] + grid[7][6:] + grid[8][6:]
    if len(set(box9)) != 9:
        return False
    row1 = grid[0]
    if len(set(row1)) != 9:
        return False
    row2 = grid[1]
    if len(set(row2)) != 9:
        return False
    row3 = grid[2]
    if len(set(row3)) != 9:
        return False
    row4 = grid[3]
    if len(set(row4)) != 9:
        return False
    row5 = grid[4]
    if len(set(row5)) != 9:
        return False
    row6 = grid[5]
    if len(set(row6)) != 9:
        return False
    row7 = grid[6]
    if len(set(row7)) != 9:
        return False
    row8 = grid[7]
    if len(set(row8)) != 9:
        return False
    row9 = grid[8]
    if len(set(row9)) != 9:
        return False
    col1 = list(i[0] for i in grid)
    if len(set(col1)) != 9:
        return False
    col2 = list(i[1] for i in grid)
    if len(set(col2)) != 9:
        return False
    col3 = list(i[2] for i in grid)
    if len(set(col3)) != 9:
        return False
    col4 = list(i[3] for i in grid)
    if len(set(col4)) != 9:
        return False
    col5 = list(i[4] for i in grid)
    if len(set(col5)) != 9:
        return False
    col6 = list(i[5] for i in grid)
    if len(set(col6)) != 9:
        return False
    col7 = list(i[6] for i in grid)
    if len(set(col7)) != 9:
        return False
    col8 = list(i[7] for i in grid)
    if len(set(col8)) != 9:
        return False
    col9 = list(i[8] for i in grid)
    if len(set(col9)) != 9:
        return False
    
    return True
