# Handle Errors!
# In Python, it is strongly encouraged to use try/except blocks, to catch exceptions when we can do something about them.
# try:
# 	foobar
# except NameError as err:
# 	print(err)

# Why Not Catch Them All
# try:
# 	foobar
# except:
# 	print("Your tried to use a variable that was never declared")
# What we are doing here is catching every error, which means we are not able to correctly identify "what" went wrong. It is highly discouraged to do this.

# def get(d,key):
# 	try:
# 		return d[key]
# 	except KeyError:
# 		return None
# d = {"name":"Smith"}
# print(get(d,"city"))

# try:
# except:
# else:
# finally:
# while True:
# 	try:
# 		num = int(input("Please enter a number: "))
# 	except ValueError:
# 		print("That's not a number")
# 	else:
# 		print("I'M IN THE ELSE!")
# 		break
# 	finally:
# 		print("RUNS NO MATTER WHAT !")
# print("REST OF GAME LOGIC RUNS")

#------------------------------------------------#
def divide(a,b):
	try:
		result = a/b
	except ZeroDivisionError:
		print("Don't Divide By Zero Please !")
	except TypeError as err:
		print(err)
	else:
		print(f"{a} divided by {b} is {result}")

print(divide(3,4))
print(divide(1,'a'))