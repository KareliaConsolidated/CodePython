# Write a function called single_letter_count. This function takes in two parameters(two strings). The first parameter should be a word and the second should be a letter. The function returns the number of times that letter appears in the word. The function should be case insensitive. If the letter is not found in the word, the function should return 0.
def single_letter_count(str1,str2):
	str1 = str1.lower()
	str2 = str2.lower()
	if str2 in str1:
		return str1.count(str2)
	return 0

print(single_letter_count('Hello World', "h")) # 1
print(single_letter_count('Hello World', "O")) # 2
print(single_letter_count('Hello World', "L")) # 3