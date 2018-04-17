"""
When you recently visited your little nephew, he told you a sad story: there's a bully at school who steals his lunch every day, and
locks it away in his locker. He also leaves a note with a strange, coded message. Your nephew gave you one of the notes in hope that you
can decipher it for him. And you did: it looks like all the digits in it are replaced with letters and vice versa. Digit 0 is replaced
with 'a', 1 is replaced with 'b' and so on, with digit 9 replaced by 'j'.

The note is different every day, so you decide to write a function that will decipher it for your nephew on an ongoing basis.

Example

For note = "you'll n4v4r 6u4ss 8t: cdja", the output should be
  stolenLunch(note) = "you'll never guess it: 2390".
"""
def stolenLunch(note):
    my_dict = {'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j'}
    msg = ""
    reverse = {}
    for key in my_dict:
        reverse[my_dict[key]] = key
    for char in note:
        if char in my_dict:
            msg += my_dict[char]
        elif char in reverse:
            msg += reverse[char]
        else:
            msg += char
    return msg
