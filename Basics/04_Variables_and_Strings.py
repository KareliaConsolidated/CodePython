##### Introduction to Variables #####

# Variables are like Containers. Store Some Data, Pull it Out Later. They can hold all sorts of things like numbers, booleans and strings.

# Variables are always assigned with the variable name on the left and the value on the right of the equals sign.

# Variables must be assigned before they can be used.

number_of_dragons = 99 

print(number_of_dragons) #99

print(number_of_dragons * 2) #198

#### Variable Assignment #####
# Variables can be assigned to other variables.
# It can be reassigned at any time.

Count_Dragons = number_of_dragons

print(Count_Dragons) #99

Count_Dragons = 1337

print(Count_Dragons) #1337

all, at, once = 5, 10, 15 # Multiple Assignment

print(all) #5
print(at) #10
print(once) #15

Count_Dragons = Count_Dragons - 1
print(Count_Dragons) #1336

#### Naming Restrictions ####
# In Python, you can name your variables whatever you want with some restrictions:
# 1. Variables must start with a letter or underscore. Ex: _Dragons(Good), 2Dragons(Not Good)
# 2. The rest of the name must consist of letters, numbers, or underscores. Ex: Dragons2(Good), hey@you(Not Good)
# 3. Names are Case-Sensitive. Ex: CATS != Cats, Cats != cats

#### Naming Conventions ####
# Most variables should be snake_case(underscores between words).
# Most variables should also be lowercase with some exceptions: CAPITAL_SNAKE_CASE usually refers to constants (Ex: PI = 3.14)
# UpperCamelCase usually refers to a class
# Variables that start and end with two underscores (called "dunder" for double underscore) are supposed to be private or left alone.(__no_touchy__)

#### Dynamic Typing ####
# Python is highly flexible about reassigning variables to different types:
active = True
print(active) # True

active = "Dragon"
print(active) # Dragon

active = None
print(active) # None

active = 100/10
print(active)

#### String Concatenation ####
# Concatenation is combining multiple strings together.
str_one = "Blue"
str_two = "Dragon"
str_three = str_one + " " + str_two 
print(str_three) #Blue Dragon
print("Hello there and welcome to the game, "+str_three)

name = "A"
name += " Karelia"
print(name) # A Karelia

print("a" + "b" + "c") #abc

# print(8 + "hello") # Error: Unsupported Operand Type

#### Formatting Strings ####
# There are also several ways to format strings in Python to interpolate variables.

print(f"{8} hello") # F-Strings

#### Strings and Indexes ####
print("lol"[2]) # Starts with 0, this will return l.
print("lol"[-1]) # -1 Means Starts with End, will return l

#### Converting Data Types ####
decimal = 12.56345
integer = int(decimal)
print(integer) # 12

my_list = [1,2,3]
print(str(my_list)) # "[1,2,3]"

num = 12
print(type(num)) # Int

print(type(float(num))) # float

print(type(str(8))) # str

print(str(8)) # '8'