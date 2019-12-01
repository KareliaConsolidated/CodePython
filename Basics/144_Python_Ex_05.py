# repeat
# Write a function called repeat, which accepts a string and a number and returns a new string with the string passed to the function repeated the number amount of times. Do not use the built in repeat method.
def repeat(strg,num):
	return strg * num

print(repeat('*', 3)) # ***
print(repeat('abc', 2)) # abcabc
print(repeat('abc', 0)) # 