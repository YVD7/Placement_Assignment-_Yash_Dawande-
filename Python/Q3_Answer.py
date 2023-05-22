# Question 3: -
# Write a program, which would download the data from the provided link, and then read the data and convert
# that into properly structured data and return it in Excel format.

# importing libraries
import numpy as np
import pandas as pd
import requests

# reading path variable
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"

# create download function for downloading the dataset
def download_data(url):
    response = requests.get(url)
    return response.text

# create function for processing the data
def process_data(data):

    # Process the data as needed
    # Replace this with your own logic to structure the data properly
    
    # Example: Splitting the data by lines
    lines = data.split('\n')

    # Example: Spliting each line by commas to form a table
    table = [line.split(',') for line in lines]

    return table
    # for header in data:
    #     for sample in header:
            

# creating the function to export data 
def export_to_excel(data, output_file):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)

#output file
output = 'output.xlsx'

# Download the data
data = download_data(url)

# Process the data
processed_data = process_data(data)

# Export to Excel
export_to_excel(processed_data, output_file='output.xlsx')
    



    