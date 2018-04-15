"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For
  picture = ["abc",
             "ded"]
  the output should be

  addBorder(picture) = ["*****",
                        "*abc*",
                        "*ded*",
                        "*****"]
"""
def addBorder(picture):
    ast = '*'*(len(picture[0])+2)
    r = [ast]
    for i in picture:
        t = "*" + i + "*"
        r.append(t)
    r.append(ast)
    return r
