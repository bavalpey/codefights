"""
You are implementing your own HTML editor. To make it more comfortable for developers you would like to add an auto-completion feature
to it.

Given the starting HTML tag, find the appropriate end tag which your editor should propose.

Example

  For startTag = "<button type='button' disabled>", the output should be
    htmlEndTagByStartTag(startTag) = "</button>";
  For startTag = "<i>", the output should be
    htmlEndTagByStartTag(startTag) = "</i>".
"""
import re
def htmlEndTagByStartTag(startTag):
    p = re.compile("\<[^ \t\n\r\f\v>]+")
    return "</" + p.match(startTag).group()[1:] + ">"
