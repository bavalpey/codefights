"""
Given a character, check if it represents an odd digit, an even digit or not a digit at all.

Example

  For symbol = '5', the output should be
  characterParity(symbol) = "odd";
  For symbol = '8', the output should be
  characterParity(symbol) = "even";
  For symbol = 'q', the output should be
  characterParity(symbol) = "not a digit".
"""
def characterParity(symbol):
    try:
        symbol = int(symbol)
        if symbol % 2:
            return "odd"
        else:
            return "even"
    except:
        return "not a digit"
