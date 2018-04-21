"""
While migrating to a new operation system, you faced an unexpected problem: now you need to create a new build command for your favorite
text editor plugin. The build command is stored as a JSON file that you should now update. In order to make the transition simpler, you
decided to write a program that will create a template of the build command by replacing everything but dictionaries in given jsonFile
with their default values: numbers with 0, strings with "" and lists with [].

It is guaranteed that there are only aforementioned types in the given JSON file.

Example

  For

  jsonFile =
  {
      "version": "0.1.0",
      "command": "c:python",
      "args": ["app.py"],
      "problemMatcher": {
          "fileLocation": ["relative", "${workspaceRoot}"],
          "pattern": {
              "regexp": "^(.*)+s$",
              "message": 1
          }
      }
  }
  the output should be

  buildCommand(jsonFile) =
  {
      "version": "",
      "command": "",
      "args": [],
      "problemMatcher": {
          "fileLocation": [],
          "pattern": {
              "regexp": "",
              "message": 0
          }
      }
  }
  
"""
import json
from collections import OrderedDict

def dict_parser(data):
    for key in data:
        print(type(data[key]))
        print()
        if type(data[key]) == str:
            data[key] = ""
        elif type(data[key]) == list:
            data[key] = []
        elif type(data[key]) == int or type(data[key]) == float:
            data[key] = 0
        elif type(data[key]) == OrderedDict:
             data[key] = dict_parser(data[key])
    return data
    
def buildCommand(jsonFile):
    data = json.loads(jsonFile, object_pairs_hook=OrderedDict)
    return json.dumps(dict_parser(data))
