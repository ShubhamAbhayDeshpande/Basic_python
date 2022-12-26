# shopping_list = ["Milk","Bread","Eggs","spam","Coffee"]

# """The goal of the program is to not print the "spam" in the list above. 

# We are going to use the "continue" statement for that"""


# for item in shopping_list:
#     if item == "spam":
#         continue
#     """The continue statement will not exit out of the loop but it will not execute the rest of the statements in the loops 
#     and will go directly to the next iterable variable in the loop."""
#     print("Buy "+ item)

"""The goal of the program is to print the output of the numbers between 0 and 20 that are not divisible by 3 or 5"""
non_div = []
for i in range(0,20):
    if i%3 == 0 or i%5 == 0:
        continue
    non_div.append(i)

print("The numbers between 0 to 20 that are not divisible 3 or 5 are: ", non_div)