"""
You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main
recognition system is already implemented, and now you need to start the teaching process.

Today you want to teach your program to recognize star patterns in the image of the night sky, which means that you need to implement
a function that, given the adjacency matrix representing a number of contours in the sky, will find the number of stars in it.

The graph representing some contour is cosidered to be a star if it is a tree of size 2 or if it is a tree of size k > 2 with one
internal node (which is a tree root at the same time) and k - 1 leaves.

Example
For
  adj = [[false, true, false, false, false],
         [true, false, false, false, false],
         [false, false, false, true, false],
         [false, false, true, false, false],
         [false, false, false, false, false]]
the output should be
  countStars(adj) = 2.
"""

def countStars(adj):
  degree = lambda x: sum(x)
  roots = {}
  leafDict = {}
  mx = -1 # I also want to keep track of the maximum degree
  for node,pos in enumerate(adj):
    d = degree(pos)
    if d > mx:
      mx = d
    if degree(pos) > 1: # if the degree of this node is >1, then it is a potential root
      roots[node] = d
    elif degree(pos) == 1:
      leafDict[node] = d
  if len(leafDict) == 0: # if there are no leaves, there are no stars
    return 0
  elif len(roots) == 0: # If all nodes have degree <= 1, then the only stars are those of size 2, so return those
    return len(leafDict) // 2
  def isStar(root):
    for pos,edge in enumerate(adj[root]):
      if edge:
        pDegree = leafDict.pop(pos,None) # Remove a leaf it is connected to the root, this will help identify stars of size 2
        if pDegree != 1: # if the degree of any of the children is >1, then it cannot be a leaf, so the whole tree is 
          return 0       # not a star.
    else:
      return 1
  stars = 0
  for node in roots:
    stars += isStar(node)
      
  return stars + len(leafDict) //2
