import random
from replit import clear

from art import logo
from art import vs
from gameData import data

# functions
def formatData(account):
	"""Takes the account data and return the printable format"""

	accountName = account['name']
	accountDesc = account['description']
	accountCountry = account['country']
	# accountFollower = accountA['follower_count']

	return f"{accountName}, a {accountDesc}, from {accountCountry}"

def checkAnswer(guess, a_follower, b_follower):
	"""take the user guess and follower counts and returs if they got it right. """
	if a_follower > b_follower:
		return guess == 'a'
	else:
		return guess == 'b'



# Display art
print(logo)
score = 0
gameShouldContinue = True
accountB = random.choice(data)

# make the game repeatable
while gameShouldContinue:

	# Generate random account from the game data
	accountA = accountB
	accountB = random.choice(data)

	while accountA == accountB:
		accountB = random.choice(data)

	print(f"Compare A : {formatData(accountA)}")

	print(vs)

	print(f"Compare B : {formatData(accountB)}")

	# ask user for guess
	guess = input("Who has more followers, Type A or B: ").lower()


	# check if user is correct
	## get follower count of each account
	A_follower_count = accountA['follower_count']
	B_follower_count = accountB['follower_count']
	is_correct = checkAnswer(guess, A_follower_count, B_follower_count)

	# clear the screen between rounds
	clear()
	print(logo)

	# give user feedback on their guess
	if is_correct:
		score += 1
		print(f"You're right, your score is {score}")
	else:
		gameShouldContinue = False
		print(f"Sorry you are wrong, your final score is {score}")


# making account at position B become the next account at position A.

# clear the screens between rounds

