"""
You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main
recognition system is already implemented, and now you need to start the teaching process.

Today you want to teach your program to recognize wheel patterns, which means that you need to implement a function that, given the
adjacency matrix representing the contour, will determine whether it's a wheel or not.

The wheel contour can be thought of as a single center vertex and a regular polygon with n (n > 2) vertices which are all connected to
the center.


Given the object's contour as an undirected graph represented by its adjacency matrix adj determine whether it's a wheel or not.

Example
For
  adj = [[false, true, true, true, true],
         [true, false, true, false, true],
         [true, true, false, true, false],
         [true, false, true, false, true],
         [true, true, false, true, false]]
the output should be
  isWheel(adj) = true.

"""

def isWheel(adj):
  degree = lambda x: sum(x)
  roots = {}
  spokeDict = {}
  for node,pos in enumerate(adj):
    d = degree(pos) - pos[node]
    if degree(pos) > 3: # if the degree of this node is >1, then it is a potential root
      roots[node] = d
    elif degree(pos) == 3:
      spokeDict[node] = d
    else:
      return False
  if len(spokeDict) == 0 or len(roots) > 1: # if there are no leaves, there are no stars
    return False
  if len(adj) == 4 and len(roots) == 0 and len(spokeDict) == 4:
    return True
  elif len(roots) == 0:
    return False
  def isWheel(root):
    for pos,edge in enumerate(adj[root]):
      if edge:
        pDegree = spokeDict.pop(pos,None) # Remove a leaf it is connected to the root, this will help identify stars of size 2
        if pDegree != 3: # if the degree of any of the children is >1, then it cannot be a leaf, so the whole tree is 
          return False       # not a star.
    else:
      return True
  for node in roots:
    return (isWheel(node) and len(spokeDict) == 0)
