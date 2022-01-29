from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)
email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)

pass_label = Label(text="Password:", bg="white")
pass_label.grid(column=0, row=3)
pass_entry = Entry(width=32)
pass_entry.grid(column=1, row=3)
pass_button = Button(text="Generate Password")
pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()