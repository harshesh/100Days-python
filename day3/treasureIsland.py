print("Welcome to treasure islands, Your mission is to find treasure")

leftRight = input("left or right : ").lower()

if leftRight == 'left':
	swimWait = input("swim or wait").lower()
	if swimWait == "wait":
		color = input("Which color Blue, Yellow, red").lower()
		if color == 'yellow':
			print("win")
		else:
			print("Game Over")
	else:
		print("Game Over")
else:
	print("Game over")