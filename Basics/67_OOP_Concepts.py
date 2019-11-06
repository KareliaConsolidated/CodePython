# What is OOP?
# Object Oriented Programming is a method of programming that attempts to model some process or thing in the world as a class or object.

# Class - A blueprint for objects. Classes can contain methods(functions) and attributes(similar to keys in a dict)

# Instance - Objects that are constructed from a class blueprint that contains their class's methods and properties.

# Why OOP?
# With OOP, the goal is to encapsulate your code into logical, hierarchical groupings using classes so that you can reason about your code at a higher level.

# Encapsulation
# The grouping of public and private attributes and methods into a programmatic class, making abstraction possible.

# Example:
# Designing the Deck class, I make cards a private attribute (a list).
# I decide that the length of the cards should be accessed via a public method called count() -- i.e. Deck.count()

# Abstraction
# Exposing only "relevant" data in a class interface, hiding private attributes and methods (aka the "inner workings") from users.

# Example:
# Hide the inner workings, and expose what's needed

# CREATING CLASSES AND INSTANCES
# class User:
# 	pass

# user1 = User() # Instance 1
# user2 = User() # Instance 2
# print(user1) # Store at different memory location
# print(user2) # Store at different memory location

# The __init__ method
# Classes in Python can have a special __init__ method, which gets called everytime you create an instance of the class(instantiate).
class User:
	def __init__(self, first,last,age):
		self.first = first
		self.last = last
		self.age = age

user1 = User("Francesca","Smokes", 56)
user2 = User("Maria","Smokes", 34)
user3 = User("Arundhati","Smokes", 67)

print(user1.first, user1.last, user1.age)

# Instantiating a Class
# Creating an object that is an instance of a class is called instantiating a class.
v = Vehicle("Honda", "Civic", 2017)
# In this case, v becomes a Honda Civic, a new instance of Vehicle.

# The self keyword refers to the current class instance. 
# self must always be the first parameter to __init__ and any methods and properties on class instances.

# _name # Just a way of convention, that it suppose to be private variable.
# __name # Name Mangling: can be seen by print(dir(p))
# __name__ (Dunder Method) # Used for Python Specific Methods

class Person:
	def __init__(self) :
		self.name = "Tony"
		self._secret = "Hi!"
		self.__msg = "I like turtles!"

p = Person()
print(p.name)
print(p._secret)
print(dir(p))
print(p._Person__msg)

# Instance Attributes and Methods
# A User class with 3 instance attributes but no instance methods (aside from __init__)
class User:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

user1 = User("John","Smith", 46)
user2 = User("Jo","Smith", 41)
print(user1.full_name())
user1.likes("Ice Cream")