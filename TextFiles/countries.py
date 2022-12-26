input_filename= 'country_info.txt'
countries= {} # This wil be helpful later on.
countries_code= {} # this will be useful later on.

with open(input_filename) as country_file: # read the input file
    country_file.readline() # readline() will read the line and then move on to the next line. This means that, it will read the line containig
    # the country, code etc. and then will not save it. But, then for loop below will be free to move on to the actual content without saving the line
    # that is not required. 
    for row in country_file: # read each row of the file
        data= row.strip('\n').split('|') 
        # split the row at the pipe character. But if we use only .split('|') each line will end in a \n character. 
        country, capital, code, code3, dialing, timezone, currency= data
        # print(country, capital, code, code3, dialing, timezone, currency, sep= '\n\t') #print the output of the above command. Uncomment this because it is not required.
        # The goal is to move the contents of each of the country to a dictionary
        country_dict= {
            'country': country,
            'capital': capital,
            'code': code,
            'code3': code3,
            'dialing': dialing,
            'timezone': timezone,
            'currency': currency
        }

        # print(country_dict) # uncomment this line when you want to see the output.

        #The next goal is to be able to search the country by its name. This can be done by making the dictionry inside a dictionary.
        countries[country.casefold()] = country_dict 
        # casefold() method is important here. Need to understand how this works exactl.......

        # If we want to sort the dictionary by using the country code, we can do something like this
        countries_code[code.casefold()]= country_dict

print(country_dict)

# print(countries) #This line is for finding out if the program works. Uncomment if needed.


# The challange is to get a country name from the user and print the capital city for that country from the data above.

# country_choosen = str(input('Please choose a country. We will tell you what is the capital of that country.'))

# sub_dict = countries[country_choosen]
# print(sub_dict)

# country_cpaital = sub_dict['capital']

# print(f"the capital of {country_choosen} is {country_cpaital}.")


         