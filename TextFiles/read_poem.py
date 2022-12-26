"""
We will see how to open a file in a cleaner way later on but for now we will see how to open a file and read lines 
from it. 

"""
jabber = open('Jabberwocky.txt', 'r')

# we can iterate over the file and read lines from it as follows.

for lines in jabber:
    print(lines.strip())

jabber.close()

# closing a file after reading or opening it is important. 
# If this is not done then we might run into problems. Especially in windows. If the files are not closed
# correctly, we can run out of file handles. These handles are used by Mac or linux OS to keep track of which files 
# have been open. Another thing that can happen is the newly written data can be lost. 
# The reason the output is doubled spaced is because, there is a new line character at the end of each line in the file. 
# We are not able to see it.
# So we can simply strip these characters from the lines end. As shown above. 

# we can use 'end' to supress the automatic new line that is printed in automatically.

