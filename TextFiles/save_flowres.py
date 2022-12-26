
"""
The goal is to write the following data into a file. This is very similar to reading the data from the file.
But the only difference is that we need to specify the 'w' in 'with open()' instead of the default argument 'r' 

"""
data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

plants_filename= "flowers_print.txt" #here we are assigning the name of the file to a variable. It is also fine if we directly write the neame
# of the file in the with open() itself along with the extension.

with open(plants_filename, 'w') as plants:
    for plant in data: 
        print(plant, file= plants) # print() has a keyword argument in the function which will tell it where to write the the contents of the first
        # argument. By default this is the screen. But sometimes we can change it. We tell the print to send the text to an open file.

# It is not much useful if we cannot read the written data from the file. We will see if we can still do that
# create a new dictionary to append the contents of the file.

new_flowers_dict= []

with open(plants_filename) as flowers:
    for flower in flowers:
        flower_to_add= flower.rstrip()
        new_flowers_dict.append(flower_to_add)

#print(new_flowers_dict) # This is just used to visualize the output of the above. Uncomment the line if required.

""" There are other ways to write and store the data in a file. This time using write() method.
There is a difference between the data that is stored in the file by using the above method and
using this method."""

# creating a new file name 
plants_filename_2 = "flowers_write.txt"

# Write the data to the file
with open(plants_filename_2, "w") as plants:
    for plant in data:
        plants.write(plant) # The difference between this method and the print() is that, no special characters will be included such as brackets, commas
        # etc. Also, if there is no conversion that will convert the given argument into a string. If the argument is a integer, it will try to print an
        # integer which can cause an error. 

        #The choice between the write() and print() will be dependent on the usecase. There is no specific rule for that. 
        




