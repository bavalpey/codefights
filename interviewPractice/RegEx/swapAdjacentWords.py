"""
You are given a string consisting of words separated by whitespace characters, where the words consist only of English letters. Your
task is to swap pairs of consecutive words and return the result.

Example
  For s = "CodeFight On", the output should be
    swapAdjacentWords(s) = "On CodeFight";
  For s = "How are you today guys", the output should be
    swapAdjacentWords(s) = "are How today you guys".
"""

def swapAdjacentWords(s):
    return re.sub(r"([A-Za-z]+)\s([A-Za-z]+)", lambda x: x.group(2)+" " + x.group(1), s)
