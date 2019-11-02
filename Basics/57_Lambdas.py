# Lambdas
# Function that has no name. (Anonymous Function)
def square(num): return num * num

square2 = lambda num: num * num
print(square2(7)) # 49
print(square.__name__) # square
print(square2.__name__) # lambda

# map: A Standard function that accepts at least two arguments, a function and an "iterable".
# Iterable: Something that can be iterated over(lists, strings, dictionaries, sets, tuples)
# Runs the lambda for each value in the iterable and returns a map object which can be converted into another data structure.
# map in Action
l = [1,2,3,4]
doubles = list(map(lambda x: x*2,l))
print(doubles) # [2, 4, 6, 8]

names = [
{'first':'Arnold','last':'Smith'},
{'first':'Blue','last':'Smith'},
{'first':'Colt','last':'Smith'}
]

first_names = list(map(lambda x:x['first'],names))
print(first_names)  # ['Arnold', 'Blue', 'Colt']

# filter: There is a lambda for each value in the iterable.
# Returns filter object which can be converted into other iterables.
# The object contains only the values that return true to the lambda.
evens = list(filter(lambda x: x % 2 == 0, l))
print(evens) # [2, 4]

names = ['austin', 'angel','anthony','billy','penny']
a_names = list(filter(lambda n: n[0] == "a",names))
print(a_names)

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
# Way_01
inactive_users_01 = list(filter(lambda u: len(u['tweets']) == 0 , users)) # [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'guitar_gal', 'tweets': []}]
print(inactive_users_01)
# Way_02
inactive_users_02 = list(filter(lambda u: not u['tweets'], users)) # [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'guitar_gal', 'tweets': []}]
print(inactive_users_02)

# Combining filter and map
# Given the list of names:
names = ['Lassie','Ankit','Rusty','Yash']
# Task: Return a new list with the string, "Your instructor is "+each value in the array, but only if the value is less than 5 characters.
print(names)
print(list(map(lambda name: f"Your instructor is {name}",filter(lambda val: len(val) < 5, names)))) # ['Your instructor is Yash']

print(list(map(lambda user:user["username"].upper() ,filter(lambda u: not u['tweets'],users))))

# all : Return True if all elements of the iterable are truthy (or if the iterable is empty)
print(all([0,1,2,3])) # False

print(all([char for char in 'eio' if char in 'aeiou'])) # True

print(all([num for num in [4,2,10,6,8] if num % 2 == 0])) # True

# any : Return True if any element of the iterable is truthy. If the iterable is empty, return False
print(any([0,1,2,3])) # True

print(any([val for val in [1,2,3] if val > 2])) # True

print(any([val for val in [1,2,3] if val > 5])) # False

import sys
list_comp = sys.getsizeof([x*10 for x in range(10000)])
gen_exp = sys.getsizeof(x*10 for x in range(10000))

print("To do the same thing, it takes...")
print(f"List Comprehension: {list_comp} bytes")
print(f"Generator Expression: {gen_exp} bytes")

# sorted : Returns a new sorted list from the itemms in iterable wheareas .sort() sort the iterable in place.
# sorted (works on anything that is iterable)
more_numbers = [6, 1, 8, 2]
print(sorted(more_numbers))
print(sorted(more_numbers, reverse=True))

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

print(sorted(users, key=lambda user: user["username"])) # [{'username': 'bob123', 'tweets': []}, {'username': 'doggo_luvr', 'tweets': ['dogs are the best', "I'm hungry"]}, {'username': 'guitar_gal', 'tweets': []}, {'username': 'jeff', 'tweets': []}, {'username': 'katie', 'tweets': ['I love my cat']}, {'username': 'samuel', 'tweets': ['I love cake', 'I love pie', 'hello world!']}]
print(sorted(users, key=lambda user: len(user["tweets"]))) # [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'guitar_gal', 'tweets': []}, {'username': 'katie', 'tweets': ['I love my cat']}, {'username': 'doggo_luvr', 'tweets': ['dogs are the best', "I'm hungry"]}, {'username': 'samuel', 'tweets': ['I love cake', 'I love pie', 'hello world!']}]

print(sorted(users, key=lambda user: len(user["tweets"]), reverse=True))

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

print(sorted(songs,key=lambda s:s['playcount'])) # [{'title': 'happy birthday', 'playcount': 1}, {'title': 'Survive', 'playcount': 6}, {'title': 'Toxic', 'playcount': 31}, {'title': 'YMCA', 'playcount': 99}]