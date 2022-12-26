"""
The goal of this program is to demonstrate the union of the two sets who have some elements in common.

Some code is commented that is mostly print statement. If you want to see the output of any code, please uncomment it in the following code lines.

"""
farm_animals= {"sheep", "hen", "cow", "horse", "goat"}
wild_animals= {"lion", "elephant", "tiger", "goat", "panther", "horse"}

all_animals_1= farm_animals.union(wild_animals)
#print(all_animals_1)

#Let's see what happens if we keep the wild_animals first.

all_animals_2= wild_animals.union(farm_animals)
#print(all_animals_2)

# There is another way to denote the union by using the pipe operator.
all_animals_3= wild_animals | farm_animals
#print(all_animals_3)

# UNION OF TWO SETS IS COMMUTATIVE. 

from priscription_data import adverse_interactions

# Make a list of all the medications. This list should be sorted alphabetically.

meds_to_watch= set()

for interaction in adverse_interactions:
    meds_to_watch2= meds_to_watch.union(interaction)# This is not very efficient since this operation will create a new set everytime we go around the loop.
    # We can imporove this by using update() union. 

    # Getting the same output using the update() method.
    meds_to_watch.update(interaction) # update() can also be written as |= 


# This is jsut to prove that both methods get the same output.
print(sorted(meds_to_watch))
print(sorted(meds_to_watch2))
print()
print()

############################# Following is just the practice for the union of the two sets.############################################

scorpions= {"emporor", "red_claw", "arizona", "forest", "fat_tail"}
snakes= {"python", "cobra", "viper", "anaconda", "mamba"}
spiders= {"tarantula", "black_widow", "wolf_spider", "crab_spider"}
vaspas={"yellow_jacket", "hornet", "paper_wasps"}

# Creating a union of sets of all the insects that bite. Do this by using the 'union method'.
things_that_bite= spiders.union(snakes)
print("List of things that bite: ",sorted(things_that_bite))

# Creating a union set of all the things that sting do this by using the 'union operator'.
things_that_sting= scorpions | vaspas
print("List of things that sting: ",sorted(things_that_sting))

# Spiders and scorpions are both aracnids. Make an empty set called aracnids and update it with the spiders and scorpions.
arachnids= set()
arachnids.update(spiders) # by using the 'update method'
arachnids |= scorpions# by using the 'update operator'
print("List of all the animals that come under arachnids category: ", sorted(arachnids))

# One advantage of using methods over the operators is that methods can take multiple argumetns. Hence in theory, we can make union of two or more sets in one statement more easily.
# This can be reason why people use the methods over operators. 