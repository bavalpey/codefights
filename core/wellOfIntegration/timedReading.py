"""
Timed Reading is an educational tool used in many schools to improve and advance reading skills. A young elementary student has just
finished his very first timed reading exercise. Unfortunately he's not a very good reader yet, so whenever he encountered a word longer
than maxLength, he simply skipped it and read on.

Help the teacher figure out how many words the boy has read by calculating the number of words in the text he has read, no longer than
maxLength.
Formally, a word is a substring consisting of English letters, such that characters to the left of the leftmost letter and to the right
of the rightmost letter are not letters.

Example

For maxLength = 4 and
  text = "The Fox asked the stork, 'How is the soup?'",
the output should be
  timedReading(maxLength, text) = 7.

The boy has read the following words: "The", "Fox", "the", "How", "is", "the", "soup".
"""
def timedReading(maxLength, text):
    count = 0
    newtxt = ""
    for char in text:
        if char.isalpha():
            newtxt += char
        elif char == " ":
            newtxt += char
    for i in newtxt.split(" "):
        if len(i) <= maxLength and len(i) != 0:
            count += 1
    return count
