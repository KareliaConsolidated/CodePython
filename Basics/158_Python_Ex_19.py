# Vowel Count
# Write a function called vowel_count that accepts a string and returns a dictionary with the keys as the vowels and values as the count of times that vowel appears in the string.
def vowel_count(string):
	lower_string = string.lower()
	return {letter:lower_string.count(letter) for letter in lower_string if letter in 'aeiou'} 

print(vowel_count('awesome')) # {'a': 1, 'e': 2, 'o': 1}