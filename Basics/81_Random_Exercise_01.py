# TODO: Define a control structure that finds the smallest positive
# number in in_list and returns the correct smallest number.
def smallest_positive(li):
	smallest_positive = None
	for num in li:
		if num > 0 :
			if smallest_positive == None or num < smallest_positive:
				smallest_positive = num
	return smallest_positive

print(smallest_positive([4, -6, 7, 2, -4, 10])) # 2
