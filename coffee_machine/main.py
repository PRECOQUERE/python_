from menu import MENU
import math
import os

clear = lambda:os.system('cls')

# off를 입력하여 종료/ 그전까진 무한루프
# report를 입력 시, 현재 머신 내 재료 용량 표시
# 용량이 충분치 않을 시 "죄송합니다. 현재 우유 or 원두 or 물이 부족합니다."
# 동전 계산하기 돈을 많이 넣었을 시 거스름돈 주기/ 
# 돈이 부족할 시 "죄송합니다. 금액이 충분치 않습니다. 넣으신 금액은 반환됩니다."
# 거스름돈은 소수 2째자리에서 올림
# 라떼/에스프레소/카푸치노 나왔습니다. 맛있게 드세요!

state = {
    "water": 300,
    "coffee": 100,
    "milk" : 200,
    "money": 0
}

def calc_state(coffee) :
    state["water"]  = state["water"] - MENU[coffee]["ingredients"]["water"]
    state["coffee"] = state["coffee"] - MENU[coffee]["ingredients"]["coffee"]
    state["milk"]   = state["milk"] - MENU[coffee]["ingredients"]["milk"]

def report_state():
    print("현재 남은 water은 " + str(state["water"]) + "ml 입니다.")
    print("현재 남은 coffee은 " + str(state["coffee"]) + "g 입니다.")
    print("현재 남은 milk은 " + str(state["milk"]) + "ml 입니다.")


def coffee_order(coffee):
    nis_water   = MENU[coffee]["ingredients"]["water"]
    nis_coffee  = MENU[coffee]["ingredients"]["coffee"]
    nis_milk    = MENU[coffee]["ingredients"]["milk"]

    if nis_water > state["water"] :
        print("죄송합니다. 현재 물이 부족합니다. 나중에 다시 이용해주세요.")
        return "off"
    if nis_coffee > state["coffee"]:
        print("죄송합니다. 현재 원두가 부족합니다. 나중에 다시 이용해주세요.")
        return "off"
    if nis_milk > state["milk"]:
        print("죄송합니다. 현재 우유가 부족합니다.  나중에 다시 이용해주세요.")
        return "off"
    
    calc_state(coffee)
    print(f"{coffee} 나왔습니다. 맛있게 드세요!")

def calc_coin(coffee):
    P = float(input("How many Penny is it? "))
    N = float(input("How many Nickel is it? "))
    D = float(input("How many Dime is it? "))
    Q = float(input("How many Quarter is it? "))
    price = float( MENU[coffee]["cost"])
    cost = math.ceil(P * 0.01 + N * 0.05 + D * 0.1 + Q * 0.25)

    change = cost - price
    if change < 0 :
        print("죄송합니다. 금액이 충분치 않습니다. 넣으신 금액은 반환됩니다.")
        return 0
    if change > 0 :
        print(f"잔돈 {change}가 반환됩니다. 반환구에서 가져가세요.")

    return 1
    

#main
clear()
rs = 1
while(rs > 0):
    guess = input("What would you like? (latte/espresso/cappuccino) ")
    if guess not in MENU :
        if guess == "off" : 
            rs = 0
        elif guess == "report" : 
            report_state()
        else : 
            print("해당 메뉴는 취급하지 않습니다. 다른 음료를 골라주세요.")
        continue        
    else :
        rs = calc_coin(guess)
        if rs == 1: coffee_order(guess) 
