"""
It is very common to get the data from a third party source in the real world. That case the most common format is a list. We will write a function here that will convert
the given list into a dictionary.

"""
# The given list. 
computer_parts = [ "computer",
                     "monitor",
                     "keyboard",
                     "mouse",
                     "hdmi cable",
                     "dvd drive"]

def make_dict(convert):
    """
    This function will take a list as an input and will convert it to the dictionary and give that dictionary as an output. 
    
    """
    output= {} # This is the dictionary that will be returned. So defining it as an empty dictionry for now. 
    for i in range(len(convert)):
        output[i]= convert[i]
    
    return output

available_parts= make_dict(computer_parts)

current_coice = None

while current_coice != "9":
    if current_coice in available_parts: #pay attention here. The 'in' will only check keys in the dictionary. It will not check the values. (In the list, 'in' check the values in the list )
        chosen_part =available_parts[current_coice]
        print(f"Adding {chosen_part}")
    
    # We are adding this part just for the fun. 
    if current_coice != 0 and current_coice not in available_parts.keys(): # What are we trying to do here is that, if the entered value is invalid print a message. And also print the valid choices.
        print("The valid choices are:")

        for keys, values in available_parts.items():
            print(keys)

        print("To quit the program, enter '9'. ")

    current_coice= input("> ")