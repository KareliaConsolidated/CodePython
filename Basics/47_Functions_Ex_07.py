# Write a Function is_palindrome. A palindrome is a word, phrase, number or other sequence of characters which reads the same backward or forward. This function should take in one parameter and returns True or False depending on whether it is a palindrome. As a bonus, allow your function to ignore whitespace and capitalization.
# Way_01
# Here's the simpler version that doesn't ignore whitespace.  I reverse the string using a slice [::-1] and compare that to the original string, which returns True or False.  
def is_palindrome_v_01(string):
	return string == string[::-1]

# Way_02
# For the more advanced version that ignores whitespace, I first remove all whitespace from the input string using a string method called replace() . What I'm actually doing is replacing all spaces(" ") with empty strings ("").  I save the result to a new variable I call stripped .  Then, I simple check if stripped  is a palindrome, using the same logic I did in the previous solution.
def is_palindrome_v_02(string):
	stripped = string.replace(" ","")
	return stripped == stripped[::-1]

print(is_palindrome_v_01('testing')) # False
print(is_palindrome_v_02('testing')) # False
print(is_palindrome_v_01('hannah')) # True
print(is_palindrome_v_02('hannah')) # True
print(is_palindrome_v_02('tacocat')) # True