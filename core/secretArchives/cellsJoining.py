"""
You are writing a spreadsheet application for an ancient operating system. The system runs on a computer so old that it can
only display ASCII graphics. Currently you are stuck with implementing the cells joining algorithm.

You are given a table in ASCII graphics, where the following characters are used for borders: +, -, |. The rows can have 
different heights and the columns can have different widths. Each cell has an area greater than 1 (excluding the borders) and
can contain any ASCII characters excluding +, - and |.

The algorithm you want to implement should merge the cells within a given rectangular part of the table into a single cell by 
removing the borders between them (i.e. replace them with space characters (' ') and replace redundant +s with correct border 
symbols). The cells to join are represented by the coordinates of the cells at the extreme bottom-left and top-right of the 
area.

Example
For

table = ["+----+--+-----+----+",
         "|abcd|56|!@#$%|qwer|",
         "|1234|78|^&=()|tyui|",
         "+----+--+-----+----+",
         "|zxcv|90|77777|stop|",
         "+----+--+-----+----+",
         "|asdf|~~|ghjkl|100$|",
         "+----+--+-----+----+"]
and coords = [[2, 0], [1, 1]], the output should be

cellsJoining(table, coords) = ["+----+--+-----+----+",
                               "|abcd|56|!@#$%|qwer|",
                               "|1234|78|^&=()|tyui|",
                               "+----+--+-----+----+",
                               "|zxcv 90|77777|stop|",
                               "|       +-----+----+",
                               "|asdf ~~|ghjkl|100$|",
                               "+-------+-----+----+"]

"""

def cellsJoining(table, coords):
  colsToCheck = set()
  row = -1
  for i, r in enumerate(table):
    mod = False
    if r[0] == '+':
      row += 1
    else:
      mod = coords[1][0] <= row <= coords[0][0]
    if coords[1][0] < row <= coords[0][0] or mod:
      # Replace unneeded +'s with |'s
      if coords[0][1] == 0 and r[0] == '+':
        table[i] = "|" + table[i][1:]
      col = 0
      for pos, char in enumerate(r[1:], 1):
        colStart = False
        if char == '|' or char == '+':
          col += 1
          # Remove redundant +'s from column edge
          if (col-1) == coords[1][1] and pos+1 == len(r):
            table[i] = table[i][:-1] + '|'
          if col == coords[0][1]:
            colStart = True
        if coords[0][1] <= col <= coords[1][1]:
          if char in ['+','-','|'] and not colStart:
            table[i] = table[i][:pos] + ' ' + table[i][pos+1:]
          if char == '|':
            colsToCheck.add(pos)
  
  for pos, char in enumerate(table[0][1:-1],1):
    if char == '+' and pos in colsToCheck:
      if table[1][pos] != '|':
        table[0] = table[0][:pos] + '-' + table[i][pos+1:]
  
  for pos, char in enumerate(table[-1][1:-1], 1):
    if char == '+' and pos in colsToCheck:
      if table[-2][pos] != '|':
        table[-1] = table[-1][:pos] + '-' + table[-1][pos+1:]
  return table
