# Multidimensional List
# List can contain any kind of element, even other lists!
nested_list = [[1,2,3], [4,5,6], [7,8,9]]

# Accessing Nested Lists
nested_list[0][1] # 2
nested_list[1][-1] # 6

# Printing Values in Nested Lists
for l in nested_list:
	for val in l:
		print(val)

coords = [[10.423, 9.132], [37.212, -14.092], [21.367, 32.572]]
# For Loop
for loc in coords:
	for coord in loc:
		print(coord)

# List Comprehension
[[print(l) for l in val] for val in coords]

# Another Example
board = [[num for num in range(1,4)] for val in range(1,4)]
print(board) # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

print([["X" if num % 2 != 0 else "O" for num in range(1,4)]for val in range(1, 4)]) # [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]

# Using a List Comprehension and range(), create a variable called answer with the following value [[0,1,2],[0,1,2],[0,1,2]]
print([[val for val in range(0,3)] for num in range(0,3)])