from random import randint
# define a python function that takes an argument

def winorlose(status):
	print("called win or lose")
	print("**************************")

	print("You", status, "! Would you like to play again?")

	choice = input("Y / N")
	print(choice)

		if (choice is "N") or (choice is "n"):
			print("You chose to quit.")
			exit()

		elif (choice is "Y") or (choice is "y"):
			#reset the game so we can play again
			global player_lives
			global computer_lives
			global player
			global computer
			global choices 

			player_lives = 1
			computer_lives = 1
			player = False
			computer = choices[randint(0,2)]

	else:
		#need to check all of our conditions after checking for a tie
		player = False
		computer = choices[randint(0,2)]