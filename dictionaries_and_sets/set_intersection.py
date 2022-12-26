"""
The following program will demonstrate the intersection between the sets.

"""
# Imports
from primes_and_squares import squares_generator, primes_generator

evens= set(range(0,50,2))
odds= set(range(1,50,2))

# The above sets are good. But, not much usefull for creating the intersection. Since they are disjoint. Which means that there are no common elements.
# But this shows how we can generate a set with mehods and using an iterable.

#The following steps are not required but they provide a good visualization of what the imports do exactly.
primes= set(primes_generator(100))# print all the prime numbers from 1 to 100
print(primes) 
squares= set(squares_generator(100))# print all the squares from 1 to 100
print(squares) 

# Taking the intersection of odds, evens, primes and squares
odds_intersection_square= odds.intersection(squares) # How many perfect squares in the range of odd numbers between 1 to 50
evens_intersection_square= evens.intersection(squares)# How many perfect squares in the range of even numbers between 1 to 50

# Uncomment the following lines to see the output of the above. 
print(odds_intersection_square)
print(evens_intersection_square)

