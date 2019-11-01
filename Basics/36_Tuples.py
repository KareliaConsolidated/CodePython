# Tuple: Ordered Collection or Grouping of Items!
numbers = (1, 2, 3, 4) # It is immutable !
print(3 in numbers) # True
# numbers[0] = 'Change Me!' # TypeError
# Tuples are faster than lists
# .items() returns list of tuples!
months = ("Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec")
# Creating / Accessing
# Create using () or the tuple function
print(numbers[1]) # 2
print(months[2]) # Mar

# Tuples can be used as a Keys in Dictionaries:
locations = {
	(35.685, 39.6917): "Tokyo Office",
	(40.7128, 74.0060): "New York Office",
	(37.7749, 122.4194): "San Francisco Office"
}

print(locations[(37.7749, 122.4194)]) # San Francisco Office

# Some Dictionary Methods Like .items() return Tuples
locations = {"name":"San Francisco Office", "country":"US"}
print(locations.items()) # dict_items([('name', 'San Francisco Office'), ('country', 'US')])
													# tuple ^				  # tuple ^            

# Looping
# We can use a for loop to iterate over a tuple just like a list !
for mon in months:
	print(mon)

# Using While Loop Dec to Jan
i = len(months) - 1
while (i >= 0):
	print(months[i])
	i -= 1

# Tuple Methods
# Count: Returns the number of times a value appears in a tuple
x = (1,2,3,3,3,3)
print(x.count(1)) # 1
print(x.count(3)) # 4

# Index: Returns the index at which a value is found in a tuple
print(x.index(1)) # 0
print(x.index(5)) # IndexError
print(x.index(3)) # 2 - Only the First Matching Index is Returned!
