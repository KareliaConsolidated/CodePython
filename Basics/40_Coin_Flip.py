from random import random

def flip_coin():
	# Generate Random Number 0 or 1
	r = random() # Gives Number between 0 and 1
	if r > 0.5:
		return "Heads"
	else:
		return "Tails"

print(flip_coin())