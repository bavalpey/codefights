"""
Some people run along a straight line in the same direction. They start simultaneously at pairwise distinct positions and run with
constant speed (which may differ from person to person).

If two or more people are at the same point at some moment we call that a meeting. The number of people gathered at the same point is
called meeting cardinality.

For the given starting positions and speeds of runners find the maximum meeting cardinality assuming that people run infinitely long. If
there will be no meetings, return -1 instead.

Example

For startPosition = [1, 4, 2] and speed = [27, 18, 24], the output should be
  runnersMeetings(startPosition, speed) = 3.
"""
def runnersMeetings(startPosition, speed):
    ans = 1
    for i in range(len(startPosition)):
        for j in range(i+1,len(startPosition)):
            spd = speed[i]-speed[j]
            dist = startPosition[j]-startPosition[i]
            num = 0
            if(spd == 0 and dist != 0):
                continue
            for k in range(len(startPosition)):
                if startPosition[k]*spd + speed[k] * dist == startPosition[i]*spd+speed[i]*dist:
                    num += 1
            if num == 0:
                continue
            if num > ans:
                ans = num
    if ans > 1:
        return ans
    return -1
