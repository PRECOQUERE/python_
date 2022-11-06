import random
import os

from logo import logo
clear = lambda: os.system('cls')

clear()
print(logo)

def difficulty(diffy):
    if diffy == 'easy' :
        return 10
    elif diffy == 'hard':
        return 5

def guess_number():
    return random.randint(1,100)


print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
guess_num = guess_number()
#print(f"Pssst, the correct answer is {guess_num}")
attempt = difficulty(input("Choose a difficulty. Type 'easy' or 'hard': "))

while(1):
    print(f"You have {attempt} remaining to guess the number.")
    user_num = int(input("Make a guess: "))

    if user_num > guess_num :
        print("Too High.")
    elif user_num < guess_num:
        print("Too Low.")
    elif user_num == guess_num:
        print(f"You got it! The answer was {guess_num}")
        break

    attempt -= 1
    if attempt == 0 :
        print(f"You've run out of guesses, you lose. The answer was {guess_num}")
        break
    
    print("Guess again.")