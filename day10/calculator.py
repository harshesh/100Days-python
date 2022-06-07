from replit import clear

# ADD
def add(n1, n2):
	return n1 + n2 

# SUBtRACT
def subtract(n1, n2):
	return n1 - n2 

# MULTIPLY
def multiply(n1, n2):
	return n1 * n2 

# DIVIDE
def divide(n1, n2):
	return n1/n2

operations = {
	'+': add,
	'-': subtract,
	'*': multiply,
	'/': divide
}


def calculator():
	num1 = float(input('What is the first number: \n'))
	for i in operations:
		print(i)

	shouldContinue = True
	while shouldContinue:
		operationSymbol = input("Pick an operations from above: ")
		num2 = float(input('What is the second number: \n'))
		result = operations[operationSymbol](num1, num2)
		print(f"{num1} {operationSymbol} {num2} = {result}")
		yN = input(f"Type 'y' to continue calculating with {result}, or Type 'n' to start new calculator: ")
		if  yN== 'y':
			num1 = result
		elif yN == 'n':
			shouldContinue = False
			clear()
			calculator()

calculator()