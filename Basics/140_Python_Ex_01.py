# Running Average
# Create a function running_average that returns a function. When the function returned is passed a value, the current average of all previous function calls. You will have to use closure to solve this. You should round all answers to the 2nd decimal place.
def running_average():
	avg = []
	def inner_avg(num):
		avg.append(num)
		return sum(avg)/len(avg)
	return inner_avg

rAvg = running_average()
print(rAvg(10))
print(rAvg(11))
print(rAvg(12))