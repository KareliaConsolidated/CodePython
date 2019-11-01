# *args : A special operator we can pass to functions, It will gather all remaining arguments as tuple. This is just a parameter - you can call it whatever you want !
def sum_all_nums(*nums):
	total = 0
	for num in nums:
		total += num
	return total

print(sum_all_nums(1,2,3,4)) # 10

# **kwargs: A special operator we can pass to functions, It will gather remaining keyword arguments as a dictionary.
def fav_colors(**kwargs):
	for person,color in kwargs.items():
		print(f"{person} likes {color}")

fav_colors(john="purple", ruby="red", ethel="teal")

# Parameter Ordering
# 1. Parameters
# 2. *args
# 3. Default Parameters
# 4. **kwargs

# Example
def display_info(a,b,*args,instructor="Karelia",**kwargs):
	return [a,b,args,instructor,kwargs]

print(display_info(1,2,3,last_name="Karelia",instructor="KareliaConsolidated",job="instructor")) # [1, 2, (3,), 'KareliaConsolidated', {'last_name': 'Karelia', 'job': 'instructor'}]