#2022/10/22
import random
import os
from logo import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_cd_com(com_cd) :
    total = 0
    while(total < 17):
        com_cd.append(random.choice(cards))
        total = sum_total(com_cd)
        
def get_cd_you(you_cd) :
    for i in range(1,3) :
        you_cd.append(random.choice(cards))

def get_cd(dex):
    dex.append(random.choice(cards))

def sum_total(who):
    sum = 0
    for x in who:
        sum += x
    
    return sum

def match(you, com) :
    you = sum_total(you)
    com = sum_total(com)

    # 둘 중 하나 이상 21을 초과한 경우
    if com > 21 or you > 21 :
        if com > 21 and you > 21 :
            if com > you :
                print("Opponent went over. You Win!!")
            elif you > com :
                print("You went over. You lose...")
            else:
                print("Draw")
        else :
            if com > you :
                print("Opponent went over. You Win!!")
            elif you > com:
                print("You went over. You lose...")
    # 둘 다 21을 초과하지 않은 경우 
    else :
        if you == com :
            print("Draw")
        elif you > com :
            print("You Win!!")
        else :
            print("You lose...")

while(1) :
    y_n = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    chosen_you = []
    chosen_com = []

    if y_n == 'y' :
        os.system('cls')
        print(logo)

        get_cd_com(chosen_com)
        get_cd_you(chosen_you)

        while(1):
            print(f"    Your cards: {chosen_you} current score: " + str(sum_total(chosen_you)))
            print(f"    Computer's first card: {chosen_com[0]}")

            if sum_total(chosen_you) < 22:
                add_cd = input("Type 'y' to get another card, type 'n' to pass: ")
                if add_cd == 'y':
                    get_cd(chosen_you)
                else :
                    print(f"    ★ Your final cards: {chosen_you}, final score: " + str(sum_total(chosen_you)))
                    print(f"    ★ Computer's final hand: {chosen_com}, final score: " + str(sum_total(chosen_com)))
                    match(chosen_you, chosen_com)
                    break

            else:
                print(f"    ★ Your final cards: {chosen_you}, final score: " + str(sum_total(chosen_you)))
                print(f"    ★ Computer's final hand: {chosen_com}, final score: " + str(sum_total(chosen_com)))
                match(chosen_you, chosen_com)
                break
    else:
        break
