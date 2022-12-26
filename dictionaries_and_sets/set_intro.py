""" 
This is an intriductory file for the python sets.

*********************SETS ARE UNORDERED.********************************************

"""

# Create a set called farm_animals
farm_animals ={'cow', 'sheep', 'hen', 'goat', 'horse'}# sets are written with {}. But, python can tell it is a set and not a dictionary because we have not used keys and values.
print(farm_animals) # Printing the set values. The order of the set will change each time the program is run. This is important because the sets are un-ordered. 

# set can be iterate over
for animal in farm_animals:
    print(animal)

#since the sets are not ordered. We will probably not iterate over it frequently.

# Sets use hash function to store the items in them. Hence, consequently, all the elements of the set must be hashable. Similar to the key values of the set. 
# So this means, no mutable data structures (lists for example) can be an element of a set.

# Since the sets are un-ordered, you cannot index into a set. 
# Let's compare a list and a set containing the same elements.

animals_list= ['cow', 'sheep', 'hen', 'goat', 'horse']

print(animals_list[2]) # This should print 'hen'
# print(farm_animals[2]) # We should get an error for this line

# This unorderedness of the sets also has a funny implicatoin. If python wants to check if the two sets are equal, it will compare the items in the sets. The order of the items is not important.
# This behavior is different to the rules for comparing the lists or tuples. There the item and the item order both matter. It is proven below. 

more_animals={'sheep', 'cow', 'horse', 'goat', 'hen'}

if more_animals == farm_animals:
    print("The two sets are equal")
else:
    print("The two sets are not equal")
