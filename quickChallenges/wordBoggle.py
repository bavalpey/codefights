"""
Boggle is a popular word game in which players attempt to find words in sequences of adjacent letters on a rectangular board.

Given a two-dimensional array board that represents the character cells of the Boggle board and an array of unique strings words,
find all the possible words from words that can be formed on the board.

Note that in Boggle when you're finding a word, you can move from a cell to any of its 8 neighbors, but you can't use the same cell
twice in one word.

Example
For
board = [
    ['R', 'L', 'D'],
    ['U', 'O', 'E'],
    ['C', 'S', 'O']
]
and words = ["CODE", "SOLO", "RULES", "COOL"], the output should be
  wordBoggle(board, words) = ["CODE", "RULES"].
"""
def wordBoggle(board,words):
    def returnDictWithSubStrings(word):
      d = {}
      for i in range(1,len(word)):
          d[word[:i]] = 1
      return d
  
    visited = {0: {0: False, 1: False, 2: False, 3: False}, 1: {0: False, 1: False, 2: False, 3: False}, 2: \
    {0: False, 1: False, 2: False, 3: False}, 3: {0: False, 1: False, 2: False, 3: False}}

    if len(words) == 0:
        return []
    wordDict = {}
    mx = 0
    for i in words:
        l = len(i)
        if l > mx:
            mx = l
        wordDict[i] = "0"
    def isWord(word):
        try:
            wordDict[word]
        except KeyError:
            return False
        return True
    if len(board) == 0:
        return []
    elif len(board[0]) == 0:
          return []
    ans = []
    ssDict = {}
    for word in words:
        ssDict.update(returnDictWithSubStrings(word))
        
    def findWords(i,j,string):
        string += board[i][j]
        if len(string) > mx:
            return
        if isWord(string):
            ans.append(string)
        try:
            ssDict[string]
        except KeyError:
            return
        visited[i][j] = True
        for row in range(max(i-1,0),min(i+2,len(board))):
            for col in range(max(j-1,0),min(j+2,len(board[0]))):
                if not visited[row][col]:
                    findWords(row,col,string)
        visited[i][j] = False
    for i in range(len(board)):
        for j in range(len(board[0])):
            findWords(i,j,"")
    return sorted(set(ans))
