import tkinter
# 모듈이 하나일 경우 from tkinter import * // 이상일 경우엔 모듈 구분이 어려워져서 비추천
window = tkinter.Tk()
window.title("MY FIRST GUI PROGRAM")
window.minsize(500, 300)

#LABEL
my_label = tkinter.Label(text="I AM A LABEL", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "It's my space"
my_label.config(text="No, it's mine")
my_label.place(x=100, y=0)
#Button
def button_clicked() :
    print("I got Clicked")
    my_label.config(text=input.get())

button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

#Entry
input = tkinter.Entry(width=10)
input.pack()



window.mainloop()