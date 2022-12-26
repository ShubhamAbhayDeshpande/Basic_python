"""
Various methods for removing the items from a set

"""
small_ints= set(range(21)) # This set will not be ordered. 
print(small_ints)

# Clearing all items from the set
small_ints.clear()
print(small_ints)

small_ints= set(range(21)) # This set will not be ordered.

# Deleting the items from the set. discard() and remove() methods
small_ints.discard(10) # This will remove 10 from the set
small_ints.remove(11)# This will remove 11 from the set
print(small_ints)

# If we try to remove an item that does not exists in the set, discard() will work. remove() will not work.
small_ints.discard(99)
small_ints.remove(99) # This should give an error. 
print(small_ints)


