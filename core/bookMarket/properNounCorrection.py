"""
Proper nouns always begin with a capital letter, followed by small letters.

Correct a given proper noun so that it fits this statement.

Example

For noun = "pARiS", the output should be
properNounCorrection(noun) = "Paris";
For noun = "John", the output should be
properNounCorrection(noun) = "John".
"""
def properNounCorrection(noun):
    noun = noun.lower()
    return noun[0].upper() + noun[1:]
