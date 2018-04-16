"""
A ciphertext alphabet is obtained from the plaintext alphabet by means of rearranging some characters. For example "bacdef...xyz"
will be a simple ciphertext alphabet where a and b are rearranged.

A substitution cipher is a method of encoding where each letter of the plaintext alphabet is replaced with the corresponding
(i.e. having the same index) letter of some ciphertext alphabet.

Given two strings, check whether it is possible to obtain them from each other using some (possibly, different) substitution ciphers.

Example

  For string1 = "aacb" and string2 = "aabc", the output should be
    isSubstitutionCipher(string1, string2) = true.

  Any ciphertext alphabet that starts with acb... would make this transformation possible.

  For string1 = "aa" and string2 = "bc", the output should be
    isSubstitutionCipher(string1, string2) = false.
"""
def isSubstitutionCipher(string1, string2):
    mydict = {}
    for pos,key in enumerate(string1):
        value = string2[pos]
        if key in mydict and mydict[key] != value:
            return False
        elif value in mydict.values() and key not in mydict:
            return False
        else:
            mydict[key] = value
    return True
        
