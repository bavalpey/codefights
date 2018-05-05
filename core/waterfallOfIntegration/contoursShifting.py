"""
Mark got a rectangular array matrix for his birthday, and now he's thinking about all the fun things he can do with it. He likes
shifting a lot, so he decides to shift all of its i-contours in a clockwise direction if i is even, and counterclockwise if i is odd.

Here is how Mark defines i-contours:
  the 0-contour of a rectangular array as the union of left and right columns as well as top and bottom rows;
  consider the initial matrix without the 0-contour: its 0-contour is the 1-contour of the initial matrix;
  define 2-contour, 3-contour, etc. in the same manner by removing 0-contours from the obtained arrays.
  
Implement a function that does exactly what Mark wants to do to his matrix.

Example

  For
    matrix = [[ 1,  2,  3,  4],
               [ 5,  6,  7,  8],
               [ 9, 10, 11, 12],
               [13, 14, 15, 16],
               [17, 18, 19, 20]]
  the output should be
    contoursShifting(matrix) = [[ 5,  1,  2,  3],
                                 [ 9,  7, 11,  4],
                                 [13,  6, 15,  8],
                                 [17, 10, 14, 12],
                                 [18, 19, 20, 16]]
  For matrix = [[238, 239, 240, 241, 242, 243, 244, 245]],
  the output should be
    contoursShifting(matrix) = [[245, 238, 239, 240, 241, 242, 243, 244]].
  Note, that if a contour is represented by a 1 × n array, its center is considered to be below it.

  For
    matrix = [[238],
               [239],
               [240],
               [241],
               [242],
               [243],
               [244],
               [245]]
  the output should be
    contoursShifting(matrix) = [[245],
                                 [238],
                                 [239],
                                 [240],
                                 [241],
                                 [242],
                                 [243],
                                 [244]]
  If a contour is represented by an n × 1 array, its center is considered to be to the left of it.
"""
from copy import deepcopy
def cycleBorder(m,step):
    c = deepcopy(m) # makes a copy of of m that does not change when m changes
    if step%2 == 0:
        direction = 1
    elif step%2 == 1:
        direction = -1
    try:
        if step == len(m) - step-1 and len(m[step][step:-step]) != 0:
            if direction == 1:
                for col,elem in enumerate(m[step][step:len(m[step])],step):
                    if col == step:
                        m[step][col] = m[step][len(m[step])-step-1]
                    else:
                        m[step][col] = c[step][col-1]
            else:
                for col,elem in enumerate(m[step][step:-step],step):
                    if col == len(m[step][step:-step]):
                        m[step][col] = c[step][step]
                    else:
                        m[step][col] = c[step][col+1]
            return m
    except TypeError:
        pass
    if len(m[step:len(m)-step]) == 1:
        if len(m[step:len(m)-step][step:len(m[step])-step]) == 1:
            return m
        if direction == 1:
            for col, elem in enumerate(m[step][step:len(m[step])-step],step):
                if col == step:
                    m[step][col] = c[step][len(c[step])-step]
                else:
                    m[step][col] = c[step][col-1]
        else:
            for col, elem in enumerate(m[step][step:len(m[step])-step],step):
                if col == len(m[step])-step:
                    m[step][col] = c[step][step]
                else:
                    m[step][col] = c[step][col+1]
    if direction == 1:
        for pos,row in enumerate(m[step:len(m)-step],step):
            if len(m[pos][step:len(m[pos])-step]) == 1:
                    if pos == step:
                        m[pos][step] = c[step][len(c[step])-step]
                    else:
                        m[pos][step] = c[pos-1][step]
            else:
                for col,elem in enumerate(m[pos][step:len(m[pos])-step],step):
                    if col in [step,len(m[pos])-step-1] or pos in [step,len(m)-step-1]:
                        if pos == step and col == step: # upper left corner
                            m[pos][col] = c[pos+1][col]
                        elif pos==step: # top border
                            m[pos][col] = c[pos][col-1]
                        elif col==step and pos!=len(m)-step-1: # left border
                            m[pos][col] = c[pos+1][col]
                        elif col == step and pos == len(m)-step-1: # lower left corner
                            m[pos][col] = c[pos][col+1]
                        elif pos == len(m)-step-1 and col != len(m[0])-step-1: # lower border
                            m[pos][col] = c[pos][col+1]
                        elif pos==len(m)-step-1 and col==len(m[0])-step-1: # lower right corner
                            m[pos][col] = c[pos-1][col]
                        else:
                            m[pos][col] = c[pos-1][col]
    elif direction == -1:
        for pos,row in enumerate(m[step:len(m)-step],step):
            if len(m[pos][step:len(m[pos])-step]) == 1:
                    if pos == len(m)-step-1:
                        m[pos][step] = c[step][step]
                    else:
                        m[pos][step] = c[pos+1][step]
            else:
                for col,elem in enumerate(m[pos][step:len(m[pos])-step],step):
                    if col in [step,len(m[pos])-step-1] or pos in [step,len(m)-step-1]:
                        if pos == step and col != len(m[0])-step-1: # top border
                            m[pos][col] = c[pos][col+1]
                        elif pos == step and col == len(m[0])-step-1: # upper right corner
                            m[pos][col] = c[pos+1][col]
                        elif col == step: # left border
                            m[pos][col] = c[pos-1][col]
                        elif pos == len(m)-step-1 and col!= len(m[0])-step-1: # bottom border
                            m[pos][col] = c[pos][col-1]
                        elif pos == len(m)-step-1 and col ==len(m[0])-step-1:
                            m[pos][col] = c[pos][col-1]
                        elif col == len(m[0])-step-1 and pos != step: # right border
                            m[pos][col] = c[pos+1][col]              
    return m

def contoursShifting(matrix):
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix
    if len(matrix[0]) == 1:
        return [matrix[-1]] + matrix[:-1]
    elif len(matrix) == 1:
        return [[matrix[0][-1]] + matrix[0][:-1]]
    cnt = len(matrix)
    strt = 0
    while strt != len(matrix):
        matrix = cycleBorder(matrix,strt)
        strt += 1
    return matrix
