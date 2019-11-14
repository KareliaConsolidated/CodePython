# Pandas
# High Level Data Manipulation Tool
# It is built on Numpy Package
import pandas as pd
brics = pd.read_csv("Datasets/brics.csv", index_col = 0)
print(brics)

# Dictionary to DataFrame
# Pandas is an open source library, providing high-performance, easy-to-use data structures and data analysis tools for Python. Sounds promising!

# The DataFrame is one of Pandas' most important data structures. It's basically a way to store tabular data where you can label the rows and the columns. One way to build a DataFrame is from a dictionary.

# In the exercises that follow you will be working with vehicle data from different countries. Each observation corresponds to a country and the columns give information about the number of vehicles per capita, whether people drive left or right, and so on.

# Three lists are defined in the script:

# names, containing the country names for which data is available.
# dr, a list with booleans that tells whether people drive left or right in the corresponding country.
# cpc, the number of motor vehicles per 1000 people in the corresponding country.
# Each dictionary key is a column label and each value is a list which contains the column elements.

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

# Have you noticed that the row labels (i.e. the labels for the different observations) were automatically set to integers from 0 up to 6?

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

# Importing cars.csv to DataFrame

# Fix import by including index_col
cars = pd.read_csv('Datasets/cars.csv', index_col = 0)

# Print out cars
print(cars)