# Find_The_Duplicate
# Write a function called find_the_duplicate which accepts an array of numbers containing a single duplicate. The function returns the number which is duplicate or None if there are no duplicates.
def find_the_duplicate(lst):
	counter = {}
	for val in lst:
		if val in counter:
			counter[val] += 1
		else:
			counter[val] = 1
	for key in counter.keys():
		if counter[key] > 1:
			return int(key)

print(find_the_duplicate([1,1,2,4,12])) # 1
print(find_the_duplicate([1,2,3,4])) # None