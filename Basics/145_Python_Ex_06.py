# Truncate
# Write a function called truncate that will shorten a string to a specified length, and add "..." to the end. Given a string and number n, truncate the string to a shorter string containing at most n characters. For Example truncate("long string", 5) should return a 5 character truncated version of "long string". If the string gets truncated, the truncated return string should have a "..." at the end. Because of this, the smallest number passed in as a second argument should be 3.

def truncate(string, trunc):
	if trunc < 3:
		return 'Truncation must be at least 3 characters'
	if (trunc > len(string) + 2):
		return string
	return string[:trunc-3] + "..."

print(truncate("Hello World", 6)) # 'Hel...'
print(truncate("Woah", 4)) # 'Wel...'
print(truncate("Woah", 3)) # '...'
print(truncate("Problem Solving is the Best", 10)) # Problem...
print(truncate("Super Cool", 2)) # Truncation must be atleast 3 characters.