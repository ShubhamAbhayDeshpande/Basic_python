"""
In this program we will write a csv file.
We need to:
1. Open a csv writer 
2. Open a csv fiel 
3. Write the data

"""
import csv

cereals = [
    ["Barley", 556, 1.7, 32.9, 10.1, 13.8],
    ["Durum", 339, 5, 27.4, 4.09, 9.7],
    ["Fonio", 240, 1, 4, 1.7, 0.05],
    ["Maize", 442, 7.4, 37.45, 6.15, 11.03],
    ["Millet", 484, 2, 37.9, 13.4, 9.15],
    ["Oats", 231, 9.2, 35.1, 10.3, 3.73],
    ["Rice (Brown)", 346, 2.8, 38.1, 9.9, 0.8],
    ["Rice, (White)", 345, 3.6, 37.6, 5.4, 0.1],
    ["Rye", 422, 2, 31.4, 18.2, 21.2],
    ["Sorghum", 316, 3, 37.8, 9.92, 9.15],
    ["Triticale", 338, 1.81, 36.6, 19, 0.9],
    ["Wheat", 407, 1.2, 27.8, 12.9, 13.8],
]

column_headings = ["Cereal", "Calories", "Fat", "Protein", "Fibre", "Vitamin E"]

output_filename = 'my_cereals.csv'

# Writing in a csv file

with open (output_filename, 'w', encoding = "utf-8", newline= '') as output_file:
    writer = csv.writer(output_file, quoting=csv.QUOTE_NONNUMERIC) # While writing 'quoting' will tell the writer to quote all the non numeric values.
    writer.writerow(column_headings) # We can use the writerow() method to write the columns in the csv file.
    writer.writerow(cereals) # This method will iterate over the items we pass to it and will create a formated row over for each one. 

