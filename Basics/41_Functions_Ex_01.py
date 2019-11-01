# Write a function called return_day, this function takes in one parameter (a number from 1-7) and returns the day of the week. If the Number is less than 1 or greater than 7, the function should return None
# Way_01
def return_day(num):
	days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
	# Check to see if num is valid
	if num > 0 and num < len(days):
		return days[num-1]
	return None
print(return_day(5)) # Thursday
# Way_02
def return_day(num):
	try:
		return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
	except IndexError as e:
		return None
print(return_day(7)) # Saturday
print(return_day(6)) # Friday