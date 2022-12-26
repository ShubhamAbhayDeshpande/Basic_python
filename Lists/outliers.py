"""It is useful to know how to delete the items from the list."""

data = [4,5,104,105,110,120,130,150,160,170,183,185,188,191,350,360]

# The first two and the last two values are way bigger than the others. They are the outliers.

# del data[0:2] # deleting the first two values
# print(data)
# del data[-2:] # deleting the last two values of the list
# print(data)

min_val = 100
max_val = 200

"""The code below may look good but it will not work in the reality. Check the code in the debugger for the check why it will not
work """
# for idx,num in enumerate(data):
#     if (num<min_val) or (num>max_val):
#         del data[idx]

# print(data)

"""The following code uses reversed() for reversed iterator"""

for idx, i in enumerate(reversed(data)):
    print(idx, i)

"""in the program above, the index positions are reversed. But, the index still starts at zero."""

