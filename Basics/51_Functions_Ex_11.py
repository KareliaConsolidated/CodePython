# Write a function called compact. This function accepts a list and returns a list of values that are truthy values, without any of the falsey values
def compact(li):
	return [l for l in li if l]

# With List Comprehension
print(compact([0, 1, 2, "", [], False, {}, None, "All done"])) # [1, 2, 'All done']

# Without List Comprehension
def compact_li(li):
	truthy = []
	for val in li:
		if val:
			truthy.append(val)
	return truthy

print(compact_li([0, 1, 2, "", [], False, {}, None, "All done"])) # [1, 2, 'All done']