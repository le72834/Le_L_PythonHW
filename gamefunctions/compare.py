from gamefunctions import gamelinh


#what are you trying to compare inside this functions?
#you will need to pass those things in as arguments
#inside the round brackets
def comparechoices():
	if player.lower() == "quit":
					exit()
			elif gamelinh.computer == player:
	 				print("tie! no one wins, play again")


			elif player.lower() == "rock":
					if gamelinh.computer == "paper":
						print("You lose!", gamelinh.computer, "covers", player, "\n")
						gamelinh.player_lives = gamelinh.player_lives - 1
					else:
						print("You win!", player, "smashes", gamelinh.computer, "\n")
						gamelinh.computer_lives = gamelinh.computer_lives - 1

			elif player.lower() == "paper":
					if gamelinh.computer == "scissors":
						print("You lose!", gamelinh.computer, "cuts", player, "\n")
						gamelinh.player_lives = gamelinh.player_lives - 1
					else:
						print("You win!", player, "smashes", gamelinh.computer, "\n")
						gamelinh.computer_lives = gamelinh.computer_lives  - 1

			elif player.lower() == "scissors":
					if gamelinh.computer == "rock":
						print("You lose!", gamelinh.computer, "smashes", player, "\n")
						gamelinh.player_lives = gamelinh.player_lives - 1
					else:
						print("You win!", player, "cuts", gamelinh.computer, "\n")
						gamelinh.computer_lives = gamelinh.computer_lives - 1

			else: 
					print("That's not a valid choice, try again!")