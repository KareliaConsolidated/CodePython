# Two List Dictionary
# Write a function two_list_dictionary which accepts two lists of varying lengths. The first list consists of keys and the second one consists of values. Your function should return a dictionary created from the keys and values. If there are enough values, the remaining keys should have a value of null. If there are not enough keys, just ignore the remaining values.
def two_list_dictionary(keys, values):
	collection = {}

	for idx, val in enumerate(keys):
		if idx < len(values):
			collection[keys[idx]] = values[idx]
		else:
			collection[keys[idx]] = None

	return collection

print(two_list_dictionary(['a','b','c','d'], [1,2,3]))
print(two_list_dictionary(['a','b','c'], [1,2,3,4]))
print(two_list_dictionary(['x','y','z'], [1,2]))