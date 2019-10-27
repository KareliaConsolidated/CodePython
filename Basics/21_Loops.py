# In Python, for loops are written like this:
for item in iterable_object:
	# do something with item

# An iterable object is some kind of collection of items, for instance; a list of numbers, a string of characters, a range etc.

# item is a new variable that can be called whatever you want

# item references the current position of our iterator within the iterable. It will iterate over(run through) every item of the collection  and then go away when it has visited all items.
for num in range(1,8):
	print(num)

for letter in "coffee":
	print(f"{letter}" * 10)

# A Range is just a slice of the number line.