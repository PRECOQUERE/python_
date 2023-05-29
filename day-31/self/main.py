BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
current_word = {}
to_learn = {}
#-------------------------DATA SET-------------------------------
try : 
    data = pandas.read_csv("day-31/self/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("day-31/self/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else :
    to_learn = data.to_dict(orient="records")
#-------------------------FUNCTION-------------------------------
def next_card() :
    global current_word, flip_timer

    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(card_fb, image=front_card)
    canvas.itemconfig(card_lang, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)
    
def flip_card() :
    # 전역변수를 수정하지 않을 땐 global 쓰지 않아도 되는 듯
    canvas.itemconfig(card_fb, image=back_card)
    canvas.itemconfig(card_lang, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")

def is_known():
    to_learn.remove(current_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("day-31/self/data/words_to_learn.csv", index=False)
    next_card()
#-------------------------UI SETUP-------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func = flip_card)

front_card = PhotoImage(file="day-31/self/images/card_front.png")
back_card = PhotoImage(file="day-31/self/images/card_back.png")
known_img = PhotoImage(file="day-31/self/images/right.png")
unknown_img = PhotoImage(file="day-31/self/images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_fb = canvas.create_image(400,263, image=front_card)
card_lang = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

known_button = Button(image=known_img, command=is_known)
known_button.grid(row=1, column=0)
unknown_button = Button(image=unknown_img, command=next_card)
unknown_button.grid(row=1, column=1)

next_card()
window.mainloop()