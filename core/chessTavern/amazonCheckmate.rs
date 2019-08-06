/*
An amazon (also known as a queen + knight compound) is an imaginary chess piece that can move like a queen or a knight (or,
equivalently, like a rook, bishop, or knight). The diagram below shows all squares which the amazon can attack from e4 
(circles represent knight-like moves while crosses correspond to queen-like moves).

Recently, you've come across a diagram with only three pieces left on the board: a white amazon, the white king, and the
black king. It's black's move. You don't have time to determine whether the game is over or not, but you'd like to figure
it out in your head. Unfortunately, the diagram is smudged and you can't see the position of the black king, so you'll need
to consider all possible positions.

Given the positions of the white pieces on a standard chessboard (using algebraic notation), your task is to determine the
number of possible black king's positions such that:

  it's checkmate (i.e. black's king is under the amazon's attack and it cannot make a valid move);
  it's check (i.e. black's king is under the amazon's attack but it can reach a safe square in one move);
  it's stalemate (i.e. black's king is on a safe square but it cannot make a valid move);
  black's king is on a safe square and it can make a valid move.
  
Note that two kings cannot be placed on two adjacent squares (including two diagonally adjacent ones).


*/

// The code here reverses the actual positions of the board, but it works nonetheless


fn set_square(row: i32, col: i32, value: i32, board: &mut Vec<Vec<i32>>) {
  match (row, col) {
    (0..=7, 0..=7) => board[row as usize][col as usize] = value,
    _ => (),
  };
}
fn get_square(row: i32, col: i32, board: &Vec<Vec<i32>>) -> Option<i32> {
  match (row, col) {
    (0..=7, 0..=7) => Some(board[row as usize][col as usize]),
    _ => None,
  }
}
fn convert_to_dimension(v: &String) -> (i32, i32) {
  let mut x = v.chars();
  (x.next().unwrap() as i32 - 97, x.next().unwrap().to_digit(10).unwrap() as i32 -1)
}

fn makeUnsafeSquares(k: (i32, i32), a: (i32, i32), mut board: &mut Vec<Vec<i32>>) {
  let mut min_h = 0;
  let mut max_h = 7;
  let mut min_v = 0;
  let mut max_v = 7;
  let mut diagonal = -1;
  if k.0 < a.0 && k.1 == a.1 {
    // if the king is in the same column as the amazon and is above it
    min_h = k.0 + 1;
  } else if k.0 > a.0 && k.1 == a.1 {
    // else, if it is in the same column but below the amazon
    max_h = k.0 - 1;
  } else if k.1 < a.1 && k.0 == a.0 {
    // if the king is in the same row as the amazon and to its left
    min_v = k.1 + 1;
  } else if k.1 > a.1 && k.0 == a.0 {
    max_v = k.1 - 1;
  } else if (a.0-k.0).abs() == (a.1-k.1).abs() {
    if k.0 < a.0 && k.1 < a.1 {
      // upper left
      diagonal = 0;
    } else if k.0 < a.0 && k.1 > a.1 {
      // upper right
      diagonal = 1;
    } else if k.0 > a.0 && k.1 < a.1 {
      // lower left
      diagonal = 2;
    } else if k.0 > a.0 && k.1 > a.1 {
      // lower right
      diagonal = 3;
    }
  }
  
  
  // Horizontal positions
  for i in min_h..=max_h {
    if i != a.0 {
      set_square(i, a.1, 1, &mut board);
    }
  }
  
  // Vertical Positions
  for i in min_v..=max_v {
    if i != a.1 {
      set_square(a.0, i, 1, &mut board);
    }
  }
  // Knight positions
  let knight_moves = vec![(-2, 1), (-1, 2), (2, 1), (1, 2), (-2, -1), (-1, -2), (2, -1), (1, -2)];
  for i in knight_moves {
    set_square(a.0+i.0, a.1+i.1, 1, &mut board);
  }
  
  // diagonals
  for i in 0..=7 {
    for j in 0..=7 {
      if (a.0-i).abs() == (a.1-j).abs() {
        let mut flag: bool = true;
        
        // Sequence of ifs to check if tile is on same diagonal
        //  as queen and the king blocks the path
        if diagonal == 0 && i < a.0 && j < a.1 {
          if i < k.0 && j < k.1 {
            flag = false;
          }
        } else if diagonal == 1 && i < a.0 && j > a.1 {
          if i < k.0 && j > k.1 {
            flag = false;
          }
        } else if diagonal == 2 && i > a.0 && j < a.1 {
          if i > k.0 && j < k.1 {
            flag = false;
          }
        } else if diagonal == 3 && i > a.0 && j > a.1 {
          if i > k.0 && j > k.1 {
            flag = false;
          }
        }
        
        if flag {
          set_square(i,j,1,&mut board);
        }
      }
    }
  }
  
  board[a.0 as usize][a.1 as usize] = 4;
  
  for i in -1..=1 {
    for j in -1..=1 {
      set_square(k.0+i, k.1+j, 5, &mut board);
    }
  }
}

fn get_vec_of_moves(row: i32, col: i32, board: &Vec<Vec<i32>>) -> Vec<i32> {
  let mut moves: Vec<i32> = Vec::new();
  for i in -1..=1 {
    for j in -1..=1 {
      if ! (i == 0 && j == 0) {
        match get_square(row+i, col+j, &board) {
          Some(n) => moves.push(n),
          None => (),
        };
      }
    }
  }
  moves
}
fn amazonCheckmate(king: String, amazon: String) -> Vec<i32> {
  let k = convert_to_dimension(&king);
  let a = convert_to_dimension(&amazon);
  
  let mut board = vec![vec![4;8];8];
  let mut ans = vec![0;4];
  
  // first, label all of the squares that are unsafe to move to
  makeUnsafeSquares(k, a, &mut board);
  
  // now, label each square
  for row in 0..=7 {
    for col in 0..=7 {
      // sq_val is the state of the tile that the black king is on
      let sq_val = board[row as usize][col as usize];
      
      // if the tile is a square that the black king cannot be on
      if sq_val == 5 || (row == a.0 && col == a.1) {
        continue;
      }
      let moves = get_vec_of_moves(row, col, &board);
      // if the king can move to a safe space
      if moves.contains(&4) {
        // and it is currently safe
        if sq_val == 4 {
          // Then it is in a safe square and can make a valid move
          ans[3] += 1;
        } else {
          // Otherwise, if it is not in a safe space, but can move to one,
          //  it is in check
          ans[1] += 1;
        }
      } else if sq_val == 4 {
        // If there are no safe spaces to move to, but the king is safe,
        //   Stalemate
        ans[2] += 1;
      } else {
        // Otherwise, checkmate
        ans[0] += 1;
      }
    }
  }
  ans
}
