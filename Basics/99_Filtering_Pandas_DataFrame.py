# Import cars data
import pandas as pd
cars = pd.read_csv('Datasets/cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars.loc[:,'drives_right']

# Use dr to subset cars: sel
sel = cars[dr]
# sel = cars[cars['drives_right']]

# Print sel
print(sel)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars.loc[:,'cars_per_cap'] > 500

# Print car_maniac
print(cars[cpc])

# Cars per capita

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(medium)