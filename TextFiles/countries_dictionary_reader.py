""" 
This program will use the DictReader() method  in the csv module to convert the contests of the csv file into a dictionary. 

The important thing here is to maintain the lower case lettering of the contents of all keywords in dictionary. 

"""

# Importing csv module
import csv

countries_csv = 'country_info.csv'

with open(countries_csv, 'r', encoding='utf-8') as file_read:
    dictionary = csv.DictReader(file_read)

    print(type(dictionary))

    # for keys in dictionary.keys():
    #     dictionary[keys] = dictionary[keys].lower()

    for row in dictionary:
        print(dictionary['Country'])

#Country|Capital|CC|CC3|IAC|TimeZone|Currency


