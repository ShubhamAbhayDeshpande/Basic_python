"""
This is the file for various set operations

"""

# There is only way of creating an empty set
numbers= {*""} # this should be avoided at all costs. The thing after * can be anything. such as {*{}}
print(numbers, type(numbers))

# Adding numbers to an empty set
numbers.add(1)
print(numbers)

# Since the sets contain only the unique values, we can take advantage of this.

# num= set()
# while len(num)<4:
#     next_value= int(input("Enter a number.")) # Since the set has only unique values, it will ignore the input if the value is already present in the set.
#     num.add(next_value)

# print(num)

# we can convert an iterable like a list to set to eleminate the duplicate element in the list
data= ["blue", "green", "white", "blue", "red", "red", "green", "blue", "black" ]
unique_data= set(data) # The order of the set will change everytime the program is run. 
print(unique_data)

# if we want a unique order, then we should use the methods from the dictionary
unique_data_sorted= list(dict.fromkeys(data))# dict.fromkeys() will create the keys from the iterable. list() will convert the keys of the dictionary into a list.
print(unique_data_sorted)

