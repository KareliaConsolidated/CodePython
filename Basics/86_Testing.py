# Assertions
# We can make simple assertions with the assert keyword
# assert accepts an expression
# Returns None if the expression is Truthy
# Raises an AssertionError if the expression is Falsy
# Accepts an optional error message as an second argument
def add_positive_numbers(x, y):
	assert x > 0 and y > 0, "Both numbers must be positive!"
	return x + y

print(add_positive_numbers(2,3)) # 5
#  print(add_positive_numbers(2,-1)) # Assertion Error: Both numbers must be positive.

def eat_junk(food):
	assert food in ["pizza", 'Ice Cream', "Candy", "Fried Butter"], "Food Must be a Junk Food!"
	return f"NOM NOM NOM I am eating {food}"

food = input("ENTER A FOOD PLEASE: ")
print(eat_junk(food))

# Assertions Warning
# If a Python file is run with the -O flag, assertions will not be evaluated!