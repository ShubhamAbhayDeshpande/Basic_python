"""
Python provides a in built method that will read the given the csv file and 
convert all the rows of the files to a dictionary. The following code will demonstrate the same.

"""
import csv
cereal_filename = 'cereal_grains.csv'

with open(cereal_filename, encoding ='utf-8', newline='') as cereals_file:
    reader = csv.DictReader(cereals_file)
    for row in reader:
        print(row)
