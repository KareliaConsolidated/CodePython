# Letter Counter
# Write a function called letter_counter which accepts a string and returns a function. When the inner function is invoked it should accepts a parameter which is a letter, and the inner function should return the number of times that letter appears. This inner function should be case insensitive.
def letter_counter(string):
	def inner(para):
		return len(list(c.lower() for c in string.lower() if c == para)) 
	return inner

counter = letter_counter('Amazing')
print(counter('a')) # 2