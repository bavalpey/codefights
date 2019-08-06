/*
Consider a bishop, a knight and a rook on an n × m chessboard. They are said to form a triangle if each piece attacks exactly
one other piece and is attacked by exactly one piece. Calculate the number of ways to choose positions of the pieces to form
a triangle.

Note that the bishop attacks pieces sharing the common diagonal with it; the rook attacks in horizontal and vertical
directions; and, finally, the knight attacks squares which are two squares horizontally and one square vertically, or two
squares vertically and one square horizontally away from its position.

Example

For n = 2 and m = 3, the output should be
  chessTriangle(n, m) = 8.
*/

fn c(n: i32) -> i32 {
  // Checker function that coerces non-positive integers to 0.
  if n < 1 {
    return 0;
  }
  n
}

fn chessTriangle(n: i32, m: i32) -> i32 {
  // This is a really weird problem to include in here.
  // Solutions are either going to be brute-force, or, one can work out the math
  // and determine that there are only
  
  // these are the dimensions of all of the distinct triangles (plus more for reverse)
  let configurations = vec![(2, 3), (2, 4), (3, 3), (3, 4)];
  
  
  configurations.iter().fold(0, |mut x, v| {
    {
      // Here, determine how many ways the triangle can appear on the board
      // For instance, if the board is a 3x3, and we are looking at a triangle of
      // dimension 2x3, there are two choices for consecutive rows
      //  and one choice for consecutive columns, so there are a total of 8
      // However, dimension 2x3 is also
      x += 8 * (c(n - v.0 + 1) * c(m - v.1 + 1) + c(n - v.1 + 1) * c(m - v.0 + 1));
      x
    }
  })
}
