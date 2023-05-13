from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw() :
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_let = [random.choice(letters) for _ in range(random.randint(5, 8))]
    password_num = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_sym = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    pw_list = password_let + password_num + password_sym
    random.shuffle(pw_list)
    password = "".join(pw_list)

    pw_entry.delete(0, END)
    pw_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pw() :
    site = web_entry.get()
    email = info_entry.get()
    pw = pw_entry.get()

    if len(site) == 0 or len(email) == 0 or len(pw) == 0 :
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else :
        is_ok = messagebox.askokcancel(title=site, message=f"These are the details entered: \nEmail: {email} "
                            f"\nPassword: {pw} \nIs it ok to save?")
        if is_ok :
            with open('day-29/pw_manager/data.text', mode='a') as file :
                file.write(f'\n{site} | {email} | {pw}')
            web_entry.delete(0, 'end')
            pw_entry.delete(0, 'end')

# ---------------------------- UI SETUP -------------------------------

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

pw_image = PhotoImage(file='day-29/pw_manager/logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=pw_image)
canvas.grid(row=0, column=1)

# Label
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

info_label = Label(text="Email/Username:")
info_label.grid(row=2, column=0)

pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0)

# Entry
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

info_entry = Entry(width=35)
info_entry.grid(row=2, column=1, columnspan=2)
info_entry.insert(0, 'hmin9988@gamil.com')

pw_entry = Entry(width=21)
pw_entry.grid(row=3, column=1)

# Button
pw_button = Button(text="Generate Password", command=generate_pw)
pw_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_pw)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()