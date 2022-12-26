"""
This code will demonstrate the shallow copy for the mutavble object like dictionary.

Shallow copy will copy the same dictionary to the different memory location. 
and so the changes in one dictionary will be reflected in the second dicionary even if you never touch the second dicionary.

"""

# Important thing in the below dictionary is that, it might look like the list is in the dicionary. But in reality, it is in the memory somewhere and 
# it is just referenced in the list. Hence when the append happens, the reference is updated. And since it is the same reference in both lists, the change
# is reflected in both dictionaries. 

# The shallow copy copies the reference to the list and not the actual dictionary.

animals= {"lion": ["scary", "big", "king"],
"elephant": ["big", "grey", "wrikly"],
"teddy": ["cuddly", "cute"]
}

things = animals # This line does not make a copy of the original dictionary. The 'things' will represent the same dictionary as a 'animals'
print(things["teddy"])
print(animals["teddy"])

print()

# To prove that the above are the same dictionary, we will append the teddy dictionary and print the output again.
animals["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])

"""The following program will be using the deep copy. And we will check the difference between the deep copy and the shallow copy."""

import copy # copy module will provide the deep copy method.

animals2= {"lion": ["scary", "big", "king"],
"elephant": ["big", "grey", "wrikly"],
"teddy": ["cuddly", "cute"]
}
things2= copy.deepcopy(animals2)

print()
animals2["teddy"].append("toy")
print(things2["teddy"])
print(animals2["teddy"]) # This time only the animals2 will be appended with the change in the dictionary. This shows that the two lists are not the same. 

# This means that objects are copied from one location to another. Not just the references to the objects. 

