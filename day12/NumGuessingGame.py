
# choosing a random number between 1 and 100
import random

# Constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5 

# function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
	if guess > answer:
		print("Too High")
		return turns - 1 
	elif guess < answer:
		print("Too low")
		return turns - 1
	else:
		print(f"Your guess is correct {answer}")
		return 0

# make function to set difficulty
def set_difficulty():
	level = input("Choose a difficulty. Type 'easy' or 'hard': ")
	if level == "easy":
		return EASY_LEVEL_TURNS
	else:
		return HARD_LEVEL_TURNS

def game():
	print("Welcome to the Number Guessing Game")
	print("I'm thinking of a number between 1 and 100. ")

	answer = random.randint(1, 100)
	turns = set_difficulty()
	print(f"Correct answer is {answer}")

	# Repeat the guessing functionality if they get it wrong
	while turns > 0:
		print(f"You have {turns} attemps remaining to guess the number")

		# Let the user guess the number
		guess = int(input("Make a Guess: "))

		turns = check_answer(guess, answer, turns)
game()