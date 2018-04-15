"""
You are given an array of up to four non-negative integers, each less than 256.

Your task is to pack these integers into one number M in the following way:

The first element of the array occupies the first 8 bits of M;
The second element occupies next 8 bits, and so on.
Return the obtained integer M.

Note: the phrase "first bits of M" refers to the least significant bits of M - the right-most bits of an integer.
For further clarification see the following example.

Example

For a = [24, 85, 0], the output should be
arrayPacking(a) = 21784.

An array [24, 85, 0] looks like [00011000, 01010101, 00000000] in binary.
After packing these into one number we get 00000000 01010101 00011000 (spaces are placed for convenience),
which equals to 21784.
"""
def arrayPacking(a):
    M = "0b"
    for x in a[::-1]:
        p = bin(x)[2:]
        M += "0"*(8-len(p))
        # print(p)
        M += p
    # print(M)
    return int(M,2)
