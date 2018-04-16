"""
How many strings equal to a can be constructed using letters from the string b? Each letter can be used only once and in one
string only.

Example

For a = "abc" and b = "abccba", the output should be
stringsConstruction(a, b) = 2.

We can construct 2 strings a with letters from b.
"""
def stringsConstruction(a, b):
    c = []
    for char in a:
        if char not in b:
            return 0
        else:
            if a.count(char) == 1:
                c.append(b.count(char))
            else:
                ths = a.count(char)
                store = b.count(char) // a.count(char)
                c.append(store)
    return min(min(c),len(a))
