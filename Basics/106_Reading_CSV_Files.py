# Reading CSV Files
# CSV Files are a common file format for tabular data.
# We can read CSV files just like other text files
# Python has a built-in CSV module to read/write CSVs more easily

# CSV Module
# reader - lets you iterate over rows of the CSV as lists.
# DictReader - lets you iterate over rows of the CSV as OrderedDicts

# Using Reader
from csv import reader
with open("Datasets/fighters.csv") as file:
	csv_reader = reader(file) # Iterator
	next(csv_reader) # We can move forward once, to ignore headers in the file
	for row in csv_reader:
		# print(row[0]) # Each Row in a List !
		print(row)

 # OUTPUT
# ['Name', 'Country', 'Height (in cm)']
# ['Ryu', 'Japan', '175']
# ['Ken', 'USA', '175']
# ['Chun-Li', 'China', '165']
# ['Guile', 'USA', '182']
# ['E. Honda', 'Japan', '185']
# ['Dhalsim', 'India', '176']
# ['Blanka', 'Brazil', '192']
# ['Zangief', 'Russia', '214']

# Using DictReader
from csv import DictReader
with open("Datasets/fighters.csv") as file:
	csv_reader = DictReader(file)
	for row in csv_reader:
		# Each Row is an OrderedDict
		print(row)

# OrderedDict([('Name', 'Ryu'), ('Country', 'Japan'), ('Height (in cm)', '175')])
# OrderedDict([('Name', 'Ken'), ('Country', 'USA'), ('Height (in cm)', '175')])
# OrderedDict([('Name', 'Chun-Li'), ('Country', 'China'), ('Height (in cm)', '165')])
# OrderedDict([('Name', 'Guile'), ('Country', 'USA'), ('Height (in cm)', '182')])
# OrderedDict([('Name', 'E. Honda'), ('Country', 'Japan'), ('Height (in cm)', '185')])
# OrderedDict([('Name', 'Dhalsim'), ('Country', 'India'), ('Height (in cm)', '176')])
# OrderedDict([('Name', 'Blanka'), ('Country', 'Brazil'), ('Height (in cm)', '192')])
# OrderedDict([('Name', 'Zangief'), ('Country', 'Russia'), ('Height (in cm)', '214')])

# Other Delimiters
# Readers accept a delimiter kwarg in case your data isn't separated by commas
from csv import reader
with open("Datasets/fighters.csv") as file:
	csv_reader = reader(file, delimiter="|") # Iterator
	# next(csv_reader) # We can move forward once, to ignore headers in the file
	for row in csv_reader:
		# print(row[0]) # Each Row in a List !
		print(row)