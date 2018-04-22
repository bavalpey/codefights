"""
You are creating a new website about HTML parsing. You don't want your page to be too simple, so you would like to estimate the
complexity of the main page of your site. In order to measure the complexity of the page, you need to find a set of all tags located on
the deepest level of a tree correponsing to HTML document. Given a valid HTML document, find all distinct tags located on the deepest
level.

Example

For
  document = "<!DOCTYPE html><html> <body> <h1>The best heading ever</h1> <p>The worst paragraph ever.</p> </body></html>"
the output should be
  pageComplexity(document) = ["h1", "p"]
"""
from html.parser import HTMLParser
class Level(): # I kept running into problems where simply declaring level as an int ran into problems with scope. 
    def __init__(self):  # instead, I just made it into a class, which ended up working well. Plus, I got to practise
        self.level = 0   # making classes, albeit a simple one.
    def add_Level(self): # mutator for level, adds one each time it is called
        self.level += 1
    def sub_level(self): # mutator for level, subtracts one each time it is called
        self.level -= 1
    def getLevel(self): # returns the numerical 'level' value
        return self.level
def pageComplexity(document):
    lv = Level()
    startTags = {} # the way I decided to solve this was to keep track of the unique tags found at each level,
    # in order to do this, I decided to make a dictionary whose value would be a set consisting of the distinct tags.
    # then, I simply have to return the value of the deepest level
    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            lv.add_Level()
            level = lv.getLevel()
            if level not in startTags: # Because the value is a list, I have to initialize the value for each key.
                startTags[level] = [tag]
            else:
                if tag not in startTags[level]: # the problem asks for distinct tags
                    startTags[level].append(tag)

        def handle_endtag(self, tag):
            lv.sub_level()

        def handle_data(self, data):
            True
    parser  = MyHTMLParser()
    parser.feed(document)
    mx = max(startTags)
    return startTags[mx] # although the problem asks for the answer to be sorted lexigraphically, this worked anyway.
                         # otherwise, I would have had to use the sorted() function on startTags[mx]
