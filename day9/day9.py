programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected", 
	"Function": "A piece of code that you can easily call over and over again",
	"Loop": "Tha action of doing something over and over again"
}

print(programming_dictionary['Bug'])

# adding new key
programming_dictionary['must']: "to add a new data"

# changing key values
programming_dictionary['must']: "Ypu should add a number"

# # making dictionary empty
# programming_dictionary = {}

# loop through a dictionary
for thing in programming_dictionary:
	print(thing)
	print(programming_dictionary[thing])




# grading criteria system

student_score = {
	"Harry": 81,
	"Ron": 78,
	"Hermoine": 99,
	"Draco": 74,
	"Neville": 62
}

student_grade = {}

for name in student_score:
	score = student_score[name]
	if score > 90:
		student_grade[name] = 'Outstanding'
	elif score > 80:
		student_grade[name] = 'Exceeds Expectation'
	elif score > 70:
		student_grade[name] = "Acceptable"
	elif score <= 70:
		student_grade[name] = "Fail"

print(student_grade)

# nesting of dictinary with list

# normal dict
country = {
	"france": "paris",
	"germany": "Berlin"
}

# dict with list as values of key
country_travel = {
	"France" : ['peris', 'Lille'],
	"Germany": ['stuggart', 'berlin', 'Hamburg']
}

# dict with dict and list

country_travel_value = {
	"France" : {"city_visited":['peris', 'Lille'], "total_visits": 12},
	"Germany": {"city_visited": ['stuggart', 'berlin', 'Hamburg'], "total_visits": 22}
}
print(country_travel_value)

# nesting dict in list
country_travel_list = [
	{
	  "country":"France", 
	  "city_visited":['peris', 'Lille'], 
	  "total_visits": 12
	},
	{
	  "country":"Germany", 
	  "city_visited": ['stuggart', 'berlin', 'Hamburg'], 
	  "total_visits": 22
	}
]
