# Set Comprehension
print({x**2 for x in range(10)}) # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

print({char.upper() for char in "HELLO"}) # {'L', 'O', 'H', 'E'}

# Function to Check if the String Contains All the Vowels
def are_all_vowels_in_string(string):
	return len({char for char in string if char in 'aeiou'}) == 5

print(are_all_vowels_in_string('Sequoia')) # True
