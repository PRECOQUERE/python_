from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer() :
    global reps
    reps = 0

    window.after_cancel(timer)
    title_lb.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer() :
    global reps
    reps += 1
    
    work = WORK_MIN * 60
    short_rest = SHORT_BREAK_MIN * 60
    long_rest = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_lb.config(text="Long Break")
        count_down(long_rest)
    elif reps % 2 == 0:
        title_lb.config(text="Short Break")
        count_down(short_rest)
    else :
        title_lb.config(text="Work Time")
        count_down(work)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count) :
    time_min = str(int(count / 60)).zfill(2)
    time_sec = str(count % 60).zfill(2)
    canvas.itemconfig(timer_text, text=f"{time_min}:{time_sec}")

    if count > 0 :
       global timer
       timer =  window.after(1000, count_down, count - 1)
    else :
        start_timer()
        marks = ""
        work_session = reps / 2 
        for _ in range(work_session):
            marks += "✔"
        canvas.itemconfig(timer_text, text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#label
title_lb = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_lb.grid(row=0, column=1)

#CANVAS
tomato_img = PhotoImage(file="day-28/self/tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

#BUTTON
button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset",highlightthickness=0, command=reset_timer)
button_reset.grid(row=2, column=2)

#check_mark
check_mark = Label(text="", bg=YELLOW, fg=GREEN, font=(20))
check_mark.grid(row=2, column=1)

window.mainloop()