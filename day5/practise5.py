# # loops

# fruits = ['apple', 'pear', 'peach']

# for fruit in fruits:
# 	print(fruit)

# print(fruit)

stu_heights = [129, 138, 878, 677, 990, 222, 333, 444, 111]

noOfStud = 0
summ = 0
highest = 0
for i in stu_heights:
	summ += i
	noOfStud += 1
	if i > highest:
		highest = i
	else:
		pass

print(round(summ/noOfStud))
print(highest)

j = 0
for i in range(0, 101, 2):
	j += i
	# if i % 2 == 0:
	# 	j += i
	# else:
	# 	pass
print(j)

for i in range(101):
	if i % 15 == 0:
		print("fizzbuzz")
	elif i % 3 == 0:
		print("buzz")
	elif i % 5 == 0:
		print("fizz")
	else:
		print(i)