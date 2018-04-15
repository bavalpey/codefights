"""
Check whether the given string is a subsequence of the plaintext alphabet.

Example

For s = "effg" or s = "cdce", the output should be
alphabetSubsequence(s) = false;
For s = "ace" or s = "bxz", the output should be
alphabetSubsequence(s) = true.
"""
def alphabetSubsequence(s):
    this = sorted(s)
    this2 = list(s)
    if this == this2 and len(set(s)) == len(s):
        return True
    return False
