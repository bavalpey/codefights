"""
You are watching a volleyball tournament, but you missed the beginning of the very first game of your favorite team. Now you're curious
about how the coach arranged the players on the field at the start of the game.

The team you favor plays in the following formation:

  0 3 0
  4 0 2
  0 6 0
  5 0 1
where positive numbers represent positions occupied by players. After the team gains the serve, its members rotate one position in a
clockwise direction, so the player in position 2 moves to position 1, the player in position 3 moves to position 2, and so on, with the
player in position 1 moving to position 6.

Example

  For
    formation = [["empty",   "Player5", "empty"],
                 ["Player4", "empty",   "Player2"],
                 ["empty",   "Player3", "empty"],
                 ["Player6", "empty",   "Player1"]]
  and k = 2, the output should be
    volleyballPositions(formation, k) = [
        ["empty",   "Player1", "empty"],
        ["Player2", "empty",   "Player3"],
        ["empty",   "Player4", "empty"],
        ["Player5", "empty",   "Player6"]
    ]    
  For
    formation = [["empty", "Alice", "empty"],
                 ["Bob",   "empty", "Charlie"],
                 ["empty", "Dave",  "empty"],
                 ["Eve",   "empty", "Frank"]]
  and k = 6, the output should be
    volleyballPositions(formation, k) = [
        ["empty", "Alice", "empty"],
        ["Bob",   "empty", "Charlie"],
        ["empty", "Dave",  "empty"],
        ["Eve",   "empty", "Frank"]
    ]
"""
def volleyballPositions(formation, k):
    lineup = []
    k %= 6
    if k == 0:
        return formation
    lineup.append(formation[0][1])
    lineup.append(formation[1][2])
    lineup.append(formation[3][2])
    lineup.append(formation[2][1])
    lineup.append(formation[3][0])
    lineup.append(formation[1][0])
    while k != 0:
        lineup = lineup[1:] + [lineup[0]]
        k-=1
    ans = []
    ans.append("empty")
    ans.append(lineup[0])
    ans.append("empty")
    ans.append(lineup[-1])
    ans.append("empty")
    ans.append(lineup[1])
    ans.append("empty")
    ans.append(lineup[3])
    ans.append("empty")
    ans.append(lineup[-2])
    ans.append("empty")
    ans.append(lineup[2])
    return [ans[x:x+3] for x in range(0, len(ans), 3)]
# Hard coding a solution to this problem is the easiest and most efficient way to solve it, thanks to python's O(1) indexing speed
