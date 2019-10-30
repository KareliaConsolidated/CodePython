# List: It's just a collection or grouping of items !
# Creating List
demo_list = ["a", 1.45, True, 6.777]
print(type(demo_list))

# Another Way to Make a List
tasks = list(range(1, 4))
print(tasks)
print(list(range(1,10)))

# Accessing Values in a List
friends = ["Ashley", "Matt", "Michael"]
# Like ranges, list ALWAYS start counting at zero. So the first element lives at index 0.
print(friends[0]) # Ashley
print(friends[1]) # Matt
print(friends[2]) # Michael
# print(friends[3]) # Index Error

# Accessing Values from the End
# You can use a negative number to index backwards.
print(friends[-1]) # Michael
print(friends[-2]) # Matt
print(friends[-3]) # Ashley

# Accessing Data in Lists
friends = ["Ashley", "Matt", "Michael"]
"Ashley" in friends # True
"Karelia" in friends # False

if "Ashley" in friends:
	print("You are really good friend !")

# Accessing All Values in a List
# Way_01 : For Loop
numbers = [1,2,3,4,5,6]
for number in numbers:
	print(f"{number} square is {number * number}")

# Way_02 : While Loop
index = 0
while index < len(numbers):
	print(numbers[index])
	index += 1

# List Methods
print('####### List Methods #######')
# Adding Data to a List
# Append: Add an item to the end of the list, takes only one argument.
first_list = [1,2,3,4]
second_list = [1,2,3,4]
first_list.append(5)
print(first_list) # [1,2,3,4,5]
second_list.append([5,6])
print(second_list)

# Extend: Add to the end of a list all values passed to extend.
first_list.extend([5,6,7,8])
print(first_list) # [1,2,3,4,5,5,6,7,8]

# Insert: It Insert an Item at a Given Position
first_list_insert = [1,2,3,4]
first_list_insert.insert(2, 'Hello there')
print(first_list_insert)

first_list_insert.insert(-1, 'The End!') # Will Place it as per Index
print(first_list_insert)

# To Add the Item, for Unknown Length of List
first_list_insert.insert(len(first_list_insert), 'NUMS')
print(first_list_insert)

# To Remove the Items
# Clear: Remove all items from the list.
first_list = [1,2,3,4]
first_list.clear()
print(first_list)

# Pop: Remove the item at the given position in the list, and return it.
# If no index is specified, removes and returns last item in the list.
pop_list = ["James Blunt", "Jessie J", "Backstreet Boys", "Badhshah"]
print(pop_list.pop(2)) # Backstreet Boys
print(pop_list.pop()) # Badhshah

# Remove: Remove the first item from the list whose value is x, throws a ValueError if the item is not found.
first_remove = [1, 2, 3, 4, 4, 4]
first_remove.remove(2)
print(first_remove)

# Index: Returns the index of the specified item in the list.
num_index = [5, 6, 7, 8, 9, 10]
num_index.index(6) # 1
num_index.index(9) # 4

# Can Specify start and end point.
num_index = [5, 5, 6, 7, 5, 8, 9, 8 ,10]
num_index.index(5) # 0
num_index.index(5, 1) # 1
num_index.index(5, 1) # 1
num_index.index(5, 2) # 4

# Looking for 8 between the index 6 and 8
num_index.index(8, 6, 8) # 7

# Count: Return the number of times x appears in the list.
num_count = [1, 2, 3, 4, 3, 2, 1, 4, 10, 2]
num_count.count(2) # 3
num_count.count(21) # 0
num_count.count(21) # 2

# Reverse: Reverse the Elements of the list (in-place)
# It Updates the List
first_reverse = [1,2,3,4]
print(f"Preview Before Reverse : {first_reverse}")
first_reverse.reverse()
print(f"Preview After Reverse : {first_reverse}")

# Sort: Sort the Items of the list (in-place)
another_list = [6, 4, 1, 2, 5]
another_list.sort()
print(another_list) # [1, 2, 4, 5, 6]

# Join: Technically a String Method that takes an iterable argument.
# Concatenates(combines) a copy of the base string between each item of the iterable.
# Returns a New String
# Can be used to make sentences out of a list of words by joining on a space, for instance:
words = ['Coding', 'is', 'Fun!']
print(' '.join(words)) # 'Coding is Fun!'
print(', '.join(words)) # 'Coding is Fun!'

# Slicing: Make new lists using slices of the old list!
# some_list[start:end:step]
first_slice = [1, 2, 3, 4]
first_slice[1:] # [2, 3, 4]
first_slice[3:] # [4]

# If you enter a negative number, it will start the slice that many back from the end.
first_slice[-1:] # [4]
first_slice[-3:] # [2, 3, 4]

# Second Parameter for Slice: end
# The index to copy up to (exclusive counting).
first_slice[:2] # [1, 2]

# With negative numbers, how many items to exclude from the end (i.e. indexing by counting backwards)
first_slice[:-1] # [1, 2, 3]
first_slice[1:-1] # [2, 3]

# Third Parameter for Slice: step
# "step" in Python is basically the number to count at a time.
# Same as step with range!
first_slice = [1, 2, 3, 4, 5, 6]
first_slice[1::2] # [2, 4, 6]
first_slice[::2] # [1, 3]

# With Negative Numbers, Reverse the Order
first_slice[1::-1] # [2, 1]
first_slice[:1:-1] # [6, 5, 4, 3]
first_slice[2::-1] # [3, 2, 1]

# Tricks with Slices
# Reversing Lists/Strings
string = "This is fun!"
print(string[::-1])

# Modifying Portions of Lists
numbers = [1,2,3,4,5,6]
numbers[1:3] = ['a','b','c']
print(numbers) # [1,'a','b','c',4,5,6]

# Swapping Values
names = ["June","November"]
names[0],names[1] = names[1],names[0]
print(names) # ["November", "June"]