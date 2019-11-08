# Iterator: An object that can be iterated upon. An object which returns data, one element at a time when next() is called on it.

# Iterable: An object which will return an iterator when iter() is called on it.

# NEXT - When next() is called on an iterator, the iterator returns the next item. It keeps doing so until it raises a StopIteration Error.
def for_my(iterator, func):
	iterator = iter(iterator)
	while True:
		try:
			thing = next(iterator)
		except StopIteration:
			break
		else:
			func(thing)

def square(x):
	print(x*x)

for_my("lol", print)
for_my([1,2,3,4,5], square)

# Writing a Custom Iterator 
class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration

for x in Counter(29,39):
	print(x)