import tkinter

window = tkinter.Tk()
window.title("MY FIRST GUI PROGRAM")
window.minsize(500, 300)

#LABEL
my_label = tkinter.Label(text="I AM A LABEL", font=("Arial", 24, "bold"))
my_label.pack(expand=True)
window.mainloop()