print("Welcome to tip calculator")

billAmount = float(input("What was the total bill amount? \n"))

tipPercent = int(input("what percentage tip would you like to give? 10, 12 or 15? \n"))

people = int(input("How many people to split the bill ? \n"))

tip_amount = billAmount*(tipPercent/100)
total_amount = billAmount+tip_amount
perPersonSplit = round(total_amount/people, 2)

print(f"Each person should pay {perPersonSplit} RS")