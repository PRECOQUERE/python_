BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *

#--------------------------------DATA CARD-----------------------------------


#--------------------------------UI SETUP------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_img = PhotoImage(file="day-31/images/card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_img)
text_lang = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
text_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_img =  PhotoImage(file="day-31/images/wrong.png")
button_right = Button(image=right_img)
button_right.grid(row=1, column=0)

wrong_img = PhotoImage(file="day-31/images/right.png")
button_wrong = Button(image=wrong_img)
button_wrong.grid(row=1, column=1)

window.mainloop()