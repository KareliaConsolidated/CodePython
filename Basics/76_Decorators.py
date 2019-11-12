# Higher Order Functions
# We can pass functions as args to other functions
def sum(n, func):
	total = 0
	for i in range(n):
		total += func(n)
	return total

def square(x):
	return x*x

def cube(x):
	return x ** 3

print(sum(3, square))


from random import choice
def greet(person):
	def get_mood():
		msg = choice(('Hello there ', 'Go away ', 'I love you '))
		return msg

	result = get_mood() + person
	return result

print(greet("John"))

# Introduction to Decorators
# Decorators are functions
# Decorators wrap other functions and enhance their behavior
# Decorators are examples of higher order functions
# Decorators have their own syntax, using "@"(syntactic sugar)

# Decorators as Functions
def be_polite(fn):
	def wrapper():
		print("What a pleasure to meet you!")
		fn()
		print("Have a great day!")
	return wrapper

@be_polite
def greet():
	print("My name is John.")

greet()
greet()
# greet = be_polite(greet)

# Decorators with different signatures
def shout(fn):
	def wrapper(*args, **kwargs):
		return fn(*args, **kwargs).upper()
	return wrapper

@shout
def greet(name):
	return f"Hi, I'm {name}."

@shout
def order(main, side):
	return f"Hi, I'd like the {main}, with a side of {side}, please !"

print(greet("johny"))
print(order("burger", "fries"))