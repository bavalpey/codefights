"""
Sort the letters in the string s by the order they occur in the string t.

Example
  For s = "weather" and t = "therapyw", the output should be
    sortByString(s, t) = "theeraw";

  For s = "good" and t = "odg", the output should be
    sortByString(s, t) = "oodg".
"""
def sortByString(s, t):
  if len(s) <= 1:
    return s
  print(t.find(s[0]))
  return "".join(sorted(s,key=lambda x: t.find(x)))
