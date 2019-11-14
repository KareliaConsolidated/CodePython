# Square Brackets
	# Column Access : brics[["country","capital"]]
	# Row Access: Only Through Slicing : brics[1:4]

# loc (label-based)
	# Row-Access : brics.loc[["RU", "IN", "CH"]]
	# Column-Access : brics.loc[:,["country", "capital"]]
	# Row & Column Access : brics.loc[["RU", "IN", "CH"], ["country", "capital"]]

# brics.iloc[[1, 2, 3], [0, 1]]

# Import cars data
import pandas as pd
cars = pd.read_csv('Datasets/cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

# loc and iloc
# With loc and iloc you can do practically any data selection operation on DataFrames you can think of. loc is label-based, which means that you have to specify rows and columns based on their row and column labels. iloc is integer index based, so you have to specify rows and columns by their integer index.

# Print out observation for Japan
print(cars.loc['JPN'])

# Print out observations for Australia and Egypt
print(cars.iloc[[1, 6]])

# Print out drives_right value of Morocco
print(cars.loc[['MOR'],['drives_right']])

# Print sub-DataFrame
print(cars.loc[['RU','MOR'], ['country', 'drives_right']])

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap','drives_right']])