
# A program that adds the digits in a 2 digit number




# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

print(int(first_digit) + int(second_digit))






# A program that calculates the Body Mass Index (BMI) from a user's weight and height.

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

weight_float = float(weight)
height_float = float(height)

bmi = int(weight_float / height_float ** 2)
bmi_as_str = str(bmi)
print("Your BMI is" " "+ bmi_as_str)







# A program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_remained = 90 - int(age)

days_remained = age_remained * 365
weeks_remained = age_remained * 52
months_remained = age_remained * 12

print(f"You have {days_remained} days, {weeks_remained} weeks and {months_remained} months left")





# A tip a calculator program

print("Welcome to the tip calculator!")
bill = input("What was the total bill? ")

bill_as_float = float(bill)

tip_percentage = input("How much tip would you like to give? 10, 12 or 15 ")

tip_as_int = int(tip_percentage)
tip_percent_calculated = tip_as_int / 100

actual_tip_amount = bill_as_float * tip_percent_calculated
bill_with_tip = bill_as_float + actual_tip_amount

number_of_people = int(input("How many people to split the bill? "))

every_one_to_pay = bill_with_tip / number_of_people
every_one_to_pay_rounded = f"{every_one_to_pay:.2f}"

print(f"Everyone should pay {every_one_to_pay_rounded}")