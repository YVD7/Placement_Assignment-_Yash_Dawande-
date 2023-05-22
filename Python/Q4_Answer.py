# Question 4 -
# Write a program to download the data from the link given below and then read the data and convert the into
# the proper structure and return it as a CSV file.
# Link - https://data.nasa.gov/resource/y77d-th95.json
# Note - Write code comments wherever needed for code understanding.

# importing libraries
import numpy as np
import pandas as pd
import requests
import os
import json

# store the url link into url variable
url = "https://data.nasa.gov/resource/y77d-th95.json"

# download json file and save 
response = requests.get(url)

download = response.text

with open('data.json', 'w') as json_file:
    json.dump(download,json_file)

# Now load the data file
open = open('data.json')

load = json.load(open)

print(load)

# now save the file into csv format
df = pd.read_json(load).to_csv('data.csv')
print(df)



