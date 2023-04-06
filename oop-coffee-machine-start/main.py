from menu import Menu, MenuItem         #주문 받는 기계, 메뉴판
from coffee_maker import CoffeeMaker    #커피 만드는 기계
from money_machine import MoneyMachine  #돈 받는 기계

# 2023/04/06
# 'str' object has no attribute 'ingredients' 오류가 났었음.
# 클래스 선언 순서에 문제가 있었던 걸로 보임.
# 선언 순서에 따라 클래스 속성으로 받아들일 수도 받아들이지 못할 수도 있으니 확인해서 코딩하기
Cashier = MoneyMachine()
Maxim = CoffeeMaker()
Waiter = Menu()

is_on = True

while(is_on) :
    options = Waiter.get_items()
    choice = input(f"What would you like ? ({options}) ")
    if choice == "off" :
        is_on = False        
    elif choice == "report" :
        Maxim.report()
        Cashier.report()
    else :
        drink = Waiter.find_drink(choice)
        if drink:
            if Maxim.is_resource_sufficient(drink) and Cashier.make_payment(drink.cost) :
                Maxim.make_coffee(drink)
            else :
                print("Try again later.")
        else :
            print("Choose another one plz.")


