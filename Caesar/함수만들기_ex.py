#2022/10/10
import math

# 깡통 세기
"""
def paint_calc(height, width, cover) :
    cans_ = math.ceil(height * width / cover)
    print(f"You'll need {cans_} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
"""

#소수 찾기
def prime_checker(number):
    is_prime = True
 
    for i in range(2, number) :
        if number % i == 0 :
            is_prime = False

    if is_prime :
        print("It is prime number")
    else :
        print("It isn't prime number")
        
n = int(input("Check this number: "))
prime_checker(number=n)