# Max: Return the largest item in an iterable or the largest of two or more arguments.
print(max(3, 67, 99)) # 99
print(max('c','d','a')) # d

names = ["Arya", "Samson", "Dora", "Tim", "Ollivander", "Harry", "John"]

# finds the minimum length of a name in names
print(min(len(name) for name in names)) # 3

# find the longest name itself
print(max(names, key=lambda n:len(n))) # Ollivander

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# Finds the song with the lowest playcount
print(min(songs,key=lambda s:s['playcount'])) # {'title': 'happy birthday', 'playcount': 1}

# Finds the title of the most played song
print(max(songs,key=lambda s:s['playcount'])['title'])  # YMCA

# Using Loop
# max = 0
# for song in songs:
# 	if song['playcount'] > max:
# 		max = song['playcount']
# print(max)

# Reversed: Return a reverse iterator
print(reversed('hello world')) # <reversed object at 0x000001E614BD81C8>
print(list(reversed('hello world'))) # ['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']
print(''.join(list(reversed('hello world')))) # ['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']

for x in reversed(range(0,10)):
	print(x)

# len: Return the length(the number of items) of an object. The argument may be sequence (such as a string, tuple, list, or range) or a collection (such as a dictionary, set)

print(len('asda')) # 4
 
# abs: Return the absolute value of a number. The argument may be an integer or a floating point number.
print(abs(-23)) # 23

print(abs(2.4444)) # 2.4444

import math
print(math.fabs(-4))  # 4.0

# sum: Takes an iterable and an optional start.
# Return the sum of start and the items of an iterable from left to right and returns the total.
# start by default is 0
print(sum([1,2,3], 10)) # start with 10 adding all the numbers to it, which will result in 16

print(sum([1,2,3], -6))

# round: Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input. 
print(round(10.2)) # 10
print(round(1.212121, 2)) # 1.21
print(round(10, None)) # 10

# zip: Make an iterator that aggregates elements from each of the iterables.
# Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of th argument sequences or iterables.
# The iterator stops when the shortest input iterable is exhausted.
nums1 = [1,2,3]
nums2 = [4,5,6]
first_zip = zip([1,2,3],[4,5,6])
print(list(first_zip)) # [(1, 4), (2, 5), (3, 6)]
print(dict(zip(nums1, nums2))) # {1: 4, 2: 5, 3: 6}

five_by_two = [(0,1), (1,2), (2,3), (3,4), (4,5)]
print(list(zip(*five_by_two))) # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]
print(max(5,6))
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

# Dict Comprehension
print({students[i]:max(midterms[i],finals[i]) for i in range(0,len(students))})

# Trick
# Underscores stores last expression value which is 1 in below case.
# 1
# n = [[9,8,7],[1,2,3],[3,4,5]]
# print([_][2]) #3

final_grades = {pair[0]:max(pair[1],pair[2]) for pair in zip(students,midterms,finals)}

print(final_grades) # {'dan': 98, 'ang': 91, 'kate': 78}

# Using Max
print(list(zip(students,map(lambda pair: max(pair), zip(midterms, finals)))))

# Max Grades
print(dict(zip(students,map(lambda pair:max(pair),zip(midterms,finals)))))

# Average Grades
print(dict(zip(students,map(lambda pair:((pair[0]+pair[1])/2),zip(midterms,finals)))))

# Exercise_01
# Write a lambda that accepts a single number and cubes it. Save it in a variable called cube.
cube = lambda x : x ** 3
print(cube(2))

# Exercise_02
# Write a function called decrement_list that accepts a single list of numbers as a parameter. It should return a copy of the list where each item has been decremented by one. Use map to do this. Ex : decrement_list([1,2,3]) # [0,1,2]
def decrement_list(l):
	return list(map(lambda x:x-1,l))

print(decrement_list([1,2,3])) # [0,1,2]

# Exercise_03
# Write a function called remove_negatives that accepts a list of numbers and returns a copy of the lists with all negative numbers removed. 
def remove_negatives(l):
	return list(filter(lambda l : l>=0, l))

print(remove_negatives([-1,2,3,-4,1])) # [2, 3, 1]

# Any/All Exercise
# Implement a function is_all_strings that accepts a single iterable and returns True if it contains ONLY strings. Otherwise, it should return False
def is_all_strings(l):
	return all(type(val) == str for val in l)

print(is_all_strings(['a', 'b', 'c'])) # True
print(is_all_strings(['a', 'b', 'c', 3])) # False

# Extremes Exercise - Using Min and Max
# Write a function called extremes which accepts an iterable. It should return a tuple containing the minimum and maximum elements.
def extremes(l):
	return (min(l),max(l))

print(extremes([1,2,3,4,5])) # (1, 5)
print(extremes("karelia")) # ('a', 'r')

# Greatest Magnitude Exercise
# Write a function max_magnitude that accepts a single list full of numbers. It should return the magnitude of the number with the largest magnitude(the number that is furthest away from zero)
def max_magnitude(nums):
	return max(abs(val) for val in nums)

print(max_magnitude([300, 20, -900])) # 900

# Sum_Even_Values
# Write a function called sum_even_values. This function should accept a variable number of arguments and return the sum of all the arguments that are divisible by 2. If there are no numbers divisible by 2, the function should return 0. To be clear, it accepts all the numbers as individual arguments.
def sum_even_values(*args):
	return sum(val if val % 2 == 0 else 0 for val in args)

print(sum_even_values(1,2,3,4,5,6)) # 12

# Sum_Floats
# Write a function called sum_floats. This function should accepts a variable number of arguments. This function should return the sum of all the parameters that are floats. If there are no floats the function should return 0.
def sum_floats(*args):
	return sum(val if type(val) == float else 0 for val in args)

print(sum_floats(1,2.0,3.0,4,5,6)) # 5.0

# Interleaving Strings
# Write a function interleave that accepts two strings. It should return a new string containing the 2 strings interwoven or zipped together.For Example: interleave('hi','ha') # hhia
def interleave(str1, str2):
	return ''.join(''.join(val) for val in zip(str1, str2))

print(interleave('hi','ha')) # hhia

# Triple and Filter
# Write a function called triple and filter. This function should accept a list of numbers, filter out every number that is not divisible by 4, and return a new list where every remaining number is tripled.
def triple_and_filter(l):
	return list(map(lambda val: val * 3,(filter(lambda x: x % 4 != 0, l))))

print(triple_and_filter([1,2,3,4])) # [3, 6, 9]

# Extract_Full_Name
# Write a function called extract_full_name. This function should accept a list of dictionaries and return a new list of strings with the first and last name as keys in each dictionary concatenated.
def extract_full_name(dic):
	return list(map(lambda val: f"{val['first']} {val['last']}",dic))

print(extract_full_name([{'first':'John','last':'Smith'},{'first':'Anu','last':'Smith'}]))