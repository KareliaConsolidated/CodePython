# Using ** as an Argument: Dictionary Unpacking
def display_name(first, second):
	print(f"{first} says hello to {second}")

names = {"first": "John", "second": "Smith"}
display_name(**names)  # John says hello to Smith
