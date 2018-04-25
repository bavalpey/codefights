"""
You're given a substring s of some cyclic string. What's the length of the smallest possible string that can be concatenated to itself
many times to obtain this cyclic string?

Example

For s = "cabca", the output should be
  cyclicString(s) = 3.
"cabca" is a substring of a cycle string "abcabcabcabc..." that can be obtained by concatenating "abc" to itself. Thus, the answer is 3.
"""
def cyclicString(s):
    mn = len(s)
    for pos in range(1,len(s)):
        go = True
        i = 0
        while (i+pos) < len(s) and go:
            if s[i] != s[pos+i]:
                go = False
            i += 1
        if go:
            return pos
    return mn
