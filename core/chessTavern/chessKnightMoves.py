"""
Duplicate of intro level 11
"""

def chessKnightMoves(cell):
    moves = 8
       
    
    if cell[0] in ['a','h']:
        moves -= 4
        if cell[1] in ['1','8']:
            moves -= 2
        elif cell[1] in ['2','7']:
            moves -= 1
    
    elif cell[0] in ['b','g']:
        moves -= 2
        if cell[1] in ['1','8']:
            moves -= 3
        elif cell[1] in ['2','7']:
            moves -= 2
    else:
        if cell[1] in ['1','8']:
            moves -= 4
        elif cell[1] in ['2','7']:
            moves -= 2
    
    return moves
