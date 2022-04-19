import random

# random_integer = random.randint(1, 10)
# print(random_integer)


# random_float = random.random()
# print(random_float)



# headsTails = random.randint(0, 1)

# if headsTails == 0:
# 	print("Tails")
# else:
# 	print("Heads")


# # Data structure Lists

# fruits = ['apple', 'mango', 'oranges', 'kivy']

# print(fruits[0])

# names = input("give names using comma sepaeration").split(", ")
# length = len(names)

# rand = random.randint(0, length-1)
# print(names[rand])
# print(random.choice(names))

# list1 = [" ", " ", " "]
# list2 = [" ", " ", " "]
# list3 = [" ", " ", " "]
# map1 = [list1, list2, list3]
# print(f"{list1}\n{list2}\n{list3}")

# choice = input("Where do you want to put the treasure: \n")

# one = int(choice[0])
# two = int(choice[1])
# print(one, two)
# map1[one-1][two-1] = 'X'
# print(map1)

rpsChoice = int(input("Select 0 for rock, 1 for paper and 2 for scissors \n"))

choice = random.randint(0,2)
print("Computer selects ", choice)

if rpsChoice > 2:
	print("You choose wrong number")
elif choice == rpsChoice:
	print("Draw")
elif choice == 0 and rpsChoice == 1:
	print("User wins")
elif choice == 0 and rpsChoice == 2:
	print("Computer wins")
elif choice == 1 and rpsChoice == 0:
	print("Computer wins")
elif choice == 1 and rpsChoice == 2:
	print("User wins")
elif choice == 2 and rpsChoice == 0:
	print("User wins")
elif choice == 2 and rpsChoice == 1:
	print("Computer wins")
else:
	pass


