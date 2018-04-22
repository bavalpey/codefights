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
    length = len(picture[0])
    for i,c in enumerate(picture):
        picture[i] = "*" + c + "*"
    picture.append("*"*(length+2))
    picture.insert(0, "*"*(length+2))
    return picture
