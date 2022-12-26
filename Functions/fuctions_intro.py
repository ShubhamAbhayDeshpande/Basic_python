# Import section
# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
 
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


"""Create a simple fuction that multiplies the two numbers"""

from cmath import e
from re import I
from turtle import backward

from pyparsing import col


def multiply(x,y):
    result = x*y 
    return result


def is_palindrome(string):
    """The fuction will check if the enterd word is a palindrome or not. This fucntion is not case sensitive. And it only works on the words and not sentences."""

    string = string.lower() # This should make the function ignore the case of the letters in the word.
    backwards = string[::-1] # This line will create a 'backwards' variable that will be later compared with the original string.
    return string==backwards # The output of the comparison will be either true or false. 

def is_sentense_palindrome(ip_sentense):
    import string
    valid = set(string.ascii_letters) # This will create a set of valid ascii characters 
    sentense = ''.join([ch for ch in ip_sentense if ch in valid]) # This line checks if the character in the input sentence is a valid and if yes then adds it to the list.
    # sentense = sentense.lower() #ignores the case of the character. 
    # backward=sentense[::-1] # form the backward sequence.
    # return sentense==backward # return a boolean by comparing the forward and backward sequence.

    """We can do this in the way that is shown above or, we can use call a function in another function."""
    return is_palindrome(sentense)

# Function calling a function.......

"""The following function can be used to check if the value entered by the user is a integer or not """
def check_integer(temp):
    i =1 
    if i ==1:
        if temp.isnumeric():
            return print("This is a number....")
            
        else:
            print("this is not a number, try again.")
            i+=1

    while True:

        temp = input("let's see if you can enter a number: ")
            
        if temp.isnumeric():
            return print("This is a number....")

        else:
            print("this is not a number, try again.")




def sum_odd_even(n,t):
    """In this function, we have to write a function named sum_eo with the following parameters:

    n: a positive number

    t: a str

    If t has the value 'e', the function should return the sum of all even natural numbers less than n.

    Else if t has the value 'o', the function should return the sum of all odd natural numbers less than n.

    For any other values of t return -1."""

    start = 0
    sum = 0

    if t == 'e' or 'E':

        for i in range(start,n):
            if i%2 ==0:
                sum = sum+i

        return print("The sum of all even numbers between 0 and {} is {}".format(n, sum))

    if t == 'o' or 'O':
        for i in range(start,n):
            if i%2 !=0:
                sum = sum+i

        return print("The sum of all even numbers between 0 and {} is {}".format(n, sum))

def fibonacci(n: int) -> int: # The ':int' and the '->' int are the annotations and the type hints respectively for this function.
    """
    Print the nth Fibonacci number. The value of n should be always positive
    
    """
    if n < 0:
        raise ValueError("The number entered must be a positive Integer.")
    
    if 0<=n<=1:
        return n
    
    n_minus_1, n_minus_2 = 1,0

    for n in range(n-1):
        result = n_minus_2 + n_minus_1
        n_minus_2 = n_minus_1
        n_minus_1 = result
    
    return result

def color_print(text: str, effect: str) -> None : 
    """Takes some input string and the colour which you want to print it in and will print the string in that colour. 
    Generally this function will work just fine in any IDE. But, if you are using it from the command prompt then make the following changes because the
    command prompt will not be able to show the colours in the output. """
    
    output = "{0}{1}{2}".format(effect, text, RESET)
    print(output)


def FizzBuzz(number: int)->str:
    """
    This function takes a single integer as a value. 
            
    If the input integer is divisible by 3, 'Fizz' will be printed, if it is divisible by 5, 'Buzz' will be printed,
    if it is divisible by both 3 and 5, 'FizzBuzz' will be printed. 
    
    In any case, the output will always be a string. 
    
    """

    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)

def factorial(number: int) -> int:
    """
    
    Function to calcualte the factorial of number.
    
    entred number has to be an integer. If it is not error is raised. 
    
    """ 
    if type(number)==int:

        for i in range(number):
            if i == 0:
                temp = i 
          
            temp = (i-1)*temp
        
        return print("Factorial of {} is {}".format(number,temp))

    else:
        raise ValueError("int is the only acceptable input. Check input")

    


 
    


        








    




"""
    Following are the test cases for the functions that are written above. 
    To check the use of the functions, uncomment the lines below the docstrings. 
    
"""




"""Test case for palindrome. Uncomment to use. """
# word = input("Input a word to check: ")
# if is_sentense_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

"""Test case to check if the input is a number, uncomment to use."""
# num = input("let's see if you can enter a number: ")

# check_integer(num)

"""Test case for sum of odd or even numbers"""
#sum_odd_even(56,'o')

"""Testing Fibonacci number function"""
# print(fibonacci(36))
# print(fibonacci(-3))

"""Test case for printing the coloured letters in the string."""
# color_print("Shubham", BLUE)
# color_print("work", RED)

"""Test case for FizzBuzz function."""

# for i in range(100):
#     print(FizzBuzz(i))

"""Test case for factorial function."""
print(factorial(8))