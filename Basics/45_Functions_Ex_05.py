# Write a function called multiple_letter_count. This function takes in one parameter(a string) and returns a dictionary with the keys being the letters and the values being the count of the letter.
def multiple_letter_count(string):
	return {let:string.count(let) for let in string}

print(multiple_letter_count("awesome"))