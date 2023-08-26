# Printing

print("Day 1 - String Manipulation")
print("String Concatenation is done with the '+' sign.")
print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n."))





#  A program that prints the number of characters in a user's name

name = input ("Hello, What's your name? " )
length = len(name)
print("The number of characters in your name is ", length)





#  A program that switches values stored in the variable a and b

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c = a
a = b
b = c
#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)





#  A band name generator program

print("Welcome to the Band Name Generator !")
city = input("What's the name of the city you grew up in ? \n")
pet = input("What's you pet's name ? \n")
print("Your band name could be", city + " " + pet)