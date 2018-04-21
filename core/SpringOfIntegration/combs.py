"""
Miss X has only two combs in her possession, both of which are old and miss a tooth or two. She also has many purses of different length,
in which she carries the combs. The only way they fit is horizontally and without overlapping. Given teeth' positions on both combs, find
the minimum length of the purse she needs to take them with her.

It is guaranteed that there is at least one tooth at each end of the comb.
It is also guaranteed that the total length of two strings is smaller than 32.
Note, that the combs can not be rotated/reversed.

Example

For comb1 = "*..*" and comb2 = "*.*", the output should be
combs(comb1, comb2) = 5.
"""
def combs(comb1, comb2):
    b1 = b2 = "0b"
    mn = min([comb1,comb2])
    mx = max([comb1,comb2])
    for char in mx:
        if char == "*":
            b1 += "1"
        else:
            b1 += "0"
    for char in mn:
        if char == "*":
            b2 += "1"
        else:
            b2 += "0"
    b1 = int(b1,2)
    b2 = int(b2,2)
    b1_2,b2_2 = b1,b2
    c = 1
    while b1&b2:
        c+=1
        b1 <<= 1
    while b1_2&b2_2:
        b2_2 <<=1
    return min(len(bin(b1|b2)) -2,len(bin(b2_2|b1_2))-2)
