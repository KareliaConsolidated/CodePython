# Write a function called number_compare. This function takes in two parameters(both numbers). If the first is greater than the second, this function returns "First is greater" If the second number is greater than the first, the function returns "Second is greater."Otherwise the function returns "Numbers are equal"
def number_compare(a,b):
	if a>b:
		return "First is Greater"
	elif b>a:
		return "Second is Greater"
	return "Numbers are equal"

print(number_compare(1,1))  # Numbers are equal
print(number_compare(2,1))  # First is Greater
print(number_compare(1,2))  # Second is Greater