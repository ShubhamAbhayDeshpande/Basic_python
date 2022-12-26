choice = "-"  # initialise choice to something invalid
while choice != "0":
    #if choice in "12345": # This is not good since, it is not checking the input in the list. Instead use the list() function to make list of the iterable "12345". Or we can similarly use the set() function. 
    if choice in set("12345"): # Set is better choice than list. Because hashing function makes it easy to retrive the values. Sets are a lot quicker than other iterables such as lists or tuples.
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()

# Sets are faster because when a python searches for the set membership using hashcode. It will first calculate the hashcode in it and then check for the same hashcode in the elements 
# of the set. Where as in the list, it will have to match element in the list to the elelment we are checking for. This will take a lot of time. Especially if the lists are huge. 
# This is not the case with the set. A set with millions of members will take the same time as set with ten items.

# This does not mean that we can replace all lists with sets. It is mostly application dependent. So be carefull.