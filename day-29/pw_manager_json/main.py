from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password() :
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    rd_letters = [random.choice(letters) for _ in range(random.randint(5, 8))]
    rd_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    rd_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = rd_letters + rd_numbers + rd_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pw() :
    website = site_entry.get()
    userinfo = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email" : userinfo,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 :
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else :
        try :
            with open("day-29/pw_manager_me/data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError :
            with open("day-29/pw_manager_me/data.json", mode="a") as file:
                json.dump(new_data, file, indent=4)
        else :
            data.update(new_data)
            with open("day-29/pw_manager_me/data.json", mode="w") as file :
                json.dump(data, file, indent=4)
        finally:
            site_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- PASSWORD SEARCH ------------------------------- #
def find_password() :
    website = site_entry.get()
    try :
        with open("day-29/pw_manager_me/data.json", mode="r") as file :
            data = json.load(file)         
    except FileNotFoundError :
        messagebox.showinfo(title="Oops", message="No Data File Found")
    else :
        if website in data :
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message= f"Email/Username: {email}\n"
                                                        f"Password: {password}")
            pyperclip.copy(password)   
        else :
            messagebox.showinfo(title="Oops", message="No details for the website exists")

        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

pw_image = PhotoImage(file="day-29/pw_manager_me/logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=pw_image)
canvas.grid(row=0,column=1)

# Label
site_label = Label(text="Website: ")
site_label.grid(row=1, column=0)
user_label = Label(text="Email/Username: ")
user_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Entry
site_entry = Entry(width=21)
site_entry.grid(row=1, column=1)
site_entry.focus()
user_entry = Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "hmin9988@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Button
search_bt = Button(text="Search", width=13, command=find_password)
search_bt.grid(row=1, column=2)
generate_pw_bt = Button(text="Generate Password", command=generate_password)
generate_pw_bt.grid(row=3, column=2)
add_pw_bt = Button(text="Add", width=36, command=add_pw)
add_pw_bt.grid(row=4, column=1, columnspan=2)

window.mainloop()