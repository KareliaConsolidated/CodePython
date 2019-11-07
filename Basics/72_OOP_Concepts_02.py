# Inheritance
# A Key feature of OOP is the ability to define a class which inherits from another class(a "base" or "parent" class).
# In Python, Inheritance works by passing the class as an argument to the definition of a child class.
class Animal:
	def make_sound(self, sound):
		print(sound)

class Cat(Animal):
	pass

gandalf = Cat()
gandalf.make_sound("meow") # meow

print(isinstance(gandalf, Cat))  # True
print(isinstance(gandalf, Animal))  # True

# Properties
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		if age >= 0:
			self._age = age
		else:
			self._age = 0

	@property # getter
	def age(self):
		return self._age

	@age.setter
	def age(self, value):
		if value >= 0:
			self._age = value
		else:
			raise ValueError("Age Can't be Negative!")

	@property
	def full_name(self):
		return f"{self.first} {self.last}"

	@full_name.setter
	def full_name(self, name):
		self.first, self.last = name.split(" ")
			

jane = Human("Jane", "Godwin", 50)
print(jane.age) # 50
jane.age = 20
print(jane.age) # 20
jane.full_name = "Tim Jopling"
print(jane.full_name)

# Polymorphism
# A key principle in OOP is the idea of polymorphism - an object can take on many(poly) forms(morph).
# While a formal definition of polymorphism is more dificult, here are two important practical applications:
	# 1. The same class method works in a similar way for different classes.
	# Ex: Cat.speak() # meow, Dog.speak() # woof, Human.speak() # yo

	# 2. The same operation works for different kinds of objects
	# sample_list = [1,2,3], sample_tuple = (1,2,3), sample_string = "awesome" , len(sample_list), len(sample_tuple), len(sample_string)

# Polymorphism & Inheritance
	# 1. The same class method works in a similar way for different classes.
	# A common implementation of this is to have a method in a base (or parent) class that is overridden by a subclass. This is called method overriding.
	# Each subclass will have a different implementation of the method.
class Animal():
	def speak(self):
		raise NotImplementedError("Subclass needs to implement this method")

class Dog(Animal):
	def speak(self):
		return "woof"

class Cat(Animal):
	def speak(self):
		return "meow"
# Special Methods
# 2. The same operation works for different kinds of objects.
8 + 2 = 10
"8" + "2" = 82

# Special Methods

# The + operator is shorthand for a special method called __add__() that gets called on the first operand.
# If the first(left) operand is an instance of int, __add__() does mathematical addition. If it's string , it does string concatenation.

# Special Methods Applied
# Therefore, you can declare special methods on your own classes to mimic the behavior of builtin objects, like so using __len__:
class Human:
	def __init__(self, height):
		self.height = height # in inches

	def __len__(self):
		return self.height

Cruise = Human(60)
len(Cruise) # 60
