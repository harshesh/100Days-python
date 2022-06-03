import random

wordList = ['mouse', 'paper', 'apple', 'committee']

chosenWord = random.choice(wordList)

chances = 6
blank = ["_" for _ in chosenWord]
print(blank)

SpaceCon = True
print("You will get Six wrong Chances")

while (SpaceCon):
	guess = input("Guess the chracater: ").lower()
	
	for i in range(len(chosenWord)):
		if guess == chosenWord[i]:
			blank[i] = guess

	if guess not in chosenWord:
		chances -= 1
		if chances == 0:
			print("You Loose")
			SpaceCon = False

	if "_" not in blank:
		SpaceCon = False



	print(blank)

if '_' not in blank:
	print("You won")
	print("")