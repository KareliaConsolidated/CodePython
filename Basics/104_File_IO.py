# Reading Files - OPTION 01
# You can read the file with the open function.
# "open" returns a file object to you.
# You can read a file object with the "read" method.
file = open('Datasets/story.txt')
print(file.read())

# Cursor Movement
# Python reads files by using a cursor
# This is like the cursor you see when you're typing
# After a file is read, the cursor is at the end.
# To move the cursor, use the "seek" method.
print(file.seek(0)) #To Reset Position to Start
print(file.readline()) # To Read Line one by one
# readlines reads the file into memory as a list of strings, raed reads the file into memory as a single string.

# Closing a File
# You can close a file with the "close" method.
# You can check if a file is closed with the "closed" attribute
# Once closed, a file can't be read again
# Always close files - it frees up system resources !
print(file.closed) # FALSE
print(file.close()) 
print(file.closed) # TRUE

# Reading Files - OPTION 02
with open('Datasets/story.txt') as file:
	data = file.read() # File will closed automatically after the block, we dont have to close it manually.

print(file.closed) # True

# Writing Files
# You can also use "open" to write to a file.
# Need to Specify the "w" flag as the second argument.
with open('Datasets/story_write.txt', "w") as file: # If File does not exist, file will created for you!
	file.write("Writing Files is Great\n")
	file.write("Here's another line of text\n")
	file.write("I think that's enough line check, GoodBye!")

# Modes for Opening Files
# r - Read a file(no writing) - This is the Default
# w - Write to a file (previous contents removed)
# a - Append to a file (previous contents not removed)

with open("Datasets/story_write.txt", "a") as file:
	file.write(":) \n")

# r+ - Read and Write to a file (writing based on cursor)
with open("Datasets/story_write.txt", "r+") as file: # Won't Create New File, If doesn't exist.
	file.write("Added using r+") # It enter from the start, but overrides.
	file.seek(10)
	file.write(":)")

