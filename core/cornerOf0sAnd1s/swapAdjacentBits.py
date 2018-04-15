"""
You're given an arbitrary 32-bit integer n. Take its binary representation, split bits into it in pairs
(bit number 0 and 1, bit number 2 and 3, etc.) and swap bits in each pair. Then return the result as a decimal number.

Example

For n = 13, the output should be
swapAdjacentBits(n) = 14.

1310 = 11012 ~> {11}{01}2 ~> 11102 = 1410.

For n = 74, the output should be
swapAdjacentBits(n) = 133.

7410 = 010010102 ~> {01}{00}{10}{10}2 ~> 100001012 = 13310.
Note the preceding zero written in front of the initial number: since both numbers are 32-bit integers, they have
32 bits in their binary representation. The preceding zeros in other cases don't matter, so they are omitted.
Here, however, it does make a difference.
"""
# NOTE, THIS CODE IS SPECIFIC TO THE PROBLEM UNDER THE GIVEN INPUT CONSTRAINTS: 
# Guaranteed constraints:
# 0 ≤ n < 2^30.

def swapAdjacentBits(n):
    return ((n & 0b1010101010101010101010101010101010) >> 1) | ((n & 0b0101010101010101010101010101010101) << 1)
