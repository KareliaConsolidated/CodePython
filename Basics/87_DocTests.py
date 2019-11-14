# We can write tests for functions inside of the docstring
# Write code that looks like its inside of a REPL
# def add(a, b):
# 	"""
# 	>>> add(2, 3)
# 	5
# 	>>> add(100, 300)
# 	400
# 	"""
# 	return a + b

# COMMAND TO RUN
# python -m doctest -v 87_DocTests.py

def  double(values):
	"""Double the Values in a list
	>>> double([1,2,3,4])
	[2, 4, 6, 8]

	>>> double([])
	[]

	>>> double(['a', 'b', 'c'])
	['aa', 'bb', 'cc']"""
	return [2*element for element in values]

def say_hi():
	"""
	>>> say_hi()
	"hi"
	"""
	return "hi"

def true_that():
	"""
	>>> true_that()
	True
	"""
	return True

def make_dict(keys):
	"""
	>>> make_dict(['a','b'])
	{'a': True, 'b': True}
	"""
	return {key: True for key in keys}