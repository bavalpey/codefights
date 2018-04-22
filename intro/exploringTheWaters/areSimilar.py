"""
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

  For a = [1, 2, 3] and b = [1, 2, 3], the output should be
    areSimilar(a, b) = true.

  The arrays are equal, no need to swap any elements.

  For a = [1, 2, 3] and b = [2, 1, 3], the output should be
    areSimilar(a, b) = true.

  We can obtain b from a by swapping 2 and 1 in b.

  For a = [1, 2, 2] and b = [2, 1, 1], the output should be
    areSimilar(a, b) = false.

  Any swap of any two elements either in a or in b won't make a and b equal.
"""
def areSimilar(a, b):
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            c += 1
            if c > 2:
                return False
            
            if c == 1:
                a1 = a[i]
                b1 = b[i]
            elif c == 2:
                a2 = a[i]
                b2 = b[i]
                
                if(not(a1 == b2 and a2 == b1)):
                    return False
            
    return (c in [2, 0])
