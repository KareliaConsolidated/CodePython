# Write a function called frequency. This function accepts a list and search item and returns the number of times the search term appears in the list.
def frequency(li,st):
	return li.count(st)

print(frequency([True,True,True,True,False,False], True)) # 4
print(frequency([True,True,True,True,False,False], False)) # 2