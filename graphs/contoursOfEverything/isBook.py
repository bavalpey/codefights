"""
You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main
recognition system is already implemented, and now you need to start the teaching process.

Today you want to teach your program to recognize book patterns, which means that you need to implement a function that, given the
adjacency matrix representing the contour, will determine whether it's a book or not.

A book consists of a base and may have any number of pages.
The book's base consists of a single edge connecting two nodes, and it is a common edge for all the pages. Besides that, every page
has only one node connected to both sides of the base.

Given the object's contour as an undirected graph represented by its adjacency matrix adj determine whether it's a book or not.

Example
For
  adj = [[false, true, true, true],
         [true, false, true, true],
         [true, true, false, false],
         [true, true, false, false]]
the output should be
  isBook(adj) = true.
"""

def isBook(adj):
  # need to find 2 nodes of maximal degree
  # Every other node needs to have degree 2
  if len(adj) == 3:
    for node in adj:
      if sum(node) != 2:
        break
    else:
      return True
  degree = lambda x: sum(x)
  binding = {}
  pageDict = {}
  for node,pos in enumerate(adj):
    if pos[node]:
      return False
    d = degree(pos) - pos[node]
    if d == 2:
      pageDict[node] = d
    elif d == len(adj) - 1:
      binding[node] = d
    else:
      return False
  return len(binding) == 2
