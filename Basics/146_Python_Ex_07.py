# SumUp Diagonals
# Write a function called sum_up_diagonals which accepts an N*N list of lists and sums the two main diagonals in the array; the one from the upper left to the lower right, and the one from the upper right to the lower left.
def sum_up_diagonals(arr):
	total = 0
	for i,val in enumerate(arr):
		total += arr[i][i]
		total += arr[i][-1-i]
	return total

list1 = [
	[1,2],
	[3,4]
]

list2 = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]

list3 = [
	[4,1,0],
	[-1,-1,0],
	[0,0,9]
]

list4 = [
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
	[13,14,15,16]
]

print(sum_up_diagonals(list1)) # 10
print(sum_up_diagonals(list2)) # 30
print(sum_up_diagonals(list3)) # 11
print(sum_up_diagonals(list4)) # 68