"""
You are given a string s of characters that contains at least n numbers (here, a number is defined as a consecutive series of digits,
where any character immediately to the left and right of the series are not digits). The numbers may contain leading zeros, but it is
guaranteed that each number has at least one non-zero digit in it.

Your task is to find the n^th number and return it as a string without leading zeros.

Example
For s = "8one 003number 201numbers li-000233le number444" and n = 4,
the output should be
  nthNumber(s, n) = "233".
"""
def nthNumber(s, n):
    pattern = r"(?:\D*\d+\D+){" + str(n-1) + r"}\D*0*(\d+)"
    return re.match(pattern, s).group(1)
