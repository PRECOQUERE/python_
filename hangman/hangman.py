# 2022/10/05


import random
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
display = []

# for _ in range(word_length):
#     display += "_"

#hangman_1
"""
list = random.randint(0,2)
word = word_list[list]

Alpha = input("Guess a letter: ")

for i in word:
    if i == Alpha :
        print("Right")
    else :
        print("Wrong")


#hangman_2
chosen_word = random.choice(word_list)
death = 0

# for i in chosen_word:
#     display += "_"
# print(display)
display = []
word_length = len(chosen_word)
for _ in range(len(chosen_word)):
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()

for position in range(word_length):
    if chosen_word[position] == guess:
        display[position] = guess
print(display)
"""

# 2022/10/10
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
already_letter = []
for _ in range(word_length):
    display += "_"

left_life = 7

print(logo)
while(left_life > 0) :
    guess = input("Guess a letter: ").lower()

    if guess in already_letter:
        print("You've already guessed " + guess)
    else:
        if guess not in chosen_word :
            left_life -= 1
            if (left_life == 0) :
                print("You Lose..")
                print(chosen_word)

                break
            else :
                print("You guessed " + guess + ", that's not in the word. You lose a life.")
        
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess :
                display[position] = guess

        if "_" not in display :
            print("You Win!")
            left_life = 0

    already_letter += guess

    if left_life > 0:
        print(display)
        print(stages[left_life-1])
