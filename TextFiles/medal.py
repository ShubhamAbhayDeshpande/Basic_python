"""
This program contains the code for reading a csv file by using the csv module in python."""

# Standard import
import csv

# Rreading the file 
csv_filename = 'OlympicMedals_2020.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file: # Until now we did not needed a space for the newline character in case of the csv function, csv will take care of this on its own and we do not need to provide it with the additional information. This was not the case with the files that we used earlier.

    headers = csv_file.readline().strip('\n').split(',') # In the csv file it is very easy to isolate the headerd in the files:
    print(f'column headers are: {headers}') # This will put all the column headers in a list. 
    reader = csv.reader(csv_file)
    for row in reader:
       print(row)

