""" This is a file that will save and demonstrate the python capabilities for the JSON format. """

import json

languages = [
    ['ABC', 1987],
    ['Algol 68', 1968],
    ['APL', 1962],
    ['C', 1973],
    ['Haskell', 1990],
    ['Lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]

#In the below example we will write some more languages into a JSON file. The below line will create a test.json file in the folder. 
with open("test.json", "w", encoding= "utf-8") as testfile:
    json.dump(languages, testfile) # .dump() is a method that is used by the python for the json #file. 

# We also need to read the data back in the file. This can be done with the load() method in the #python. 
with open("test.json", 'r', encoding='UTF-8') as testfile:
    data = json.load(testfile)#
    
# to ensure that we can read the data
print(data)
print(data[2]) # This makes sure that the we are also able to read the specific items in the #dataset. This will also confirm that we are reading from a
# list and not a file. 

# This works only if what we are writing in the json file is not a tuple. json does not support 
# the tuples. This is fine because it is not a specific file format for the python. It is a standard for the information interchange. 