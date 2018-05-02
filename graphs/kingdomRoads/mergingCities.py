"""
Once upon a time, in a kingdom far, far away, there lived a king Byteasar VIII. The king came down in history as a great warrior,
since he managed to defeat the enemy that has been capturing the cities of the kingdom over more than a century. When the war was
most of the cities were almost completely destroyed, and there was no way to raise them from the debris. Byteasar decided to start
cities renovation by merging them.

The king decided to merge each pair of cities cityi, cityi+1 for i = 0, 2, 4, ... if they were connected by one of the two-way roads
running through the kingdom.

Initially, all information about the roads were stored in the roadRegister. Your task is to return the roadRegister after the merging
was performed, assuming that after merging the cities reindexation is done in such way that city formed out of cities a and b (where
a < b) receives index a, and all the cities with numbers i (where i > b) get numbers i - 1.

Example

For

  roadRegister = [
    [false, true,  true,  false, false, false, true ],
    [true,  false, true,  false, true,  false, false],
    [true,  true,  false, true,  false, false, true ],
    [false, false, true,  false, false, true,  true ],
    [false, true,  false, false, false, false, false],
    [false, false, false, true,  false, false, false],
    [true,  false, true,  true,  false, false, false]
  ]
the output should be

  mergingCities(roadRegister) = [
    [false, true,  true,  false, true ],
    [true,  false, false, true,  true ],
    [true,  false, false, false, false],
    [false, true,  false, false, false],
    [true,  true,  false, false, false]
  ]
"""
import itertools as it
def mergingCities(r):
    filt = [] # This will be a list which will keep track of rodes that will be deleted
    for i in range(0,len(r)): # iterate through all of the roads
        if not i%2: # However, only do something if the index is even
            filt.append(1) # if it is even, we do not have a chance of removing it, so keep it
            if i != len(r)-1: # the next steps will deal with the city and index i+1
                if r[i][i+1]: # if there is a road, then merge
                    filt.append(0) # merging means that the city will not be kept
                    r[i] = list(bool((r[i][j] or r[i+1][j]) and j!=i) for j in range(len(r[i])))
                    # the above code will generate the new list of connections
                    # there will be a connection to the city if either city i or city i + 1 has a connection
                    for j in range(len(r)): # now have all other roads that connected to city i+1
                        if j != i: # connect to city i
                            r[j][i] = r[j][i] or r[j][i+1]
                else: # if there is not a road, do not merge, and leave city as is
                    filt.append(1)
    ans = list(it.compress(r,filt))
    for i in range(len(ans)):
        ans[i] = list(it.compress(ans[i],filt)) # now we are only printing out the road map for the
    return ans                                  # cities which were not deleted, using itertools' compress
        
