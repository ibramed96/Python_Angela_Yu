# Welcome to the rollercoaster! program version 1.0

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster")
else:
  print("Sorry, you have to grow taller before you can ride")




#   A program that checks an Even and Odd numbers

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
  print("This is an even number")
else:
  print("This is an odd number")





# Welcome to the rollercoaster! program version 2.0

if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("What is your age ? "))
  if age < 5:
    print("Please pay $ 5.0 ")
  elif age <= 18:
    print("Please pay $ 7.0 ")
  else:
    print("Please pay $ 12.0 ")
else:
  print("Sorry you have to grow taller before you can ride the rollercoaster")




#   # A program that calculates the Body Mass Index (BMI) from a user's weight and height version 2.0

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

weight_float = float(weight)
height_float = float(height)

bmi = int(weight_float / height_float ** 2) # in this line you can change 'int' to 'float' and then round it into desired decimal place to get the accurate BMI
bmi_as_str = str(bmi)

if bmi <= 18.5:
  print(f"Your BMI is {bmi_as_str}, you are underweight ! ")
elif bmi <= 25:
  print(f"Your BMI is {bmi_as_str}, you have normal weight ! ")
elif bmi <= 30:
  print(f"Your BMI is {bmi_as_str}, you are overweight ! ")
else:
  print(f"Your BMI is {bmi_as_str}, you are clinically obese ! ")

