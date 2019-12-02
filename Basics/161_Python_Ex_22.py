# Three Odd Numbers
# Write a function called three_odd_numbers, which accepts a list of numbers and returns True if any three consecutive numbers sum to an odd number

def three_odd_numbers(arr):
	i = 0
	while i < len(arr) - 2:
		total = 0 
		for j in range(i, i+3):
			total += arr[j]
		if total % 2 != 0:
			return True
		i += 1
	return False

print(three_odd_numbers([1,2,3,4,5])) # True
print(three_odd_numbers([0,-2,4,1,9,12,4,1,0])) # True
print(three_odd_numbers([5,2,1])) # False
print(three_odd_numbers([1,2,3,3,2])) # False