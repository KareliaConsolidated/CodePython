# Valid Parentheses
# Write a function called valid_parentheses that takes a string of parentheses, and determines if the order of the parentheses is valid. valid_parentheses should return True if the string is valid, and False if its invalid.
def valid_parentheses(parens):
	count = 0
	i = 0
	while i < len(parens):
		if (parens[i] == '('):
			count += 1
		if (parens[i] == ')'):
			count -= 1
		if (count < 0):
			return False
		i += 1
	return count == 0

print(valid_parentheses("()")) # True
print(valid_parentheses(")(()))")) # False
print(valid_parentheses("(")) # False
print(valid_parentheses("(())()")) # True
print(valid_parentheses("))((")) # False
print(valid_parentheses("())(")) # False
print(valid_parentheses("(()()()())()(")) # False