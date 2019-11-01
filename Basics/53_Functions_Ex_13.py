# Write a function called partition. This function accepts a list and a callback function(which you can assume return True or False)
# This function should iterate over each element in the list and invoke the callback function at each iteration.
# If the result of the callback function is True, the element should go into the first list(i.e. the "truthy list")
# If the result of the callback function is False, the elemet should go into the second list(i.e. the "falsy" list)
# When its finished, partition should return both lists inside of one larger list, like so: [truthy_list, falsy_list]

# Loop Solution
def is_even(num):
	return num % 2 == 0

def partition(li,fn):
	truthy = []
	falsy = []
	for val in li:
		if fn(val):
			truthy.append(val)
		else:
			falsy.append(val)
	return [truthy,falsy]

print(partition([1,2,3,4], is_even)) # [[2, 4], [1, 3]]

# List Comprehension Solution
def partition_list(lst,fn):
	return [[val for val in lst if fn(val)],[val for val in lst if not fn(val)]]

print(partition_list([1,2,3,4], is_even)) # [[2, 4], [1, 3]]