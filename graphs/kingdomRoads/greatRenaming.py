"""
Once upon a time, in a kingdom far, far away, there lived a king Byteasar VI. As any king with such a magnificent name, he was destined
to leave a trace in history. Unfortunately imagination wasn't one of king Byteasar's strong suits, so the reform he came up with was quite
simple: the king ordered to rename all the cities. He didn't want to come up with new names (as a king, he'd have to remember
them all!), so he ordered the cities to swap their names in such manner that the ith city would have the name of the city number
(i + 1)th. The last city in the Byteasar's kingdom would, naturally, get the name of the very first city.

The cartographers were not happy with this reform, since they had to redraw all the maps of the kingdom. Before the reform,
information about all the roads between the cities were stored in the roadRegister. Prior to drawing maps, they had to start
with updating the register. Your task is to find out what the updated register looked like.

Example

For
  roadRegister = [[false, true,  true,  false],
                  [true,  false, true,  false],
                  [true,  true,  false, true ],
                  [false, false, true,  false]]
the output should be

  greatRenaming(roadRegister) = [[false, false, false, true ],
                                 [false, false, true,  true ],
                                 [false, true,  false, true ],
                                 [true,  true,  true,  false]]
"""
def shift(lst):
    return [lst[-1]] + lst[:len(lst)-1]
def greatRenaming(roadRegister):
    for i,x in enumerate(roadRegister):
        roadRegister[i] = shift(x)
    return shift(roadRegister)
