"""
The following set will demonstrate the intersectin method for both sets with a simple example.

"""

trial1= {"Bob", "Charley", "Georgia", "John"}
trial2= {"Anne", "Charley", "Eddie", "Georgia"}

check_set= trial1.intersection(trial2)

print(check_set)

farm_animals= {"sheep", "hen", "cow", "horse", "goat"}
wild_animals= {"lion", "elephant", "tiger", "goat", "panther", "horse"}
potential_rides= {"donkey","horse", "camel","elephant"}

# Use the inertsection() method to create an intersection of all 3 sets
inetersection= farm_animals.intersection(wild_animals, potential_rides) # Another advantage of using method is that we can use to operate on more than two sets.
print("intersection using method: ",inetersection)

# Same thing if want to do with the operator we have to do this 
intersection2 = farm_animals & wild_animals & potential_rides
print("intersection using operator: ", intersection2)
print()
print()


####################################### The following is an exercise for using the intersection() method in python ########################################################
"""
Your task for this coding exercise is to find out which prepositions have been used in the quote:

"Education is not the learning of facts but the training of the mind to think – Albert Einstein"

There are two steps you'll need to perform:

Split text to create a list of words.

Create an intersection of the set of words with the prepositions set that we've provided in the exercise code.

"""

text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

text_set = set(text.split())

# Finding the prepositions in the sentence using intersection() method

print("Prepositions in the sentence are: ", prepositions.intersection(text_set))


