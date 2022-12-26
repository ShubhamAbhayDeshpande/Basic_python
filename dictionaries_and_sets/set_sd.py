"""
The following program will explain the principles of the symmetric difference in the set with an example

"""
morning= {'java', 'C', 'Ruby', 'Lisp', 'C#'}
afternoon= {'python', 'C#', 'Java', 'C', 'Ruby'}

possible_courses= morning^afternoon # This is using operator
print(possible_courses)

# Same thing can be done with calling the methods
print(morning.symmetric_difference(afternoon))

# It is really hard to find a non-mathematical use for the symmetric_difference(). 
