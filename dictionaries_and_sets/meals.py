from contents import pantry, recipes

# Go and see the recipies one more time. It is a dictionary that contains the list of ingridients that are required for a recipies. 
# recipies are the key and ingridients are values.
# We want to display the keys(recipies) of the dictionary.

# Creating an empty dictionary for the display.
display_dict={}

#Isolating the keys and the index of the keys.
for index, key in enumerate(recipes): # This enumerate will iterate over the keys of the dictionary recipes. And it will add them to the empty dictionary created earlier.
    display_dict[str(index+1)] = key  # Convert the index from the integer to a string. This is just the simplicity of the user and the use in general.
    
# Now the time to print our values.

while True:
     print('Please choose the recipe you want to cook:')
     print("-----------------------------------------------")
     for key, value in display_dict.items():
        print(f"{key} - {value}")

     choice= input(": ")

     if choice == "0": # If the choice of the user is 0 then break out of the while loop. 
        break
     elif choice in display_dict:
         print(f"you have chosen, {display_dict[choice]}")# If the choice is anything other than 0, display the name of the recipy.
         dish= display_dict[choice] # Assign the name of the recipy to a variable for further use. 
         print("The ingridients for the recipies are")
         print("-------------------------------------------")
         print(recipes[dish]) # Print the ingridients of the recipy that was selected. from the recipes dictionary. 

         # The next challenge is to check if all the ingridients are availabel in the pantry dictionary.
         ingridients= recipes[dish] # isolate the values for the key given by the dish.
         for indi_ingri in ingridients: # for each individua ingridient in the ingridient list 
            if indi_ingri in pantry:# if the ingridient is available in the pantry list, print its name and quantity required.
               print(f"The {indi_ingri} is available in the pantry and we will require {pantry[indi_ingri]} of it.") 
            else:
               print(f"The {indi_ingri} is out of stock. Sorry :( ") # If not available print this. 
            


      
