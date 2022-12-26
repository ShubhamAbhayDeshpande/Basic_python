""" 
This file will explain the strip, lstrip, and rstrip methods in for reading the files.

ONE VERY IMPORTANT THING TO NOTE HERE IS THAT THESE METHODS DO NOT REMOVE THE CHARACTERS RANDOMLY. IF WE PASS A CHARACTER AS AN ARGUMENT e.g. 'char'

THEN THE METHODS WILL KEEP REMOVING THE CHARACTERS FROM THE STRING UNTIL A NON MATCHING CHARACTER IS FOUND IN THE INPUT STRING. AND BOTH OF THE ENDS OF THE STRINGS ARE TREATED INDEPENDENTLY.

THIS MEANS THAT EVEN IF AT ONE END THE CHARACTERS TO BE REMOVED ARE NO LONGER THERE, BUT THE OTHER END HAS CHARACTERS THAT CAN BE REMOVED, THAT END WILL KEEP REMOVING THE CHARACTERS.
"""

# there are two functions in the python that do something similar to the methods below. But they are available from the python 3.9 onwards. 


filename= 'Jabberwocky.txt'

with open(filename) as jabber:
    first= jabber.readline().rstrip() # rstrip will strip the characters from the right side of the string. this is also called as removing the trailing character. 

print(first)

# .strip() will remove the characters from both sides of the string.

print()

char= "'"
no_appostrophe = first.strip(char)
print(no_appostrophe) #This line will print the same output as the above line but without the appostrophe.