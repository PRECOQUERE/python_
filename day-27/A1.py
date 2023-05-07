import tkinter
# 모듈이 하나일 경우 from tkinter import * // 이상일 경우엔 모듈 구분이 어려워져서 비추천
window = tkinter.Tk()
window.title("MY FIRST GUI PROGRAM")
window.minsize(500, 300)
window.config(padx=100, pady=100)
#LABEL
my_label = tkinter.Label(text="I AM A LABEL", font=("Arial", 24, "bold"))
my_label["text"] = "It's my space"
my_label.config(text="No, it's mine")
my_label.grid(column=0,row=0)
my_label.config(padx=50, pady=50)

#Button
def button_clicked() :
    print("I got Clicked")
    my_label.config(text=input.get())
button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1,row=1)

button_new = tkinter.Button(text="New Button", command=button_clicked)
button_new.grid(column=2,row=0)

#Entry
input = tkinter.Entry(width=10)
input.grid(column=3,row=2)



window.mainloop()