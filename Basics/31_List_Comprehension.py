nums = [1,2,3]
print([x*10 for x in nums])

# List Comprehension vs Looping
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []
for num in numbers:
	doubled_number = num * 2
	doubled_numbers.append(doubled_number)

print(doubled_numbers)

# List Comprehension
doubled_numbers_lc = [num*2 for num in numbers]
print(doubled_numbers_lc)

# Examples
name = 'Karelia'
print(''.join([char.upper() for char in name])) # KARELIA

friends = ['john', 'archer', 'charles']
print([char[0].upper()+char[1:] for char in friends]) # ['John', 'Archer', 'Charles']

print([num*10 for num in range(1,6)]) # [10,20,30,40,50]

print([bool(val) for val in [0,[],'']]) #[False, False, False]

num_list = [1, 2, 3, 4, 5]
string_list = [str(num) for num in num_list]
print(string_list)

colors = ['red', 'orange', 'yellow', 'green', 'indigo', 'violet']
print([color.upper() for color in colors])

# Using For Loop
name_list = ['Ellie', 'Tim', 'Matt']
new_name_list = []
for name in name_list:
	name_upper = name[0].upper()
	new_name_list.append(name_upper)

print(new_name_list)

# Using List Comprehension
print([name[0].upper() for name in name_list])
