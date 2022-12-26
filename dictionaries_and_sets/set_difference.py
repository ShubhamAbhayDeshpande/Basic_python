"""
The following file will demonstrate the use of the set difference() method with simple examples.

"""

# Imports
from primes_and_squares import squares_generator, primes_generator

evens= set(range(0,50,2))
odds= set(range(1,50,2))
print("odds: ", odds)

# The above sets are good. But, not much usefull for creating the intersection. Since they are disjoint. Which means that there are no common elements.
# But this shows how we can generate a set with mehods and using an iterable.

#The following steps are not required but they provide a good visualization of what the imports do exactly.
primes= set(primes_generator(100))# print all the prime numbers from 1 to 100
print("primes: ", primes) 
squares= set(squares_generator(100))# print all the squares from 1 to 100
print("squares: ",squares) 

# Find the difference between the odds and the primes. If we write odds.difference(primes) this will give us all the elements that are in the odds but not in the union of odds 
# primes or only primes.
print()
print("Using method")
print()
print("Elements in the odds and not in union of odds and primes or only primes: ", odds.difference(primes))
print("Elements in the primes and not in union of odds and primes or only odds: ",primes.difference(odds))

# the above property means that the difference is non commutative. 

# We can do the same with the operator.
print()
print("Using operator")
print()
print("Elements in the odds and not in union of odds and primes or only primes: ", odds-primes)
print("Elements in the primes and not in union of odds and primes or only odds: ",primes-odds)