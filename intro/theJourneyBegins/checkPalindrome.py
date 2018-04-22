"""
Given the string, check if it is a palindrome.

Example

  For inputString = "aabaa", the output should be
    checkPalindrome(inputString) = true;
  For inputString = "abac", the output should be
    checkPalindrome(inputString) = false;
  For inputString = "a", the output should be
    checkPalindrome(inputString) = true.
"""
def checkPalindrome(inputString):
    my_string = list(inputString)
    str_length = len(my_string)
    j = str_length
    for i in range(str_length):
        j -= 1
        if my_string[i] != my_string[j]:
            return False
    return True
