from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=240, height=240, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(72, 120, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1, padx=2, pady=2)
website_entry = Entry(width=43)
website_entry.grid(column=1, row=1, padx=2, pady=2)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2, padx=2, pady=2)
email_entry = Entry(width=43)
email_entry.grid(column=1, row=2, padx=2, pady=2)

pass_label = Label(text="Password:", bg="white")
pass_label.grid(column=0, row=3, padx=2, pady=2)
pass_entry = Entry(width=24)
pass_entry.grid(column=1, row=3, padx=2, pady=2, sticky="w")
pass_button = Button(text="Generate Password", highlightthickness=0)
pass_button.grid(column=1, row=3, sticky="e")

add_button = Button(text="Add", highlightthickness=0, width=36)
add_button.grid(column=1, row=4)


window.mainloop()