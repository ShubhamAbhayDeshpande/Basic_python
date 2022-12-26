d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

d2= {
    7: "lucky seven",
    10: "ten",
    3: "this is the new three",
}

# we can create a dictionary from the items in a list. We are going to use the 'dict' class.
new_dict = dict.fromkeys(pantry_items)
print(new_dict) #All the vlaues in this dictionary will be None.

new_dict_1= dict.fromkeys(pantry_items, 0) # This will put all the values in the new list to 0.
print(new_dict_1)

# Get the keys from the existing dictionary.
keys= d.keys() # This is a legacy function with not much of the use case. It will sort of return the values in a list. 
print(keys)
# One example of this is to make the program a little bit easy to read. 
for items in d.keys(): #Now it is clear what we are iterating over.
    print(items)

# Similar to keys() there is also values() method for values in the dictionary.
print(d.values())
# this will return values which will be auto updated if the keys and values are added in the dictionary
d[10]= "ten"
print(d.values())
# these values are not iterable. 


# Update Method. This method will either add new values from the one dictionary to another or will replace the value in the old dictionary 
# with the value in the new dictionary provided that the key is the same in the old and the new dictionary. 
# Important thing is that this method will not change the position of the key. Will only change the value. New key value pair will be incerted at
# the end.

d.update(d2)
print(d)