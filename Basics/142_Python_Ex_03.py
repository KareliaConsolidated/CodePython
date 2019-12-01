# Find Factors
# Write a function called find_factors which accepts a number and returns a list of all numbers which are divisible by starting from 1 and going up to the number.
######### Way 01 #########
def find_factors(num):
	factors = []
	for i in range(1, num+1):
		if num % i == 0:
			factors.append(i)
	return factors

print(find_factors(10)) # [1, 2, 5, 10]

######### Way 02 #########
def find_factors(num):
	i = 1
	while (i<=num):
		if(num % i == 0):
			factors.append(i)
		i += 1
	return factors
print(find_factors(10)) # [1, 2, 5, 10]
