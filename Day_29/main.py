from email import message
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
            }
        }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Uh oh", message="It appears you forgot to fill out an entry.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():

    website = website_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title="Uh oh", message="It appears you forgot to fill out an entry.")
    else:
        with open("data.json", "r") as data_file:                                                                                                                                       
            data = json.load(data_file)

        if website in data:
            found_data = data[website]
            messagebox.showinfo(title=f"Found {website}", message=f"Email: {found_data['email']} \nPassword: {found_data['password']}")
            pyperclip.copy(found_data['password'])                                                              
        else:
            messagebox.showinfo(title="Not Found", message="No details for the website exist.")                                                                            


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()
search_website_button = Button(text="Search", width=15, command=find_password, highlightthickness=0)
search_website_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)
email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(0, "eric@notrealgmail.com")

pass_label = Label(text="Password:", bg="white")
pass_label.grid(column=0, row=3)
pass_entry = Entry(width=32)
pass_entry.grid(column=1, row=3, sticky="w")
pass_button = Button(text="Generate Password", command=generate_password, highlightthickness=0)
pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save, highlightthickness=0)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")


window.mainloop()