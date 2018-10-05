"""
Given an encoded string, return its corresponding decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. Note: k is
guaranteed to be a positive integer.

Note that your solution should have linear complexity because this is what you will be asked during an interview.

Example
  For s = "4[ab]", the output should be
    decodeString(s) = "abababab";

  For s = "2[b3[a]]", the output should be
    decodeString(s) = "baaabaaa";

  For s = "z1[y]zzz2[abc]", the output should be
    decodeString(s) = "zyzzzabcabc".
"""
def decodeString(s):
  if len(s) < 2:
    return s
  if s[0].isalpha():
    return s[0] + decodeString(s[1:])
  j = s.find("[")
  if j:
    matched = 0
    indx = j
    for char in s[j+1:]:
      if matched == 0 and char == ']':
        break
      if char == "[":
        matched += 1
      elif char == "]":
        matched -= 1
      indx+=1
    return int(s[:j]) * decodeString(s[j+1:indx+1]) + decodeString(s[indx+2:])
  else:
    return s
