# Define a class called Vehicle. It should be completely empty (just add a pass statement inside). After the class is defined, create two instances of Vehicle. Save one to a variable called car and another to a variable called boat.
class Vehicle:
	pass
 
# Instantiate a new Vehicle and save it to a variable called car and boat.
car = Vehicle()
boat = Vehicle()

# Suppose we're creating a social network application where users can comment on posts and photos. Create a class called Comment. Each comment have the following attributes::
# username - the username of the person who created the comment
# text - the actual comment itself.
# likes - the number of likes the comment has. Likes should default to 0.

class Comment:
	def __init__(self, username, text, likes = 0):
		self.username = username
		self.text = text
		self.likes = likes

another_comment = Comment("rose67", "So Cute!", 4)
comment_without_like = Comment("aka67", "So Cute!")

print(another_comment.username) # rose67
print(another_comment.likes) # 4
print(comment_without_like.likes) # 0


class BankAccount:
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

acct = BankAccount("Jackal")
print(acct.getBalance()) # 0.0
print(acct.deposit(10)) # 10.0
print(acct.withdraw(1)) # 9.0


class Chicken:
	total_eggs = 0

	def __init__(self, name, species):
		self.name = name
		self.species = species
		self.eggs = 0

	def lay_egg(self, eggs = 1):
		self.eggs += eggs
		Chicken.total_eggs += eggs
		return self.eggs
c1 = Chicken(name="Alice", species="Partridge Silkie")
c2 = Chicken(name="Amelia", species="Speckled Sussex")
print(f"Chicken Eggs: {Chicken.total_eggs}")
c1.lay_egg(3)
print(f"Chicken Eggs: {Chicken.total_eggs}")
c1.lay_egg()
print(f"Chicken Eggs: {Chicken.total_eggs}")

# What is the difference betweeen a class and an instance ?
# A class is a blueprint for constructing objects; an instance is an object constructed from the class definition.

# Encapsulation
# Encapsulation is the process of designing a programmatic class using public and private methods and attributes to implement abstraction.

# Abstraction
# The idea of exposing only "relevant" data in a class interface, hiding private attribute and methods (aka the inner workings) from users.