# The solution below is really not elegant. However, it works in O(1) memory and O(n) time.

"""
Given an array of words and a length l, format the text such that each line has exactly l characters and is fully justified on both the 
left and the right. Words should be packed in a greedy approach; that is, pack as many words as possible in each line. Add extra spaces 
when necessary so that each line has exactly l characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly
between words, the empty slots on the left will be assigned more spaces than the slots on the right. For the last line of text and
lines with one word only, the words should be left justified with no extra space inserted between them.

Example

For
words = ["This", "is", "an", "example", "of", "text", "justification."]
and l = 16, the output should be

textJustification(words, l) = ["This    is    an",
                               "example  of text",
                               "justification.  "]
"""

def textJustification(words,width):
    def evenSplit(line,charcount,wordsCounted):
        if charcount + wordsCounted-1 > width:
            return False
        if wordsCounted == 1:
            line = line[0]
            return line.ljust(width)
        s = ""
        totalSpaces = width-charcount
        spacePerWord = totalSpaces // (len(line)-1)
        extraSpaces = totalSpaces - (spacePerWord*(len(line)-1))
        for pos,word in enumerate(line[:-1]):
            s += word + " "*max((spacePerWord + (pos<extraSpaces)),1)
        s+= line[-1]
        if len(s) != width:
            return False
        return s
    final = []
    thisline = words[0]
    strToJustify = words[0]
    curlength = len(words[0])
    charlength = len(words[0])
    wordsCounted = 1
    for i in words[1:]:
        if not evenSplit((strToJustify+"|"+i).split("|"),charlength+len(i),wordsCounted+1):
            if wordsCounted == 1:
                final.append(thisline.ljust(width))
                thisline = i
                strToJustify = i
                charlength = len(i)
            else:
                final.append(evenSplit(strToJustify.split("|"),charlength,wordsCounted))
                thisline = i
                strToJustify = i
                wordsCounted = 1
                charlength = curlength = len(i)
        else:
            strToJustify += "|" + i
            wordsCounted += 1
            charlength += len(i)
    final.append(strToJustify.ljust(width).replace("|"," "))
    return final
