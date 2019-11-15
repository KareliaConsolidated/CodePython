def copy(file_name, new_file_name):
	with open(file_name) as file:
		text = file.read()

	with open(new_file_name, "w") as new_file:
		new_file.write(text)

# Write a function called copy_reverse, which takes in a file name and copies the reversed contents of the first file to second file
def copy_and_reverse(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()

    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])

# Write a function called statistics, which takes in a filename and returns a dictionary with the number of lines, words, and characters in the file
def statistics(file_name):
	with open(file_name) as file:
		lines = file.readlines()

	return {"lines": len(lines),
			"words": sum(len(line.split(" ")) for line in lines),
			"characters": sum(len(line) for line in lines)}

print(statistics('Datasets/story.txt')) # {'lines': 3, 'words': 24, 'characters': 123}

# Write a function called find_and_replace, which takes in a file name, a word to search for, and a replacement word. Replaces all instances of the word in the file with the replacement word.

def find_and_replace(file_name, old_word, new_word):
	with open(file_name, "r+") as file:
		text = file.read()
		new_text = text.replace(old_word, new_word)
		file.seek()
		file.write(new_text)
		file.truncate()
