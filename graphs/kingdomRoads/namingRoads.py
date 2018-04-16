"""
Once upon a time, in a kingdom far, far away, there lived a king Byteasar V. His predecessor, king Byteasar IV, lived quite a long life,
and when Byteasar V finally ascended the throne, he was already 150 years old. The new king had been preparing all his life for his
moment of glory and, scared that he wouldn't have enough time to shine, started his reforms right away. The first (and, as it turned
out, the last) royal decree, issued within a couple of days after the coronation, ordered the following: all the road in the kingdom
were to be named.

Unfortunately the king didn't have enough time to come up with actual names, so all the roads were to be names with numbers from 0 to
roads.length - 1. As a born strategist, Byteasar wanted to make sure that the maps of his kingdom were confusing to enemies, which is
why the road names were to be chosen so that no two roads with the neighboring names (i.e. names i and i + 1 for some i) would have a
common end at one of the cities.

The archicartographer came up with the names for the roads, but he was not sure if the constraint the king imposed was met. He asked
the Greater Power to help him check it. As a Greater Power from the future, you are the one who can help with that. Given the names
for the roads the archicartographer came up with, check that no two roads with the neighboring names have a common end.

Example

  For
    roads = [[0, 1, 0],
             [4, 1, 2],
             [4, 3, 4],
             [2, 3, 1],
             [2, 0, 3]]
  the output should be
    namingRoads(roads) = true.

  For
    roads = [[2, 3, 1],
             [3, 0, 0],
             [2, 0, 2]]
  the output should be
    namingRoads(roads) = false.
"""
def namingRoads(roads):
    # mx = 0
    # for x in roads:
    #     if x[0] > mx:
    #         mx = x[0]
    #     if x[1] > mx:
    #         mx = x[1]

    roads.sort(key = lambda x: x[2])
    roadNames = [['abc'] for i in range(35000)]
    for x in roads:
        # if x[2]-1 in roadNames[x[0]] or x[2]+1 in roadNames[x[0]] or x[2]-1 in roadNames[x[1]] or x[2]+1 in roadNames[x[1]]:
        #     return False
        if x[2] - 1 == roadNames[x[0]][-1] or x[2] - 1 == roadNames[x[1]][-1]:
            return False
        roadNames[x[0]].append(x[2])
        roadNames[x[1]].append(x[2])
    
    return True
