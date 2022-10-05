# 2022/10/05

#hangman_1
import random

word_list = ["ardvark", "baboon", "camel"]
"""
list = random.randint(0,2)
word = word_list[list]

Alpha = input("Guess a letter: ")

for i in word:
    if i == Alpha :
        print("Right")
    else :
        print("Wrong")
"""

#hangman_2
chosen_word = random.choice(word_list)
display = []
death = 0

for i in chosen_word:
    display += "_"
print(display)

while (death < 5):
    letter = input("Guess a letter: ").lower()
    count = 0
    answer = 0

    for i in chosen_word:
        if i == letter:
            display[count] = letter
            answer += 1
        count += 1
    print(display)

    if answer == 0 :
        death += 1