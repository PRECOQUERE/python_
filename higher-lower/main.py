from game_data import data
from logo import logo, vs
import random
import os
clear = lambda: os.system('cls')

def info(account):
    name = account['name']
    description = account['description']
    country = account['country']

    return f"{name}, a {description}, from {country}."

#format
def format_data():
    data_selected = random.choice(data)
    return data_selected

#answer_check
def answer_check(A, B):
    guess = input("Who has More followers? Type 'A' or 'B': ")
    A = int(A['follower_count'])
    B = int(B['follower_count'])

    if(A > B): 
        max = "A"
    else:
        max = "B"
    if max == guess :
        return True
    else :
        return False

#print_main

#main
count = 0
cp = format_data()
ag = format_data()

clear()
print(logo)
while(1):
    while(cp == ag) :
        ag = format_data()

    print(f"Compare A: {info(cp)}")
    print(vs)
    print(f"Against B: {info(ag)}")

    if(answer_check(cp, ag)):
        count = count + 1
        clear()
        print(logo)
        print(f"You're right! Current score: {count}.")
        cp = ag
    else :
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {count}")
        break