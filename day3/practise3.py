# print("Welcome to rollercoster!!")

height = int(input("What is your height in cm? \n"))

# if else statemet
if height >= 120:
	print("You can ride rollercoster")
else:
	print("Sorry, you have to grow taller before you can ride")


# odd and even number

number = int(input("Which number do you want to check? \n"))

if number%2 == 1:
	print(f"{number} is odd number")
else:
	print(f"{number} is even number")



# nested if else statements and elif statements

age = int(input("enter you age : \n"))

if height >= 120: 
	print("you can ride rollercoster!")
	if age < 12:
		bill = 5
		print("your ticket prize is 5 dollers")
	elif age < 18:
		bill = 7
		print("your ticket prize is 7 dollers")
	elif age >= 45 ad age <= 55:
		print(:you don't need ticket)
	else:
		bill = 12
		print("your ticket prize is 5 dollers")

	wantPhoto = input("do you want photo or not type Y or N")
	if wantPhoto == 'Y':
		bill += 3
else:
	print("Sorry, you have to grow taller before you can ride")

height = float(input('Enter your height in m: \n'))
weight = int(input('Enter your weight in kg: \n'))

bmi = round(weight/(height**2))

if bmi < 18.5:
	print(f"Your bmi is {bmi} and you are underweight")
elif bmi < 25:
	print(f"Your bmi is {bmi} and you are normal weight")
elif bmi < 30:
	print(f"Your bmi is {bmi} and you are overweight")
elif bmi < 35:
	print(f"Your bmi is {bmi} and you are obese")
else:
	print(f"Your bmi is {bmi} and you are clinically obese")

# leap year calculations

year = int(input("which year you want to check? \n"))

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 ==0:
			print("leap year")
		else:
			print("Not leap year")
	else:
		print("leap year")
else:
	print("Not leap year")


print("Welcome to the pizza delivieries!")
size = input("What size pizza do you want : S, M or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you wat extra cheese? Y or N \n")


if size == 'S':
	prize = 15
elif size == 'M':
	prize = 20
else:
	prize = 25

if add_pepperoni == "Y":
	if size == "S":
		prize += 2
	else:
		prize += 3

if extra_cheese == 'Y':
	prize += 1
else:
	pass

print(f"Your final bill is {prize}")



print("welcome to love calculator!!")
name1 = input("your name? \n")
name2 = input("their name? \n")

name1 = name1.lower()
name2 = name2.lower()

name = name1 + name2

t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')


true1 = t + r + u + e

l = name.count('l')
o = name.count('o')
v = name.count('v')

love = l + o +  v + e

percent = str(true1) + str(love)
love_score = int(percent)
# print(percent)
if love_score < 10 or love_score > 90:
	print("you go together like coke and mentos")
elif love_score < 50 and love_score > 40:
	print("you are alright together")
else:
	print(f"your score is {love_score}")
