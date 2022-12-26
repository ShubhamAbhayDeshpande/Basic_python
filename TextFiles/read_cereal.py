"""
In this program we will see what are the advantages that a correctly 
quotated string can provide in the csv file

"""

import csv

csv_filename = 'cereal_grains.csv'
with open(csv_filename, encoding= 'utf-8', newline='') as csv_file:
    reader= csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC) # We tell the reader function here how the data has been quoted with the quoting argument. QUOPTE_NONNUMERIC will tell the program that all the non numeric values are quoted strings.
    for row in reader:
        print(row)