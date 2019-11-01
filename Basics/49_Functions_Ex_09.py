# Write a function called multiply_even_numbers. This function accepts a list of numbers and returns the product all even numbers in the list.
def multiply_even_numbers(li):
	total = 1
	for num in li:
		if num % 2 == 0:
			total *= num
	return total


print(multiply_even_numbers([1,2,3,4,5,6,7,8,9,10])) # 3840
