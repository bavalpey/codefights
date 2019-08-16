=begin
You've been invited to a job interview at a famous company that tests programming challenges. To evaluate your coding skills, 
they have asked you to parse a given problem's input given as an inputString string, and count the number of primitive type 
elements within it.

The inputString can be either a primitive type variable or an array (possibly multidimensional) that contains elements of the 
primitive types.
A primitive type variable can be:

  an integer number;
  a string, which is surrounded by " characters (note that it may contain any character except ");
  a boolean, which is either true or false.

Return the total number of primitive type elements inside inputString.

Example

  For inputString = "[[0, 20], [33, 99]]", the output should be
    countElements(inputString) = 4;
  For inputString = "[ "one", 2, "three" ]", the output should be
    countElements(inputString) = 3;
  For inputString = "true", the output should be
    countElements(inputString) = 1;
  For inputString = "[[1, 2, [3]], 4]", the output should be
    countElements(inputString) = 4.
=end

def countElements(inputString)
  pattern = /"[^"]*+"|true|false|\d+/
  inputString.scan(pattern).length()
end
