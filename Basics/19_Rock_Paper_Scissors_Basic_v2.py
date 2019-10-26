print("Rock...")
print("Paper...")
print("Scissors...")

player_01 = input("Player 1, make your move: ")
print("***NO CHEATING!***\n\n" * 5)
player_02 = input("Player 2, make your move: ")

if player_01 == player_02:
	print("It's a Tie!")
elif player_01 == "rock":
	if player_02 == "scissors":
		print("Player 1, Wins !")
	elif player_02 == "paper":
		print("Player 2, Wins !")
elif player_01 == "paper":
	if player_02 == "rock":
		print("Player 1, Wins !")
	elif player_02 == "scissors":
		print("Player 2, Wins !")
elif player_01 == "scissors":
	if player_02 == "paper":
		print("Player 1, Wins !")
	elif player_02 == "rock":
		print("Player 2, Wins !")	
else:
	print("Something Went Wrong")