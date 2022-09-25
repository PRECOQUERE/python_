#2022/09/12
"""
#팁 계산기
print("Welcome to the tip calculator.")
price = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
 
tip = 1.0 + int(tip_percent) / 100
total = float(price) * tip

price_each = round(total / int(people), 2)
# print( "{:.2f}".format(total / int(people)))
print(f"Each person should pay: ${price_each}")
#----------------------------------------------

#IF 연습
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is a even number")
else:
    print("This is an odd number")
#----------------------------------------------

#롤러코스터 키 검사
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("what is your age? "))
    if age >= 45 and age <= 50:
        price = 0
        print("Elder tickets are free")
    elif age > 18:
        price = 12
        print("Adult tickets are $12.")
    elif age >=12 and age <= 18:
        price = 7
        print("Youth tickets are $7.")
    else:
        price = 5
        print("Child tickets are $5.")
    
    photo = input("Do you want photos?  Y or N ")
    if photo == "Y":
        price += 3
    print(f"Please ${price}")
else:
    print("Sorry, You have to grow taller than 120cm..")
#----------------------------------------------

#BMI 검사
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / height ** 2
if bmi >= 35:
    print(f"Your BMI is {round(bmi)}, you are clinically obese.")
elif bmi >= 30 and bmi < 35:
    print(f"Your BMI is {round(bmi)}, you have obese.")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is {round(bmi)}, you are overweight.")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is {round(bmi)}, you are a normal weight.")
else:
    print(f"Your BMI is {round(bmi)}, you are underweight.")
#----------------------------------------------

#윤년
year = int(input("Which year do yo want to check? "))

yun1 = year % 4
yun2 = year % 100
yun3 = year % 400

if yun1 == 0:
    if yun2 == 0:
        if yun3 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year")
else:
    print("Not Leap year")
"""
#사랑계산기
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()
True_num = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e") + name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")
Love_num = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e") + name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")
total = True_num * 10 + Love_num

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")

