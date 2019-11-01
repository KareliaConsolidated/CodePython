# Write a function called intersection. This function should accepts two lists and return a list with the values that are in both input lists.
# Sets Solution
def intersection(li1,li2):
	si1 = set(li1)
	si2 = set(li2)
	return list(si1 & si2)

print(intersection([1,2,3],[2,3,4])) # [2, 3]

# List Comprehension Solution
def intersection_li(li1,li2):
	return [val for val in li1 if val in li2]

print(intersection_li([1,2,3],[2,3,4])) # [2, 3]

# Looping Solution
def intersection_loop(li1,li2):
	in_common = []
	for val in li1:
		if val in li2:
			in_common.append(val)
	return in_common

print(intersection_loop([1,2,3],[2,3,4])) # [2, 3]