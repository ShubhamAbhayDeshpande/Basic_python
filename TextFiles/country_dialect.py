"""
This program will look at the dialect class in the csv reader and what it does. 

"""

import csv

input_filename = 'country_info.txt'

countries = {}
with open(input_filename, encoding= "utf-8", newline='') as country_file:
    # Uncomment the following line if you want to see the output with the delimeter. 

    #country_reader = csv.reader(country_file, delimiter= '|') # The delimeter is passed here because this file uses the | character as a seperator in place of a ','.
    #for row in country_reader:
     #   print(row)

################################################################################################# if we have a large number of file that all have a different separator, we cannot go and provide all the delimeter for a single file everytime we read it. The 'sniffer' class in python can help us do that by examining a sample from each file. And then all such attributes that are unique to the files are kept in a single object called the 'dialect'.
##################################################################################################

    sample = country_file.read() 
    countries_dialect = csv.Sniffer().sniff(sample)
    country_file.seek(0) # This step is required because we are reading the enftire file above with .read() method. And we need to somehow reset the file reader head at the start position.
    country_reader = csv.reader(country_file, dialect= countries_dialect)
    for row in country_reader:
        print(row)

print('*'*80)
attributes = ['delimiter',
            'doublequote',
            'escapechar',
            'lineterminator',
            'quotechar',
            'quoting',
            'skipinitialspace']

for attribute in attributes:
    print(f"{attribute} : {getattr(countries_dialect, attribute)}")