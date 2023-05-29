BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random
current_card = {}
to_learn = {}
#--------------------------------DATA CARD-----------------------------------
try :
    data = pandas.read_csv('day-31/data/word_to_csv.csv', )
except FileNotFoundError :
    original_data = pandas.read_csv('day-31/data/french_words.csv')
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

#--------------------------------FUNCTION -----------------------------------

def next_word() :
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(text_lang, text="French", fill="black")
    canvas.itemconfig(text_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=card_front)    
    flip_timer = window.after(3000, func=flip_timer )

def next_word_right() :
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("day-31/data/word_to_learn.csv", index=False)
    next_word()
    
def show_behind():
    canvas.itemconfig(text_lang, text="English", fill="white")
    canvas.itemconfig(text_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_img, image=card_behind)    
    window.after_cancel()

#--------------------------------UI SETUP------------------------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=show_behind)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="day-31/images/card_front.png")
card_behind = PhotoImage(file="day-31/images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front)
text_lang = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
text_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_img =  PhotoImage(file="day-31/images/wrong.png")
button_right = Button(image=right_img, command=next_word_right)
button_right.grid(row=1, column=0)

wrong_img = PhotoImage(file="day-31/images/right.png")
button_wrong = Button(image=wrong_img, command=next_word)
button_wrong.grid(row=1, column=1)

next_word()

window.mainloop()