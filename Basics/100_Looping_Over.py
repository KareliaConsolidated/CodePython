# Looping Over Dictionary
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for k,v in europe.items():
    print("the capital of "+k+" is "+v)

# the capital of germany is berlin
# the capital of poland is warsaw
# the capital of france is paris
# the capital of italy is rome
# the capital of norway is oslo
# the capital of spain is madrid
# the capital of austria is vienna
#=========================================================================#
#  The order of the printouts doesn't necessarily correspond with the order used when defining europe. Remember: dictionaries are inherently unordered!

# Looping Over Numpy Array
# If you're dealing with a 1D Numpy array, looping over all elements can be as simple as:

# for x in my_array :
#     ...

# If you're dealing with a 2D Numpy array, it's more complicated. A 2D array is built up of multiple 1D arrays. To explicitly iterate over all separate elements of a multi-dimensional array, you'll need this syntax:

# for x in np.nditer(my_array) :
#     ...
# Two Numpy arrays that you might recognize from the intro course are available in your Python session: np_height, a Numpy array containing the heights of Major League Baseball players, and np_baseball, a 2D Numpy array that contains both the heights (first column) and weights (second column) of those players.
import numpy as np
for x in np_height:
	print(str(x) + " inches")

for x in np.nditer(np_baseball):
	print(x)
	
#=========================================================================#
# Looping Over Pandas
import pandas as pd
brics = pd.read_csv('Datasets/brics.csv', index_col = 0)

for lab, row in brics.iterrows():
	print(lab + ": " + row["capital"])
	# Way_01: Less Efficient
	brics.loc[lab, "name_length"] = len(row['country'])
print(brics)

#=========================================================================#
# Way_02: 
brics["name_length"] = brics["country"].apply(len)
print(brics)

for lab, row in cars.iterrows():
	cars.loc[lab,"COUNTRY"] = row["country"].upper()
print(cars)
#=========================================================================#
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row['country'].upper()
print(cars)
#=========================================================================#
# Use .apply(str.upper)
cars['COUNTRY'] = cars['country'].apply(str.upper)
print(cars)
#=========================================================================#