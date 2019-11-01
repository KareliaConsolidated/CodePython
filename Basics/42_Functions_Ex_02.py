# Write a function called last_element. This function takes in one parameter (a list) and returns the last value in the list. It should return None if the list is empty.
def last_element(l):
	if len(l)>0:
		return l[-1]
	return None

print(last_element([1,2,3,4]))