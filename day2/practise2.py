# data types

# string

print("Hello"[4])

print("123" + "345")

# Integer

print(123+345)

# to interpret comma to number counting we can use _ for that
print(123_345_678)

# Float

print(31.3232)

# Boolean

# True
# False

a = float(123)
print(type(a))


print(str(70)+str(100))

twoDigitNumber = input("Write two digit number:\n")

# get the first and second digit usig subscripting then convert string into int and add them 
print(int(twoDigitNumber[0])+int(twoDigitNumber[1]))


# Mathematical operation

# addition +
# subtraction -
# multiplication *
# division / , division gives float type as output
# power to ** 
print(2**3)


# priority PEMDAS () > ** > */ > +-

print(3 * 3 + 3 / 3 - 3) # 7.0
print(3 * ( 3 + 3 ) / 3 - 3 ) # 3.0

# BMI calculator

height = float(input('Enter your height in m: \n'))
weight = int(input('Enter your weight in kg: \n'))

bmi = weight/(height**2)
# print(bmi)

# f-Strings
print(f"your BMI index is {bmi}")

# program to count number of days left to die if we die at 90
currentAge = int(input("give me your current age: \n"))

ageLeft = 90 - currentAge
ageMonths = ageLeft * 12
ageweek = ageLeft * 52
ageDay = ageLeft * 365

print(f"You have {ageDay} days, {ageweek} weeks, and {ageMonths} months left")

