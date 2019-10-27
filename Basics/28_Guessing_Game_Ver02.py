from random import randint

random_number = randint(1,10)

while True:
	guess = int(input("Pick a number from 1 to 10: "))
	if guess < random_number:
		print("TOO LOW !")
	elif guess > random_number:
		print("TOO HIGH !")
	else:
		print("YOU WON !")
		play_again = input("Do you want to play again ? (y/n): ").lower()
		if play_again == "y":
			random_number = randint(1,10) # Numbers 1-10
			guess = None
		else:
			print("Thank You !")
			break

