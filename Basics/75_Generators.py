# Generators are Iterators.
# Generators can be created with generator functions.
# Generator function use the yield keyword.
# Generators can be created with generator expressions.
# Functions               # Generator Functions
# uses return			  # uses yield
# returns once			  # can yield multiple times
# When invoked, returns the return value  # Whe invoked, returns a generator
def count_up_to(max):
	count = 1
	while count <= max:
		yield count
		count += 1

counter = count_up_to(5)
print(next(counter))

for i in counter:
	print(i)

# Writing a Beat Making Generator
def current_beat():
	nums = (1,2,3,4)
	i = 0
	while True:
		if i >= len(nums): i = 0
		yield nums[i]
		i += 1

counter = current_beat()
print(next(counter)) # 1
print(next(counter)) # 2
print(next(counter)) # 3
print(next(counter)) # 4

# Testing Memory Usage with Generators
# WITHOUT A GENERATOR....
# To generate first 1,000,000 fib numbers, it has to store all of them in a list
def fib_list(max):
     nums = []
     a, b = 0, 1
     while len(nums) < max:
         nums.append(b) 
         a, b = b, a+b
     return nums

# fib_list(1000000)


# USING A GENERATOR...
# To generate first 1,000,000 fib numbers,no list needed!
def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x, y = y, x + y
        yield x
        count+=1

print("FIB SERIES")
for n in fib_gen(10):
	print(n)

# Generator Expression and Speed Testing
import time

gen_start_time = time.time()
print(sum(n for n in range(100000000)))
gen_time = time.time() - gen_start_time


list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_time = time.time() - list_start_time

print(f"Gen Comp Took {gen_time}")
print(f"List Comp Took {list_time}")