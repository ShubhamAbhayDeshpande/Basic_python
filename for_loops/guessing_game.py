""" Make computer select a number using random module and try to guess the number with multiple guesses using a while loop. """

# importing the module

import random

highest = 10 
answer = random.randint(0,highest)

user_ip = int(input("Enter a nuber: "))

while answer != user_ip: 
    
    if user_ip < answer:
        print("Guess higher.....")

    elif user_ip > answer:
        print("Guess lower")

    else: 
        break

    user_ip = int(input("Enter a nuber: "))

print("You guessed it right...")

