#closing a file after reading or opening it is important. 
# If this is not done then we might run into problems. Especially in windows. If the files are not closed
# correctly, we can run out of file handles. These handles are used by Mac or linux OS to keep track of which files 
# have been open. Another thing that can happen is the newly written data can be lost.
# 
# The following is a more pythonic way of openinga text file.
# 
#

with open('Jabberwocky.txt', 'r') as jabber: # Note that this is a statment, os we do not need to assign a variable to it. 
    for line in jabber:
        print(line.rstrip()) # This method will strip the right character from the file.

# Writing the files this way is important because, this will close the file automatically when the use of the file
# is done. So that there can be no way we forget to close the file and cause a problem. 

# There are other ways of reading the lines directly from the text file without using the for loop.

with open('Jabberwocky.txt', 'r') as jabber:
    lines_list= jabber.readlines() # This readlines() will store all the lines in the file as a list. 
    print(lines_list)

# An advantage of this method is that the lists are iterable. We cab simply take the last line 
print()
print(lines_list[-1]) # This will give the last line giving the author name. 
print()

# the read() method will give all the content of the file as a string. 
with open('Jabberwocky.txt') as jabber: #the default mode is to read the file if one is not specified.
    lines_string= jabber.read()
    print(lines_string)

# the output of the above may look the same but it is a string and not a list or plain text. 


