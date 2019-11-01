# Function: 
# Its a Process for Executing a Task
# It can accept input and return an output
# Useful for executing similar procedures over and over.

# Why Use Functions ?
# Stay DRY - Don't Repeat Yourself!
# Clean up and prevent code duplication
# "Abstract away" code for other users

# Function Structure
def name_of_function(): # Defined
	# block of runnable code 
	pass

# First Function
def say_hi():
	print('Hi!')

say_hi()

# Returning Values from Functions
def say_hi_again():
	return 'Hi!'

greeting = say_hi_again()
print(greeting) # Hi!

# return: 
# Exists the Function
# Outputs whatever value is placed after the return keyword.
# Pops the function off of the call stack

# Functions with Parameter
# Parameters: Variables that are passed to a function - think of them as placeholders that get assigned when you call the function. 
def square(num):
	return num*num

print(square(8)) # 64
print(square(5)) # 25

# Parameters vs Arguments
# Parameter: Its a variable name in the function definition.
# When a method is called, the arguments are the data you pass into the method's parameters.
# Parameter is variable in the declaration of function.

def sum_odd_numbers(numbers):
	total = 0
	for num in numbers:
		if num % 2 != 0:
			total += num
	return total # 1 + 3 + 5 + 7 + 9 =  25
print(sum_odd_numbers(range(1,11))) # 25

def is_odd_number(num):
	if num % 2 != 0:
		return True
	return False

print(is_odd_number(4))
print(is_odd_number(9))

# Default Parameters
def exponent(num, power=2):
	return num ** power

print(exponent(2,3)) # 8 
print(exponent(2,4)) # 16

# For Default Behavior
print(exponent(2))

# Why have Default Parameters ?
# Allows you to be more defensive
# Avoids errors with incorrect parameters

# What can Default Parameters be ?
# Anything! Functions, Lists, Dictionaries, Strings, Booleans 
# Example
def add(a,b):
	return a+b

def math(a,b,fn=add):
	return fn(a,b)

def subtract(a,b):
	return a-b

print(math(2,2)) # 4

print(math(2,2,subtract)) # 0

# Keyword Arguments
def full_name(first,last):
	return f"Your name is {first} {last}"

print(full_name(first = 'John', last= 'Rambo'))
print(full_name(last= 'Rambo', first = 'John'))

# Different from Default Parameters
# When you define a function and use an = you are setting a default parameter
# When you invoke a function and use an = you are making a keyword argument

# Scoped
# Variables created in functions are scoped in that function!
def say_hello():
	instructor = 'Karelia'
	return f'Hello {instructor}'

print(say_hello())
# print(instructor) # NameError

# global
# total = 0
# def increment():
# 	total += 1
# 	return total

# print(increment()) # Error! 

# Lets us reference variables that were originally assigned on the global scope
total = 0
def increment():
	global total
	total += 1
	return total

print(increment()) # 1

# nonlocal : Lets us modify a parents variables in a child(aka nested) function
def outer():
	count = 0
	def inner():
		nonlocal count
		count += 1
		return count
	return inner()

# Documenting Functions
# Use """ """
# Essential when writing complex functions
def say_name(name):
	"""A Simple Function that returns the String Name"""
	return f"Hello {name}"

print(say_name.__doc__) # A Simple Function that returns the String Name

def count_dollar(string):
	total = 0
	for dol in string:
		if dol == "$":
			total += 1
	return f"Total Number of Dollar($) are : {total}"

print(count_dollar('Hello My Name is $olla$'))