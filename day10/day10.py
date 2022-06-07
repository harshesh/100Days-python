# functions with outputs

# single return value
def formatName(fName, lName):
	fullName = fName.title() + ' ' + lName.title()
	return fullName

name = formatName("sasuke", 'UCHIHA')
print(name)


# days in a month
def leapYear(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 ==0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False

def daysInMonth(yearCheck, monthCheck):
	monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if monthCheck == 2 and leapYear(yearCheck):
		return 29
	else:
		return monthDays[monthCheck-1]

year = int(input("Enter a year: \n"))
month = int(input("Enter a month: \n"))
days = daysInMonth(year, month)

print(days)

