"""
A rectangle with sides equal to even integers a and b is drawn on the Cartesian plane. Its center (the intersection point of
its diagonals) coincides with the point (0, 0), but the sides of the rectangle are not parallel to the axes; instead, they are forming
45 degree angles with the axes.

How many points with integer coordinates are located inside the given rectangle (including on its sides)?

Example

For a = 6 and b = 4, the output should be
  rectangleRotation(a, b) = 23.
"""
import math
def rectangleRotation(a, b):
    r = 0
    for x in range(-(a+100),a+111):
        for y in range(-(b+100),b+111):
            x1 = (x + y) / math.sqrt(2)
            y1 = (y - x) / math.sqrt(2)
            
            if x1 < a/2.0 and x1 > -a/2.0 and y1 < b/2.0 and y1 > -b/2.0:
                r += 1
    return r
