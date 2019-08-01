/*
We're going to store numbers in a tree. Each node in this tree will store a single digit (from 0 to 9), and each path from
root to leaf encodes a non-negative integer.

Given a binary tree t, find the sum of all the numbers encoded in it.

Example

  For
    t = {
        "value": 1,
        "left": {
            "value": 0,
            "left": {
                "value": 3,
                "left": null,
                "right": null
            },
            "right": {
                "value": 1,
                "left": null,
                "right": null
            }
        },
        "right": {
            "value": 4,
            "left": null,
            "right": null
        }
    }
    
  the output should be
    digitTreeSum(t) = 218.
  
  There are 3 numbers encoded in this tree:
    Path 1->0->3 encodes 103
    Path 1->0->1 encodes 101
    Path 1->4 encodes 14
    and their sum is 103 + 101 + 14 = 218.
  
  
  For 
    t = {
        "value": 0,
        "left": {
            "value": 9,
            "left": null,
            "right": null
        },
        "right": {
            "value": 9,
            "left": {
                "value": 1,
                "left": null,
                "right": null
            },
            "right": {
                "value": 3,
                "left": null,
                "right": null
            }
        }
    }
    
  the output should be
    digitTreeSum(t) = 193.
    
  Because 09 + 091 + 093 = 193
*/

fn create_digits(t: TreeNode<i32>) -> Vec<String> {
  // Turns the tree into vectors of strings representing digits of the tree
  
  // unwrap the value since it is boxed
  let t = *t.unwrap();
  // convert integer value to a string
  let re = t.value.to_string();

  // create a vec that will hold the vector of new strings
  let mut ans: Vec<String> = Vec::new();

  // Now, if left is not none, we want to recurse on it and then concatenate this value with each value from its output
  if let Some(l) = t.left {
    let left = create_digits(Some(l));
    // One way is to iterate through the source vector
    for s in left {
      ans.push(re.clone() + &s);
    }
    
  if let Some(l) = t.right {
    let right = create_digits(Some(l));
    // Another is to use functional techniques to fold the old vector into a new one, then extend the original
    ans.extend(right.iter().fold(Vec::new(), |mut j, s| {
    {j.push(re.clone() + &s);} j
    }));
  }
    
}
  
  // This could have been done with a premature return statement, but here for simplicity.
  
  match ans.as_slice() {
    [] => vec![re],  // if the vector is empty, then return a new vector containing only the current node's value
    _ => ans,  // otherwise, return the newly created vector
  }

}

fn digitTreeSum(t: TreeNode<i32>) -> i64 {
  
  let digits = create_digits(t);  // begin recursion on tree
  
  // Fold (which works like Python's reduce) the vector, parsing each string into an integer and computing the sum.
  digits.iter().fold(0, |mut n, s| {
      {n += s.parse::<i64>().unwrap();} n
  })
}
