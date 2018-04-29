"""
You are implementing a command-line version of the Paint app. Since the command line doesn't support colors, you are using different
characters to represent pixels. Your current goal is to support rectangle x1 y1 x2 y2 operation, which draws a rectangle that has an
upper left corner at (x1, y1) and a lower right corner at (x2, y2). Here the x-axis points from left to right, and the y-axis points
from top to bottom.

Given the initial canvas state and the array that represents the coordinates of the two corners, return the canvas state after the
operation is applied. For the details about how rectangles are painted, see the example.

Example

For

  canvas = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]
and rectangle = [1, 1, 4, 3], the output should be

  drawRectangle(canvas, rectangle) = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
                                      ['a', '*', '-', '-', '*', 'a', 'a', 'a'],
                                      ['a', '|', 'a', 'a', '|', 'a', 'a', 'a'],
                                      ['b', '*', '-', '-', '*', 'b', 'b', 'b'],
                                      ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]
"""
import itertools as it
def drawRectangle(canvas, rectangle):
    r = list(it.compress(rectangle,[0,1,0,1]))
    c = list(it.compress(rectangle,[1,0,1,0]))
    for row in range(r[0],r[1]+1):
        for col in range(c[0],c[1]+1):
            if row in r:
                if col in c:
                    canvas[row][col] = "*"
                else:
                    canvas[row][col] = "-"
            elif col in c:
                canvas[row][col] = "|"
    return canvas
