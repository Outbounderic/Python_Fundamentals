from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=240, height=240, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(120, 120, image=lock_img)
canvas.pack()







window.mainloop()