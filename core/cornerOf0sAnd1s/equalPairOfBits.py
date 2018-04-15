"""
You're given two integers, n and m. Find position of the rightmost pair of equal bits in their binary representations
(it is guaranteed that such a pair exists), counting from right to left.

Return the value of 2^position_of_the_found_pair (0-based).

Example

For n = 10 and m = 11, the output should be
equalPairOfBits(n, m) = 2.

10_10 = 1010_2, 11_10 = 1011_2, the position of the rightmost pair of equal bits is the bit at position 1 (0-based)
from the right in the binary representations.
So the answer is 2^1 = 2.
"""
def equalPairOfBits(n, m):
    return n + m + 1 & ~m - n ;
