# Modules
# Why Use Modules ?
# Keep Python Files Small
# Reuse code across multiple files by importing
# A module is just a Python file!

# Built-in Modules Example
import random as rand
print(rand.choice(["apple", "banana", "cherry", "durian"]))
# random = rand.shuffle(["apple", "banana", "cherry", "durian"])


# Importing Parts of a Module
# The from keyword lets you import parts of a module
# If you still want to import everything, you can also use the from MODULE import * pattern.
# from random import choice, shuffle
from random import shuffle,choice
deck = ['ace','two','three','four']
shuffle(deck)
print(deck)
#-----------------------------------------------#
# Custom Modules
# file1.py
# def fn():
# 	return "do some stuff"

# def other_fun():
# 	return "do some stuff"
#-----------------------------------------------#
# file2.py
# import file1
# file1.fn()
# file1.other_fun()
#-----------------------------------------------#
