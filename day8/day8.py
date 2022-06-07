
# Normal function
def greet():
	print("Hello")
	print("bye")
	print('thank you')

greet()

# function that allows for inputs
def greetWithName(name):
	print(f"Hello {name}")

greetWithName("Sasuke")

# function with more than 1 input
def greetWith(name, location):
	print(name)
	print(location)

greetWith('Sasuke', 'The leaf village ')

# function with keyword argument
greetWith(name="Sasuke", location='The leaf village')

def cal(width, height, cover):
	import math
	noOFCans = math.ceil((width*height)/cover)
	print(f"You will need {noOFCans} Cans.")


testH = int(input("Height of Wall: "))
testW = int(input("Width of Wall: "))
coverge = 5
cal(testW, testH, coverge)


# prime number checker
def prime_checker(number):
	is_Prime = True
	for i in range(2, int(number/2)):
		if number%i == 0:
			is_Prime = False
	if is_Prime:
		print(f"{number} is Prime Number")
	else:
		print(f"{number} is not Prime Numberr")




n = int(input("Enter the number : \n"))
prime_checker(n)
