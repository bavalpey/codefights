"""
In the Land Of Chess, bishops don't really like each other. In fact, when two bishops happen to stand on the same diagonal, they
immediately rush towards the opposite ends of that same diagonal.

Given the initial positions (in chess notation) of two bishops, bishop1 and bishop2, calculate their future positions. Keep in mind that
bishops won't move unless they see each other along the same diagonal.

Example
  For bishop1 = "d7" and bishop2 = "f5", the output should be
    bishopDiagonal(bishop1, bishop2) = ["c8", "h3"].

  For bishop1 = "d8" and bishop2 = "b5", the output should be
    bishopDiagonal(bishop1, bishop2) = ["b5", "d8"].
  The bishops don't belong to the same diagonal, so they don't move.

"""
def bishopDiagonal(bishop1, bishop2):
  if bishop1[0] == bishop2[0] or bishop1[1] == bishop2[1]:
    return sorted([bishop1, bishop2])
  x = sorted([bishop1, bishop2])
  def onSameDiagonal(b1,b2):
    if abs(int(ord(b1[0])) - int(ord(b2[0]))) == abs(int(b1[1]) - int(b2[1])):
      return True
  if not onSameDiagonal(bishop1, bishop2):
    return x
  x1left = x[0][0] < x[1][0]
  x1down = x[0][1] < x[1][1]
  if x1down:
    vertDir = -1
  else:
    vertDir = 1
  if x1left:
    horDir = -1
  else:
    horDir = 1
  while x[0][0] not in "ah" and x[0][1] not in "18":
    x[0] = chr(ord(x[0][0])+vertDir) + str(int(x[0][1])+horDir)
  while x[1][0] not in "ah" and x[1][1] not in  "18":
    x[1] = chr(ord(x[1][0])-vertDir) + str(int(x[1][1])-horDir)
  return sorted(x)
