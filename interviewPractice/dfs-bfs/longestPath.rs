/*
Suppose we represent our file system as a string. For example, the string "user\n\tpictures\n\tdocuments\n\t\tnotes.txt"
represents:

  user
      pictures
      documents
          notes.txt
          
The directory user contains an empty sub-directory pictures and a sub-directory documents containing a file notes.txt.

The string "user\n\tpictures\n\t\tphoto.png\n\t\tcamera\n\tdocuments\n\t\tlectures\n\t\t\tnotes.txt" represents:

  user
      pictures
          photo.png
          camera
      documents
          lectures
              notes.txt
              
              
The directory user contains two sub-directories pictures and documents. pictures contains a file photo.png and an empty
second-level sub-directory camera. documents contains a second-level sub-directory lectures containing a file notes.txt.

We want to find the longest (as determined by the number of characters) absolute path to a file within our system. For
example, in the second example above, the longest absolute path is "user/documents/lectures/notes.txt", and its length is
33 (not including the double quotes).

Given a string representing the file system in this format, return the length of the longest absolute path to a file in
the abstracted file system. If there is not a file in the file system, return 0.

Note: Due to system limitations, test cases use form feeds ('\f', ASCII code 12) instead of newline characters.

Example

For fileSystem = "user\f\tpictures\f\tdocuments\f\t\tnotes.txt", the output should be
  longestPath(fileSystem) = 24.

The longest path is "user/documents/notes.txt", and it consists of 24 characters.
*/

use std::cmp;
fn longestPath(fileSystem: String) -> i32 {
  
  // Since codefights does not give rust access to its regex crate, this is going to be a bit wonky
  
  
  // Test cases are sneaky, 4 spaces should be equivalent to a tab.
  let res = str::replace(&fileSystem, "    ", "\t");
  
  // Files will store the sizes of each file (anything that has a . in the string)
  let mut files: Vec<usize> = Vec::new();
  
  // Create a vector to store the strings of each
  let mut paths: Vec<String> = Vec::new();
  
  // Hold all characters that have been read until a newline.
  let mut curString = String::new();
  let mut depth = 0;
  
  for c in res.chars() {
    match c {
      '\t' => depth +=1, // keep track of the depth to resize paths upon reaching a newline
      '\u{000C}' | '\n' => { // It is ambiguos whether the newline is a formfeed or
        if curString.contains(".") {
          // if the depth is 0, there is no leading '/' in the filename, so check for this
          let extra = match depth {
            0 => 0,
            _ => 1,
          };
          files.push(curString.len() + paths[0..depth].join("/").len() + extra);
          curString.clear();
          depth = 0;
        } else {
          paths.resize(depth, String::from(""));
          paths.push(curString.clone());
          curString.clear();
          depth = 0;
          
        }
      },
      _ => curString.push(c),
    }
    
  }
  if curString.contains("."){
  
    let extra = match depth {
            0 => 0,
            _ => 1,
    };
    files.push(curString.len() + paths[0..depth].join("/").len() + extra);

  }
  
  if files.len() > 0 {
    return files.iter().fold(0, |mut n, s| {
      {n = cmp::max(n, *s as i32);} n
    });
  }
  0
  
}
