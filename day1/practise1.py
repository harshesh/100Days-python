# Learn print
print("Hello World!")

# Exercise
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

#Learn string manipulation
print("Hello" + " Sasuke")

# Exercise Debuggig

print("Day 1 String Manipulation")
print('String concatination is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# Learn Input function
# input() will get user input in console
# Then print() wil print the word "Hello" and the user input
print("Hello " + input("what is your Name?\n"))

# exercise 
print(len(input("what is your name? ")))

# learn - python variables
name = input("what is your name? ")
print(name)

# exrecise write a program to switches the values stored in the variables a  and b

a = int(input("a : "))
b = int(input("b : "))

# # one way without third varibale
# a = a + b
# b = (a - b)
# a =  str(a - b)
# b  = str(b)

# with third varibale
c = a
a = str(b) 
b = str(c)


print("a = " + a)
print("b = " + b)
