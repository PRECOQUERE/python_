from menu import Menu, MenuItem         #주문 받는 기계, 메뉴판
from coffee_maker import CoffeeMaker    #커피 만드는 기계
from money_machine import MoneyMachine  #돈 받는 기계

Waiter = Menu()
Maxim = CoffeeMaker()
Cashier = MoneyMachine()

is_on = True

while(is_on) :
    print("What do u want to order?")
    pick_drinks = input(Waiter.get_items() + ' ')
    if Waiter.find_drink(pick_drinks) :
        if Cashier.make_payment(Waiter.find_drink(pick_drinks).cost) :
            if Maxim.is_resource_sufficient(pick_drinks) :
                Maxim.make_coffee(pick_drinks)
            else :
                print("Try again later.")
                break
    else :
        print("Choose another one plz.")