"""
The goal is to define a function that can take either zero or more agruments without having to go in the function definition and modifying the function definition.

This can be done by using providing *args in the function arguments. 

In python when we write * anything in front of something, it means that that perticular datatype will be automatically unpacked. It is demonstrated below.

"""

tup = (1,2,3,4,5,6,7)

print(tup) #This will print the simple tuple.

print(*tup) # this will print the unpacked tuple.

print() #Just to add an empty line in the output.

# Using the *args in the functions. 

def test_star(*args):
    print(args)
    for x in args:
        print(x)


"""Testing the test_star function with the same tuple as above"""
test_star(1,2,3,4,5,6,7)

""""Similar to the *args we can use the **kwargs for specifying eiher no or more than one keyword arguments. 

The problem with the  functions is that, we need to spesify the arguments in the correct order and inorder to use them in the function.

This is demonstrated by the function below. """

def func(p1, p2, *args, k, **kwargs):
    print("The positional arguments are: {} and {}".format(p1, p2)) # This should return the type of the arguments passed in the p1 and p2.
    print("The generalized arguments are: {}".format(args)) # This should return a tuple for the number argumetns that are passed after p1 and p2 but before k.
    print("The first keyword argument is: {}".format(k)) # should return whatever the arguments that are provided to the k. 'k' is important because it will tell the program where to stop the *args values. 
    print("var-keyword arguments are: {}".format(kwargs)) #var-keyword arguments are explained in the section of dictionaries. 

# correct use case of the function.

func(1,2,3,4,5,k=6,k1=7,k2=8)


"""Sum of the numbers in tha argument."""

def sum_numbers(*args: float) -> float:
    result =0
    for number in args:
        result = result+number

    return result


"""Checking for the function written above"""

print(sum_numbers(1,2,3,4,5,6,7))



