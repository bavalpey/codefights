"""
Given an array strings, determine whether it follows the sequence given in the patterns array. In other words, there should be no i and
j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].

Example

For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], the output should be
  areFollowingPatterns(strings, patterns) = true;
For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the output should be
  areFollowingPatterns(strings, patterns) = false.
"""

def areFollowingPatterns(strings, patterns):
  return len(set(strings)) == len(set(patterns)) == len(set(zip(strings,patterns)))
  # the above code checks to ensure that the number of different patterns is the exact same as the number of different words.
  #  However, this is not enough, as simply having len(set(strings)) == len(set(patterns)) would return true in the case of
  #  strings = ["cat","dog","dog"] and patterns = ["a","a","b"]. (in other words, in cases where a pattern is mapped to more than one
  word).
  #  Thus, we check if the total number of unique pairs of strings and patterns is the same as the numbers of unique patterns.
