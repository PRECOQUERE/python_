#2022.09.25
"""
# For문 익히기
fruits = ["Apple", "Peach", "Pear"]

for i in fruits:
    print(i)

# 학생 키 평균 구하기
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)) :
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum_heights = 0
count = 0
for height in student_heights :
    sum_heights += height
    count += 1

avg_heights = round(sum_heights / count)
print(avg_heights)


# 높은 예제 점수
max = 0
student_scores = input("Input a list of student student scores ").split()
for n in range(0, len(student_scores)) :
    student_scores[n] = int(student_scores[n])
print(student_scores)

for num in student_scores :
    if num > max :
        max = num

print(f"The highest score in the class in: {max}")        

for number in range(1,11,3):
    print(number)

total = 0
for num in range(2, 101, 2):
    total += num
print(total)

# 3으로 나눌 수 있으면 Fizz, 5로 나눌 수 있으면 Buzz 둘다면 FizzBuzz
for num in range(1, 101):
    if num % 15 == 0 :
        print("FizzBuzz")
    elif num % 3 == 0 :
        print("Fizz")
    elif num % 5 == 0 :
        print("Buzz")
    else :
        print(num) 

#비밀번호 자동 생성
##ez mode
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like\n"))

pwd = ""
for i in range(0, nr_letters) :
    loc = random.randint(0, len(letters))
    pwd += letters[loc]

for i in range(0, nr_numbers) :
    loc = random.randint(0, len(numbers))
    pwd += numbers[loc]

for i in range(0, nr_symbols) :
    loc = random.randint(0, len(symbols))
    pwd += symbols[loc]

print(pwd)
"""
## Hard mode
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like\n"))

pwd_list = []
total = nr_letters +  nr_numbers + nr_symbols
for i in range(0, nr_letters) :
    pwd_list.append(random.choice(letters))

for i in range(0, nr_numbers) :
    pwd_list.append(random.choice(numbers))

for i in range(0, nr_symbols) :
    pwd_list.append(random.choice(symbols))

random.shuffle(pwd_list)
print(pwd_list)

print("Your password is ", end='')
for i in pwd_list :
    print(i, end='')