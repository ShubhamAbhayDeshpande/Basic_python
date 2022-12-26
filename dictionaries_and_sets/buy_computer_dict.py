available_parts = {"1": "computer",
                    "2": "monitor",
                    "3": "keyboard",
                    "4": "mouse",
                    "5": "hdmi cable",
                    "6": "dvd drive"}

current_coice = None

while current_coice != "0":
    if current_coice in available_parts: #pay attention here. The 'in' will only check keys in the dictionary. It will not check the values. (In the list, 'in' check the values in the list )
        chosen_part =available_parts[current_coice]
        print(f"Adding {chosen_part}")
    
    # We are adding this part just for the fun. 
    if current_coice != 0 and current_coice not in available_parts.keys(): # What are we trying to do here is that, if the entered value is invalid print a message. And also print the valid choices.
        print("The valid choices are:")

        for keys, values in available_parts.items():
            print(keys)

        print("To quit the program, enter '0'. ")

    current_coice= input("> ")