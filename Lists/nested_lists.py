even = [2,4,6,8]
odd = [1,3,5,7,9]

# Concatenating the lists

concat = even+odd

# Uncoment the following to see the output. Or use debugger
# print(concat)

# we can make a nested list instead. 

numbers = [even, odd]
print(numbers)


# Use the nested for loop to print the items in the nested list

for number_list in numbers:
    print(number_list)
    for num in number_list:
        print(num)


    