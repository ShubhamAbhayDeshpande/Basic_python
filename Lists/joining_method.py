flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily"
]

"""This is one way of taking care of the iterations in the list. The other method is to use the join method."""
# for flower in flowers:
#     print(flower)

"""The join method will take care of the iterables for us. join() is a method of the string class. Hence it will 
expect the separator to be a string."""

separator = " | "

print(separator.join(flowers))

"""Important thing to remember is that the iterable in the list must be strings for the join() method to work. 
If it is a mixed list, then join() will not be able to iterate over the list.

In the .join(str) method the string input is always a list. Otherwise the mehtod may not work."""