# Sets : Sets are like formal mathematical sets.
# Sets do not have duplicate values.
# Element in sets aren't ordered.
# You cannot access items in a set by index.
# Sets can be useful if you need to keep track of a collection of elements, but don't care about ordering, keys or values and duplicates.
# Creating / Accessing
s = set({1,2,3,4,4,5,6,6,6})
print(s) # {1, 2, 3, 4, 5, 6}

# Creating a new set
s = {1, 4, 5}

print(4 in s) # True
print(8 in s) # False

# Accessing All Values in a Set
for number in s:
	print(number)

cities = ['Mumbai', 'Delhi', 'Delhi', 'Mumbai', 'Indore']
print(list(set(cities))) # ['Indore', 'Delhi', 'Mumbai']
print(len(set(cities))) # 3

# Set Methods: Working with sets is very common- there are quite a few things we can do !

# add: Adds an element to a set, if the element is already in the set, the set doesn't change:
some_set = set([1,2,3])
some_set.add(4)
print(some_set) # {1, 2, 3, 4}
some_set.add(4)
print(some_set) # {1, 2, 3, 4}

# remove: removes a value from the set - returns a KeyError if the value is not found
set1 = {1,2,3,4,5,6}
set1.remove(3)
print(set1) # {1,2,4,5,6}
# set1.remove(7) # KeyError
# If you need to avoid KeyErrors use .discard()
set1.discard(7)

# copy: creates a copy of the set
set_copy = set([1,2,3])
another_set = set_copy.copy()
another_set # {1,2,3}
another_set is set_copy # False

# clear: Removes all the contents of the set
another_set.clear()

# Set Math
# Suppose I teach two classes:
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
bio_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

# Union (All Students Once, No Duplicates)
print(math_students | bio_students) # {'Aparna', 'Matthew', 'Prashant', 'Oliver', 'Jane', 'Charlotte', 'Mesut', 'James', 'Helen'}

# Common Students
print(math_students & bio_students) # {'Matthew', 'James'}