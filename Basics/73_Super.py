class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"This animal says {sound}")

class Cat(Animal):
	def __init__(self, name, species, breed, toy):
		super().__init__(name, species)
		# Animal.__init__(self, name, species)
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")

blue = Cat("Blue", "Cat", "Scottish Fold", "String")
print(blue)
print(blue.species)
print(blue.breed)
print(blue.toy)
blue.play()

# MRO (Method Resolution Order)
# Whenever you create a class, Python sets a Method Resolution Order, or MRO for that class, which is the order in which Python will look for methods on instances of that class.
# You can programmatically reference the MRO three ways:
	# __mro__ attribute on the class
	# Use the mro() method on the class
	# Use the builtin help(cls) method
print(Cat.__mro__)