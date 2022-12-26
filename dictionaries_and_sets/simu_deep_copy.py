"""
The goal is write a function that will simulate the deepcopy() method from the copy module.

This is a challange in the course.

"""

def deep_copy(d: dict)->dict:
    dicto= {}
    for key, value in d.items():
        new_key= key
        dicto[new_key]= value

    return dicto


animals= {"lion": ["scary", "big", "king"],
"elephant": ["big", "grey", "wrikly"],
"teddy": ["cuddly", "cute"]
}

things = deep_copy(animals)

# printing the id's of the memory locations and the actual dictionaries in that location. 
print(id(animals), animals)
print(id(things), things)