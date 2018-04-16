"""
Determine whether the given string can be obtained by one concatenation of some string to itself.

Example

  For inputString = "tandemtandem", the output should be
    isTandemRepeat(inputString) = true;
  For inputString = "qqq", the output should be
      isTandemRepeat(inputString) = false;
  For inputString = "2w2ww", the output should be
      isTandemRepeat(inputString) = false.
"""
def isTandemRepeat(inputString):
    length = len(inputString)
    if length % 2:
        return False
    if inputString[:length//2] == inputString[length//2:]:
        return True
    return False
