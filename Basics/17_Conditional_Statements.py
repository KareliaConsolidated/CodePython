# Conditional logic using if statements represents different paths a program can take based on some type of comparison of input.
name = "Johny Stark"

if name == "Johny Stark":
	print("Hello, " +name)
elif name == "John Fernandes":
	print("You are not authorized !" +name)
else:
	print("Calling Police Now !")

# In Python, all conditional checks resolve to True or False
x = 1
x is 1 # True
x is 0 # False

# We can call values that will resolve to True "truthy", or values that will resolve to False "falsy".

# Besides False conditional checks, other things that are naturally falsy include: empty objects, empty strings, None, and Zero.

# is vs "=="
# In Python, "==" and "is" are very similar comparators, however they are not the same.
a = 1  
a == 1 # True
a is 1 # True

a = [1,2,3] # A List of Numbers
b = [1,2,3]
a == b # True # Checking, if values are the same.
a is b # False # Checking, if values are stored in the same place in memory.

# "is" is only truthy, if the variables reference the same item in memory.