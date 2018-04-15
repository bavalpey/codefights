"""
A little boy is studying arithmetics. He has just learned how to add two integers, written one below another, column by column.
But he always forgets about the important part - carrying.

Given two integers, find the result which the little boy will get.

Note: the boy used this site as the source of knowledge, feel free to check it out too if you are not familiar with column addition.

Example

  For param1 = 456 and param2 = 1734, the output should be
    additionWithoutCarrying(param1, param2) = 1180.

       456
      1734
    + ____
      1180

    The little boy goes from right to left:

    6 + 4 = 10 but the little boy forgets about 1 and just writes down 0 in the last column
    5 + 3 = 8
    4 + 7 = 11 but the little boy forgets about the leading 1 and just writes down 1 under 4 and 7.
    There is no digit in the first number corresponding to the leading digit of the second one, so the little boy imagines that 0 is
    written before 456. Thus, he gets 0 + 1 = 1.
"""
def additionWithoutCarrying(param1, param2):
    lst = list(int(i) for i in str(min(param1,param2)))
    lst2 = list(int(i) for i in str(max(param1,param2)))
    lst3 = []
    lst = lst[::-1]
    lst2 = lst2[::-1]
    for x in range(len(lst)):
        test = ((lst[x]+lst2[x])%10)
        lst2[x] = str(test)
    string = ''
    for x in lst2[::-1]:
        string +=str(x)
    return int(string)
