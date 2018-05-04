"""
You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main
recognition system is already implemented, and now you need to start the teaching process.

Today you want to teach your program to recognize butterfly patterns, which means that you need to implement a function that, given the
adjacency matrix representing the contour, will determine whether it's a butterfly or not.

Example

For
  adj = [[false, true, true, false, false],
         [true, false, true, false, false],
         [true, true, false, true, true],
         [false, false, true, false, true],
         [false, false, true, true, false]]
  the output should be
isButterfly(adj) = true.

"""
def isButterfly(adj):
    ans = []
    for pos,i in enumerate(adj):
        ans.append(sum(i))
        if adj[pos][pos] == True:
            return False
    seen4 = False
    for i in ans:
        if i == 4:
            if seen4:
                return False
            else:
                seen4 = True
            
        elif i != 2:
            return False
    return seen4
