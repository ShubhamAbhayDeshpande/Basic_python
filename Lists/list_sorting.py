"""Sorting the elements of a string in a list"""

sort_this = "The quick brown fox jumps over the lazy dog"

sorted_list = sorted(sort_this)

print(sorted_list)

# The same method can be used for sorting the numbers as well. 

# If we want the alphabets to be sorted in the manner that the spaces are not counted and the letters appear in case sensetive manner
# then we need to add a keyword in the sorted method called str.casefold.

sorted_alphabetically = sorted(sort_this, 
                                key = str.casefold)

print(sorted_alphabetically)

"""when you sort the list of certain type of objects, the list after sorting will contain the objects that make the list.

example :- The string is made of the characters so, the sorted list will also contain characters.  """