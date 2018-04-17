"""
You've intercepted an encrypted message, and you are really curious about its contents. You were able to find out that the message
initially contained only lowercase English letters, and was encrypted with the following cipher:

Let all letters from 'a' to 'z' correspond to the numbers from 0 to 25, respectively.
The number corresponding to the ith letter of the encrypted message is then equal to the sum of numbers corresponding to the first i
letters of the initial unencrypted message modulo 26.
Now that you know how the message was encrypted, implement the algorithm to decipher it.

Example

For message = "taiaiaertkixquxjnfxxdh", the output should be
  cipher26(message) = "thisisencryptedmessage".
The initial message "thisisencryptedmessage" was encrypted as follows:
  letter 0: t -> 19 -> t;
  letter 1: th -> (19 + 7) % 26 -> 0 -> a;
  letter 2: thi -> (19 + 7 + 8) % 26 -> 8 -> i;
etc.
"""
def cipher26(message):
    num_to_char = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:
    'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'} # this dictionary maps number values to the corresponding letter
    # it could be done easier with ascii values, but I chose to hard code it.
    char_to_num = {} # char to num is a dictionary that is like num_to_char but in reverse.
    for key in num_to_char:
        char_to_num[num_to_char[key]] = key # 
    sm = char_to_num[message[0].upper()]
    ans = message[0]
    for char in message[1:]:
        num = 26 + char_to_num[char.upper()] - sm
        ans += num_to_char[num%26]
        sm += num
        sm %= 26
    return ans.lower()

