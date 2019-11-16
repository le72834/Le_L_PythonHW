from random import randint
from gamefunctions import gamelinh

# define a python function that takes an argument
def winorlose(status):
	#status will be either won or lost - you're passing this is as an argument
	print("called win or lose")
	print("**************************")

	print("You", status, "! Would you like to play again?")

	choice = input("Y / N: ")
	print(choice)

	if (choice is "N") or (choice is "n"):
		print("You chose to quit.")
		exit()

	elif (choice is "Y") or (choice is "y"):
		#reset the game so that we can start all over again
		gamelinh.player_lives = 1
		gamelinh.computer_lives = 1
		gamelinh.total_lives = 1
		gamelinh.player = False
		gamelinh.computer = gamelinh.choices[randint(0,2)]

	else:
		# use recursion to call winorlose again until we get the right input
		# recursion is just a fancy way to describe calling a function from within itself
		winorlose(status)

	
		