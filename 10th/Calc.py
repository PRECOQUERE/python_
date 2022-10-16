#2022/10/16
#Add
from logo import logo

def add(n1, n2) :
    return n1 + n2

#Substract
def subtract(n1, n2):
    return n1 - n2
 
#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    if n1 == 0 :
        return 0
    if n2 == 0 :
        return n1
    
    return n1 / n2

def calculation():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    return num1

operations = {
        "+" : add, 
        "-" : subtract, 
        "*" : multiply,
        "/" : divide
        }

print(logo)
num1 = float(input("What's the first number?: "))
for symbol in operations:
    print(symbol)

on_off = True
while(on_off):
    symbol_chosen = input("Pick an operation : ")
    num2 = float(input("What's the next number?: "))
    calculate_func = operations[symbol_chosen]
    answer = calculate_func(num1, num2)
    
    print(f"{num1} {symbol_chosen} {num2} = {answer}")

    on_off_input = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation.: ")
    if on_off_input == "n":
        num1 = calculation()
    elif on_off_input == "y" :
        on_off = True   
        num1 = answer
    else:
        on_off = False