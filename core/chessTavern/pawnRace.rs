/*
Pawn race is a game for two people, played on an ordinary 8 × 8 chessboard. The first player has a white pawn, the second
one - a black pawn. Initially the pawns are placed somewhere on the board so that the 1st and the 8th rows are not occupied.
Players take turns to make a move.

White pawn moves upwards, black one moves downwards. The following moves are allowed:

  * one-cell move on the same vertical in the allowed direction;

  * two-cell move on the same vertical in the allowed direction, if the pawn is standing on the 2nd (for the white pawn) or 
  the 7th (for the black pawn) row. Note that even with the two-cell move a pawn can't jump over the opponent's pawn;

  * capture move one cell forward in the allowed direction and one cell to the left or to the right.


The purpose of the game is to reach the the 1st row (for the black pawn) or the 8th row (for the white one), or to capture
the opponent's pawn.

Given the initial positions and whose turn it is, determine who will win or declare it a draw (i.e. it is impossible for any
player to win). Assume that the players play optimally.

Example

  For white = "e2", black = "e7", and toMove = 'w', the output should be
    pawnRace(white, black, toMove) = "draw";
    
  For white = "e3", black = "d7", and toMove = 'b', the output should be
    pawnRace(white, black, toMove) = "black";
    
  For white = "a7", black = "h2", and toMove = 'w', the output should be
    pawnRace(white, black, toMove) = "white".
    
*/

// I wrote an essentially brute-force solution that I am not exactly proud of
//  There is most likely a more elegant way to do this.

#[derive(Debug)]
struct Point {
  x: i32,
  y: i32,
}


fn pawnRace(white: String, black: String, toMove: char) -> String {
  let w_wins = String::from("white");
  let b_wins = String::from("black");
  let whiteMove = match toMove {
    'w' => true,
    _ => false,
  };
    
  let white = {
    let mut w_iter = white.chars();
    Point {x: w_iter.next().unwrap() as i32 - 97, y: w_iter.next().unwrap().to_digit(10).unwrap() as i32 - 1}
  };
  
  let black = {
    let mut b_iter = black.chars();
    Point {x: b_iter.next().unwrap() as i32 - 97, y: b_iter.next().unwrap().to_digit(10).unwrap() as i32 - 1}
  };
  


  let w_dist = match white.y {
    1 => 5,
    _ => 7-white.y,
  };
  
  let b_dist = match black.y {
    6 => 5,
    _ => black.y
  };
  
  if black.x == white.x && white.y < black.y{
    return String::from("draw");
  } else if white.y >= black.y || (white.x-black.x).abs() != 1 {
    if w_dist == b_dist {
      if whiteMove {
        return w_wins
      }
      return b_wins
    } else if w_dist < b_dist{
      return w_wins
    } else {
      return b_wins
    }
  } else if (white.x - black.x).abs() == 1 {
    if black.y-white.y == 1 {
      if whiteMove {
        return w_wins
      }
      return b_wins
    }
    if black.y == 6 && white.y == 1 {
      if whiteMove {
        return b_wins
      }
      return w_wins
    } else if (black.y == 5 && white.y == 1) {
      return w_wins
    } else if (black.y == 6 && white.y == 2){
      return b_wins
    } else if (black.y == 6 && white.y == 3) {
      if whiteMove {
        return w_wins
      }
      return b_wins
    } else if black.y == 4 && white.y == 1 {
      if whiteMove {
        return w_wins
      }
      return b_wins
    } else if (black.y == 3 && white.y == 1) || (black.y == 6 && white.y == 4){
      if whiteMove {
        return b_wins
      }
      return w_wins
    } else if (black.y == 5 && white.y == 2) {
      if whiteMove {
        return w_wins
      }
      return b_wins
    } else if (black.y == 5 && white.y == 3) {
      if whiteMove {
        return b_wins
      }
      return w_wins
    }
  }
}
