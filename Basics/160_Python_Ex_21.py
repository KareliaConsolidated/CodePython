# Write a function called reverse_vowels. This function should reverse the vowels in a string. Any characters which are not vowels should remain in their original position. You should not consider "y" to be vowel.
def reverse_vowels(s):
	vowels = 'aeiou'
	string = list(s)
	i, j = 0, len(s) - 1
	while i < j:
		if string[i].lower() not in vowels:
			i += 1
		elif string[j].lower() not in vowels:
			j -= 1
		else:
			string[i], string[j] = string[j], string[i]
			i += 1
			j -= 1
		return "".join(string)

print(reverse_vowels('Hello!')) # Hello!
print(reverse_vowels('Tomatoes!')) # Tomatoes!
print(reverse_vowels('Reverse Vowels In A String!')) # Reverse Vowels In A String!
print(reverse_vowels('aeiou'))  # ueioa
print(reverse_vowels('why try, shy fly?')) # why try, shy fly?