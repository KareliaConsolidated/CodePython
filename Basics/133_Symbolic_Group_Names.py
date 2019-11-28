import re
def parse_name(input):
	name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) ([A-Za-z]+)$')
	matches = name_regex.search(input)
	print(matches.group('first'))

parse_name('Mr. Sheldon Copper') # Sheldon