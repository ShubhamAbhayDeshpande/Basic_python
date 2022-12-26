"""
This file will create a json file from the data about the global temperatures that was downloaded from the internet. """

# standard import
import json
import urllib.request # For reading the data directly form the url. 

# the lines below will read and decode the json file downloaded from the internet. 
json_data_source = "temperature.json"
with open (json_data_source, 'r', encoding='utf-8') as json_data:
    anomolies = json.load(json_data)

# Printing the description of the file.
print(anomolies['description'])

# Print the title of the dataset from the descriotion.
print("The title of the report is: ", anomolies["description"]["title"])

print('*' * 100) # this line is just for show.

# Print the temperature for each year in the dataset.
for year, temp in anomolies['data'].items():
    year, temp = int(year), float(temp)
    print(f"{year}--------{temp}")

print("*" * 100) # this line is just for the show.

# We can do the same thing by downloading the data directly from the internet. The example is as shown below. 

# Read the data directly from the URL.
json_data_onlne = "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/10/1880-2022.json"

with urllib.request.urlopen(json_data_onlne) as online_data:
    data = online_data.read().decode("utf-8")
    anomolies_2 = json.load(online_data)

#similar to how the 'with' will close the file after we have read it, similarly, it will also close the url.

# Printing the description of the file.
print(data['description'])

# Print the title of the dataset from the descriotion.
print("The title of the report is: ", data["description"]["title"])

print('*' * 100) # this line is just for show.

# Print the temperature for each year in the dataset.
for year1, temp1 in data['data'].items():
    year1, temp1 = int(year1), float(temp1)
    print(f"{year1}--------{temp1}")