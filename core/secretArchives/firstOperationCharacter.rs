/*
Given a string which represents a valid arithmetic expression, find the index of the character in the given expression 
corresponding to the arithmetic operation which needs to be computed first.

Note that several operations of the same type with equal priority are computed from left to right.

See the explanation of the third example for more details about the operations priority in this problem.

Example

  For expr = "(2 + 2) * 2", the output should be
    firstOperationCharacter(expr) = 3.

  There are two operations in the expression: + and *. The result of + should be computed first, since it is enclosed in 
  parentheses. Thus, the output is the index of the '+' sign, which is 3.

  For expr = "2 + 2 * 2", the output should be
    firstOperationCharacter(expr) = 6.

  There are two operations in the given expression: + and *. Since there are no parentheses, * should be computed first as it 
  has higher priority. The answer is the position of '*', which is 6.

  For expr = "((2 + 2) * 2) * 3 + (2 + (2 * 2))", the output should be firstOperationCharacter(expr) = 28.

  There are two operations which are enclosed in two parentheses: + at the position 4, and * at the position 28. Since * has 
  higher priority than +, the answer is 28.
  
*/

fn firstOperationCharacter(expr: String) -> i32 {
  let mut parenCount = 0;
  let mut maxParenCount = -1;
  let mut maxPos = 0;
  let mut plusExpression = false;
  
  for (pos, i) in expr.chars().enumerate(){
    if i == '(' {
      parenCount += 1;
    } else if i == ')' {
      parenCount -= 1;
    } else if i != '+' && i != '*' {
      continue;
    } else {
      if parenCount > maxParenCount || (parenCount == maxParenCount && plusExpression){
        if i == '*' {
          plusExpression = false;
          maxPos = pos;
          maxParenCount = parenCount;
        } else if i == '+' && maxParenCount != parenCount{
          plusExpression = true;
          maxPos = pos;
          maxParenCount = parenCount;
        }
      }
    }
  }
  
  maxPos as i32
}
