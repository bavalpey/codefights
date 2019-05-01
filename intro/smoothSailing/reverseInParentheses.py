"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

  For inputString = "(bar)", the output should be
    reverseInParentheses(inputString) = "rab";
  For inputString = "foo(bar)baz", the output should be
    reverseInParentheses(inputString) = "foorabbaz";
  For inputString = "foo(bar)baz(blim)", the output should be
    reverseInParentheses(inputString) = "foorabbazmilb";
  For inputString = "foo(bar(baz))blim", the output should be
    reverseInParentheses(inputString) = "foobazrabblim".
  Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
"""

def revWord(word):
  return word[1:-1][::-1]

def reverseInParentheses(word):
  p = re.compile(r"(\([^()]*\))")
  while re.search(p,word):
    repl = re.findall(p,word)
    for i in repl:
      word = word.replace(i,revWord(i))
    
    
  return word
