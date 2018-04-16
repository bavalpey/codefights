"""
Once upon a time, in a kingdom far, far away, there lived a king Byteasar III. As a smart and educated ruler, he did everything in his
(unlimited) power to make every single system of his kingdom efficient. The king went down in history as a great road builder: during
his reign a great number of roads were built, and the road system he created was the most efficient for those dark times.

When you started to learn about Byteasar's III deeds in your history classes, the creeping doubt crawled into the back of your mind:
what if the famous king wasn't so great after all? According to the most recent studies, there were n cities in the Byteasar's kingdom,
which were connected by the two-ways roads. You managed to get information about this roads from the university library, so now you can
write a function that will determine whether the road system in Byteasar's kingdom was efficient or not.

A road system is considered efficient if it is possible to travel from any city to any other city by traversing at most 2 roads.

Example

  For n = 6 and
    roads = [[3, 0], [0, 4], [5, 0], [2, 1],
              [1, 4], [2, 3], [5, 2]]
  the output should be
    efficientRoadNetwork(n, roads) = true.

  For n = 6 and
    roads = [[0, 4], [5, 0], [2, 1],
              [1, 4], [2, 3], [5, 2]]
  the output should be
    efficientRoadNetwork(n, roads) = false.
"""
def checkSubPath(rm, curr, dest):
    for col,x in enumerate(rm[curr]):
        if x == 1:
            if rm[col][dest] == 1:
                return True
    return False
def efficientRoadNetwork(n, roads):
    inf = float('inf')
    if len(roads) < n-1:
        return False
    roadmap = []
    for x in range(n):
        thisRow = []
        for y in range(n):
            if x == y:
                thisRow.append(0)
            else:
                thisRow.append(inf)
        roadmap.append(thisRow)
    for x in roads:
        roadmap[x[0]][x[1]] = 1
        roadmap[x[1]][x[0]] = 1
    for row,x in enumerate(roadmap):
        for col,y in enumerate(x):
            if roadmap[row][col] == inf:
                if not checkSubPath(roadmap, row, col):
                    return False
    return True
