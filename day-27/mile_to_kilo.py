# 2023/05/07
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=370, height=180)
window.config(padx=20, pady=20, background="white")

# Label
label1 = Label(text="Miles")
label1.config(background="white")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.config(background="white")
label2.grid(row=1, column=0)

label3 = Label(text="Km")
label3.config(background="white")
label3.grid(row=1, column=2)

label4 = Label(text="0")
label4.config(background="white")
label4.grid(row=1, column=1)

# Entry
entry = Entry(width=7)
entry.grid(row=0, column=1)

# Button
def button_calc() :
    mile = float(entry.get())
    km = round(mile * 1.609344)
    label4.config(text=f"{km}")

button = Button(text="Calculate", command=button_calc)
button.grid(row=2, column=1)

window.mainloop()