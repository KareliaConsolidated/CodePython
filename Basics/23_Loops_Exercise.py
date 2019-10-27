# Way 01
for num in range(1,21):
	if num == 4 or num == 13:
		print(f"x is {num}, and its unlucky")
	elif num % 2 == 0:
		print(f"x is {num}, and its even")
	else:
		print(f"x is {num}, and its odd")

# Way 02
for num in range(1,21):
	if num == 4 or num == 13:
		state = "unlucky"
	elif num % 2 == 0:
		state = "even"
	else:
		state = "odd"
	print(f"{num} is {state}")