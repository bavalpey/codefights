"""
You are climbing a staircase that has n steps. You can take the steps either 1 or 2 at a time. Calculate how many distinct ways you can
climb to the top of the staircase.

Example
  For n = 1, the output should be
    climbingStairs(n) = 1;

  For n = 2, the output should be
    climbingStairs(n) = 2.
You can either climb 2 steps at once or climb 1 step two times.
"""
def climbingStairs(n):
  stepdict = {"1":1,"2":2} # Going to use dynamic programming to solve this problem.
  # So we're going to keep track of the calls in a dictionary to avoid calling the same function twice
  def findSteps(n): # this function will populate a dictionary of the answer for different numbers of steps.
    if str(n) in stepdict: 
      return stepdict[str(n)]
    else:
      stepdict[str(n)] = findSteps(n-2) + findSteps(n-1)
      return stepdict[str(n)]
  return findSteps(n)
