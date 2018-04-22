"""
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

  For name = &quot;var_1__Int&quot;, the output should be
    variableName(name) = true;
  For name = &quot;qq-q&quot;, the output should be
    variableName(name) = false;
  For name = &quot;2w2&quot;, the output should be
    variableName(name) = false.
"""
import re
def variableName(name):
    p = re.compile('[a-zA-Z\_][\w\_]*\Z')
    if p.match(name):
        return True
    else:
        return False
