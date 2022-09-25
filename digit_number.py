#2022/09/11
"""
two_digit_number = input("Type a two digit number: ")
length = len(two_digit_number)
print(int(two_digit_number[0]) + int(two_digit_number[length - 1]))
"""
"""
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = int(weight) / float(height) ** 2
print(int(bmi))
"""

age = int(input("What is your current age?"))
age = 90 - age
days = 365 * age
weeks = 52 * age
months = 12 * age

print(f"You have {days} days, {weeks} weeks and {months} months left.")