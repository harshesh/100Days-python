# 2-10 cards are face value
# jack, queen and kinng are 10 
# ace is counnt as 1 or 11 depends on total value if adding 11 is less than 21 than ace value is 11 else 1

# if dealer total is less than 17 than it can get another card
import random

def deal_card():
	""" Returns a random card from the deck. """
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	card = random.choice(cards)
	return card 

def calculate_score(cards):
	# print(cards)
	if sum(cards) == 21 and len(cards) == 2:
		return 0 

	if 11 in cards and sum(cards) > 21:
		cards.remove(11)
		cards.append(1)

	return sum(cards)

def compare(user_score, computer_score):
	if user_score == computer_score:
		return "Draw"
	elif computer_score == 0:
		return "Lose, Opponent has a blackJack"
	elif user_score == 0:
		return "Win with a backJack"
	elif user_score > 21:
		return "You went over, You Loose"
	elif computer_score > 21:
		return "Opponent went over, You win"
	elif user_score > computer_score:
		return "You win"
	else:
		return "You loose"

def play_game():
	user_card = []
	computer_card = []
	is_game_over = False

	for _ in range(2):
		user_card.append(deal_card())
		computer_card.append(deal_card())

	print(f"User Card {user_card}")
	print(f"Computer first card {computer_card[0]}")

	while not is_game_over:
		user_score = calculate_score(user_card)
		computer_score = calculate_score(computer_card)

		if user_score == 0 or computer_score == 0 or user_score > 21:
			is_game_over = True
		else:
			user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
			if user_should_deal == 'y':
				user_card.append(deal_card())
			else:
				is_game_over = True

	while computer_score != 0 and computer_score < 17:
		computer_card.append(deal_card())
		computer_score = calculate_score(computer_card)

	print(f"computer cards {computer_card}")
	print(compare(user_score, computer_score))

while input("Do you want to play a game of blackJack?  Type 'y' or 'n': ") == 'y':
	play_game()
