# Introducing Class Attributes
# We can also define attributes directly on a class that are shared by all instances of a class and the class itself.
class Pet():
	allowed = ("cat", "dog", "bird", "lizard", "rodent")

	def __init__(self, kind, name):
		if kind not in self.allowed:
			raise ValueError(f"You can't have a {kind} as a pet here!")

		self.kind = kind
		self.name = name

fluffy = Pet("cat", "Fluffy")
fluffy.allowed # ("cat", "dog", "bird", "lizard", "rodent")
Bro = Pet("bear", "Bro") # ValueError: You can't have a bear as a pet here!
