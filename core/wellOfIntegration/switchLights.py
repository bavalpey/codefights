"""
N candles are placed in a row, some of them are initially lit. For each candle from the 1st to the Nth the following algorithm is applied: if the observed candle is lit then states of this candle and all candles before it are changed to the opposite. Which candles will remain lit after applying the algorithm to all candles in the order they are placed in the line?

Example

  For a = [1, 1, 1, 1, 1], the output should be
    switchLights(a) = [0, 1, 0, 1, 0].
    
  For a = [0, 0], the output should be
    switchLights(a) = [0, 0].

  The candles are not initially lit, so their states are not altered by the algorithm.
"""
def switchLights(a):
    for pos,candle in enumerate(a):
        if candle == 1:
            a[pos] = 0
            for pos2,candle2 in enumerate(a[:pos]):
                if candle2 == 1:
                    a[pos2] = 0
                else:
                    a[pos2] = 1
    return a
