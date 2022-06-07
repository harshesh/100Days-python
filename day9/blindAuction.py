from replit import clear
# print("My name")
# clear()

trigger = True
nameBid = {}

while trigger:
	name = input("What is your name: \n")
	bid = int(input("What is your bid? \n"))
	nameBid[name] = bid
	yesNo = input("Is there any other bid - Type Yes or No : \n")
	if 'y' in yesNo:
		clear()
	else:
		trigger = False
		maxValue = max(zip(nameBid.values(), nameBid.keys()))
		print(f'The highest bid is {maxValue[0]} from {maxValue[1]}')

print("Done")