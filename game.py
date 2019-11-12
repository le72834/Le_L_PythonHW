#import the random package so that we can generate a random choice
from random import randint
from gamefunctions import winlose, gamelinh

while gamelinh.player is False:
		#set player to True
		print("***********************************")
		print("Computer lives: ", gamelinh.computer_lives, "/", gamelinh.total_lives,"\n")
		print("Player lives: ",gamelinh.player_lives,"/", gamelinh.total_lives, "\n")
		print("Choose your weapon!\n")
		print("***********************************")

		player = input("choose rock, paper or scissors: ")
		player = player.lower()


		print("computer chose", gamelinh.computer,"\n")
		print("player chose", player, "\n")

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

		# handle all lives lost for player or AI
		if gamelinh.player_lives is 0:
				winlose.winorlose("lost")
					#print("Out of lives! You suck at this game. Would you like to play again?\n")
					#choice = input("Y / N")
					#print(choice)

				#if (choice is "N") or (choice is "n"):
					#print("You chose to quit.")
					#exit()

				#elif (choice is "Y") or (choice is "y"):
					#reset the game so we can play again
						#player_lives = 5
					#gamelinh.computer_lives = 5
					#player = False
					#gamelinh.computer = choices[randint(0,2)]


		elif gamelinh.computer_lives is 0:
				winlose.winorlose("won")
				#print("Out of lives! You suck at this game. Would you like to play again?\n")
				#choice = input("Y / N")
				#print(choice)

			#if (choice is "N") or (choice is "n"):
				#print("You chose to quit.")
				#exit()

			#elif (choice is "Y") or (choice is "y"):
				#reset the game so we can play again
				#player_lives = 5
				#gamelinh.computer_lives = 5
				#player = False
				#gamelinh.computer = choices[randint(0,2)]

		else:
			#need to check all of our conditions after checking for a tie
			player = False
			gamelinh.computer = gamelinh.choices[randint(0,2)]
