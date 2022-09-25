#2022.09.25
"""
# 동전 앞 뒷면 맞추기

import random
random_side = random.randint(0,1)

if random_side == '1' :
    print("Heads")
else :
    print("Tails")


# 결제할 사람 고르기
import random

names_string = input("Give me everybody's names, seperated by a comma. \n")
names = names_string.split(", ")

random_name = random.randint(0, len(names) - 1)
print(names[random_name] + " is going to buy the meal today!")


#보물지도
row1 = ["😑","😑","😑"]
row2 = ["😑","😑","😑"]
row3 = ["😑","😑","😑"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
p1 = int(position[1]) - 1
p2 = int(position[0]) - 1
map[p1][p2] = "X"

print(f"{row1}\n{row2}\n{row3}")
"""

#가위바위보 게임

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
selection = [rock, paper, scissors]
finger_you = input("(1)rock, (2)paper, (3)scissors \nWhat do you want? ")
finger_you = int(finger_you) - 1
if finger_you > 2:
    print("Take right number")
else:
    finger_com = random.randint(0,2)

    print("Computer")
    print(selection[finger_com])
    print("You")
    print(selection[finger_you])

    if finger_you == finger_com :
        print("DRAW!")
    else :
        if finger_you == 0 :
            if finger_com == 1 :
                print("You LOSE..")
            elif finger_com == 2:
                print("You Win!!")
        elif finger_you == 1:
            if finger_com == 0:
                print("You Win!!") 
            elif finger_com == 2:
                print("You LOSE..")
        elif finger_you == 2:
            if finger_com == 0:
                print("You LOSE..")
            elif finger_com == 1:
                print("You Win!!") 