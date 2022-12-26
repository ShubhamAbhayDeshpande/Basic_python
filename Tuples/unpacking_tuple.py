#We can assign multiple values to the variables in the python. 




x,y,z = 1,4,6 # these values are actually tuples.

# Following code is what is referred to as unpacking a tuple
print(x)
print(y)
print(z)


# Unpacking a tuple

data = 1,4,6 # this is a tuple
x,y,z = data # The values on the left may look like a tuple but they are not a tuple. They are variables. And these variables get their values from the tupel data. 
# we can never have tuple on the left side of '=' because they are immutable. 
print(x)
print(y)
print(z)


"""Unpacking a tuple can be very helpful with the enumerate. As shown in the example below."""

for idx, char in enumerate("abcdefghi"):
    t = idx, char # Here we are creating a tuple. Now imagine appending this tuple to a empty list defined prior. 
    print(t)
    index = t[0]
    character = t[1]
    print("Character", character)
    print("Index",index)

"""We can use the unpacking of the tuple to make the program a bit more simpler."""
table = ("Coffee",200,100,75,34)
print(table[1]*table[2]) #Calculating the area of the table in an unreadable code.

# We can do the same thing by unpacking the tuple.
table_type, length, width, height, price = table
print("Area of the table is: ", length*width)