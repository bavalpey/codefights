"""
Your Informatics teacher at school likes coming up with new ways to help you understand the material. When you started studying numeral
systems, he introduced his own numeral system, which he's convinced will help clarify things. His numeral system has base 26, and its
digits are represented by English capital letters - A for 0, B for 1, and so on.

The teacher assigned you the following numeral system exercise: given a one-digit number, you should find all unordered pairs of one-digit
numbers whose values add up to the number.

Example

For number = 'G', the output should be
  newNumeralSystem(number) = ["A + G", "B + F", "C + E", "D + D"].

Translating this into the decimal numeral system we get: number = 6, so it is ["0 + 6", "1 + 5", "2 + 4", "3 + 3"].
"""
def newNumeralSystem(number):
    num_to_char = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
    char_to_num = {}
    for key in num_to_char:
        char_to_num[num_to_char[key]] = key
    print(char_to_num)
    first = "A"
    second = number
    ans = []
    while char_to_num[first] <= char_to_num[second]:
        ans.append(first + " + " + second)
        try:
            first = num_to_char[char_to_num[first] + 1]
            second = num_to_char[char_to_num[second]-1]
        except:
            break
    return ans1
