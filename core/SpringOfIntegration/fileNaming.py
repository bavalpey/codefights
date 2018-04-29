"""
You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes
later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not
used yet.

Return an array of names that will be given to the files.

Example

For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
  fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].
"""
def fileNaming(names):
    j = []
    for i in range(len(names)):
        print(names[i])
        c = j.count(names[i])
        if c == 0:
            j.append(names[i])
        else:
            temp = names[i] + '(' + str(c) + ')'
            while j.count(temp) > 0:
                c += 1
                temp = names[i] + '(' + str(c) + ')'
            j.append(temp)
    return j
