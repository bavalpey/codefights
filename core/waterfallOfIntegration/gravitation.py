"""
You are given a vertical box divided into equal columns. Someone dropped several stones from its top through the columns. Stones are
falling straight down at a constant speed (equal for all stones) while possible (i.e. while they haven't reached the ground or they are
not blocked by another motionless stone). Given the state of the box at some moment in time, find out which columns become motionless
first.

Example

For
  rows = ["#..##",
          ".##.#",
          ".#.##",
          "....."]
the output should be gravitation(rows) = [1, 4].
"""

def gravitation(rows):
  col_score = [0]*(len(rows[0]))
  mn = float("INF")
  mnIdx = []
  for j,item in enumerate(zip(*rows)):
    seenHash = False
    cntr = 0
    for i,sym in enumerate(item):
      if seenHash:
        if sym == '#':
          col_score[j] += cntr
          cntr = 0
        else:
          cntr += 1
      else:
        if sym == '#':
          seenHash = True
    if cntr:
      col_score[j] += cntr
    if col_score[j] < mn:
      mnIdx=[j]
      mn = col_score[j]
    elif col_score[j] == mn:
      mnIdx.append(j)
  
  return mnIdx
        
