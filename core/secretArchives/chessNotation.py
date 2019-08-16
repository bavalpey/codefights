"""
John has always had trouble remembering chess game positions. To help himself with remembering, he decided to store game
positions in strings. He came up with the following position notation:

The notation is built for the current game position row by row from top to bottom, with '/' separating each row notation;
Within each row, the contents of each square are described from the leftmost column to the rightmost;
Each piece is identified by a single letter taken from the standard English names ('P' = pawn, 'N' = knight, 'B' = bishop, 'R'
= rook, 'Q' = queen, 'K' = king);
White pieces are designated using upper-case letters ("PNBRQK") while black pieces use lowercase ("pnbrqk");
Empty squares are noted using digits 1 through 8 (the number of empty squares from the last piece);
Empty lines are noted as "8".

John has written down some positions using his notation, and now he wants to rotate the board 90 degrees clockwise and see
what notation for the new board would look like. Help him with this task.

Example

For notation = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR", the output should be
  chessNotation(notation) = "RP4pr/NP4pn/BP4pb/QP4pq/K2P2pk/BP4pb/NP4pn/RP4pr".

The notation corresponds to the initial position with one move made (white pawn from e2 to e4).
So, the notation of the new position is "RP4pr/NP4pn/BP4pb/QP4pq/K2P2pk/BP4pb/NP4pn/RP4pr".
"""

# Here's an example of why code golf just breeds bad coding habits.  How readable is this code?
# I could easily have split up these statements into their own line.  There's so much going on in one line here.
def chessNotation(notation):
  return re.sub('_*', lambda x: str(len(x.group()) if len(x.group()) != 0 else ''), '/'.join([''.join([c[i] for c in \
    re.sub('\d',lambda x: '_'*int(x.group()), notation).split("/")[::-1]]) for i in range(8)]))
  
  
