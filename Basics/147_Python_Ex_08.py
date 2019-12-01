# Min Max Key in Dictionary
# Write a function min_max_key_in_dictionary which returns a list with the lowest key in the dictionary and the highest key in the dictionary. You can assume that the dictionary will have keys that are numbers.
def min_max_key_in_dictionary(dic):
	dic = dic.keys()
	return [min(dic), max(dic)]
print(min_max_key_in_dictionary({2:'a', 7:'b', 1:'c', 10:'d', 4:'e'}))
print(min_max_key_in_dictionary({1: "Ellie", 4: "Matt", 2: "Tim"}))