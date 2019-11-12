#how to pass argument into a funtion
#
def comparestuff(thing1, thing2):
	#compare and print all the things
	if thing1 == thing2:
		print("they match!")
	else:
		print("they do not match")

# invoice a function by writing its name (calling it)
# and passing arguments


comparestuff('stuff', 'stuff')

comparestuff('stuff', 'other stuff')

comparestuff(1, 1)
comparestuff(1, 2)