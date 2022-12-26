"""
This function will have recursive function. It is a function that will call itself.
The example of recursive function is calculating the factorial.

similar thing can be done for calculating the fibonacci series. 

"""


# The way of calculating factorial without the recursive function is as follows:
def fact(n):
    """calculate n facttorial"""
    result =1

    if n>1:
        for f in range(2, n+1):
            result *= f
        return result
        
# Uncomment the following lines to see the result of the above function. 
# for i in range(110):
#     print(i, fact(i))

# Following lines shows how to use a recursive function.
def factorial(n):
    """
    This function will calculate n recursively

    This is interesting because here we can see that for calculation of factorial 4, we need to calculate the 
    factorial for the number 3, 2 and 1 first which are calculated by the same function using the same method.

    So, technically speaking this is not different than one function calling the same function again and again.

    Here the important thing is the first if condition. This will cause the function to return some value at some point.
    Without this condition, the function will run infinite times.
    
    """

    if n<1:
        return 1
    else:
        return n*factorial(n-1)

# Uncomment the following line
# for i in range(110):
#      print(i, fact(i))


