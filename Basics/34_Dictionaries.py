# Dictionaries: A Data Structure that Consists of Key-Value Pairs.
# We use the keys to describe our data and the values to represent the data.

course = {
	"name":"Python",
	"duration":5,
	"editor":"Sublime"
}

# Keys and Values separated by a colon; Our Keys are almost always numbers or strings.

# Another Way: Another Approach is to use the "dict" function. You assign values to keys by passing in keys and values separated by an =
# another_dict = dict(key = 'value')
# another_dict = {'key' : 'value'}

# Accessing Individual Values
print(course["name"]) # Python
print(course["editor"]) # Sublime
# course["area"] # KeyError

# Let's get all the Values !
# Accessing All Values in a Dictionary
# Use ".values()"
for value in course.values():
	print(value)

# Accessing All Keys in a Dictionary
# Use ".keys()"
for key in course.keys():
	print(key)

# Accessing All Keys and Values:
# Use ".items()"
# dict.items() returns a list of tuples.
for k,v in course.items():
	print(f"{k}: {v}")

# Using "In" with Dictionaries (Only Checking Keys)
print("name" in course) # True
print("awesome" in course) # False

# To Check in Values
print("Sublime" in course.values()) # True

# Dictionary Methods
# Clear: Clears all the keys and values in a dictionary:
d = dict(a=1, b=2, c=3)
print(d)
d.clear()
print(d)

# Copy: Makes a copy of a dictionary
clone = d.copy()
print(clone == d) # True
print(clone is d) # False

# fromkeys: Creates Key-Value pairs from comma separated values:
# First Paramter Should be an Iterable
print({}.fromkeys("a","b")) # {'a': 'b'}
print({}.fromkeys(['email'],'unknown')) # {'email': 'unknown'}

new_user = {}.fromkeys(['Name', 'Score', 'Email', 'Profile Bio'], 'Unknown')
print(new_user)

# get: Retrieves a key in an object and return None instead of a KeyError if the key does not exist:
d = dict(a=1, b=2, c=3)
d['a'] # 1
d.get('a') # 1
# d['no_key'] # KeyError
d.get('no_key') # None

# Given the provided dictionary of donations:
donations = dict(sam = 25.0, lena = 88.99, chuck = 13.0, linus = 99.5, stan = 150.0, lisa = 50.25, harrison = 10.0)
# Using Loop, Version 01
total = 0
for s in donations.values():
	total+=s
print(total)

# Version 02
print(sum(donations.values()))


# pop: Takes a single argument corresponding to a key and removes that key-value pair from the dictionary. Returns the value corresponding to the key that was removed.
d = dict(a=1, b=2, c=3)
# d.pop() # TypeError: pop expected at least 1 arguments, got 0
d.pop('a') # 1
print(d) # {'c': 3, 'b': 2}
# d.pop('e') # KeyError


# popitem: Removes a random key in a dictionary:
d = dict(a=1, b=2, c=3)
print(d.popitem()) # ('c', 3)

# update: Update Keys and Values in a Dictionary with another set of key value pairs
first = dict(a=1, b=2, c=3, d=4, e=5)
second = {}
second.update(first)
print(second) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
second['a'] = "Amazing" 
print(second) # {'a': 'Amazing', 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Bakery Exercise
# This code picks a random food item:
from random import choice

food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])

bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

if food in bakery_stock:
	print(food)
	print(f"{bakery_stock[food]} left")
else:
	print("We don't make that !")

# FromKeys Exercise
game_properties = [
    "current_score",
    "high_score",
    "number_of_lives",
    "items_in_inventory",
    "power_ups",
    "ammo",
    "enemies_on_screen",
    "enemy_kills",
    "enemy_kill_streaks",
    "minutes_played",
    "notifications",
    "achievements"
]

initial_game_state = dict.fromkeys(game_properties, 0)
print(initial_game_state)