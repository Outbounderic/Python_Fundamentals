from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

def new_random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=flash_card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=flash_card_back)

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
flash_card_front = PhotoImage(file="./images/card_front.png")
flash_card_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=flash_card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=new_random_word)
wrong_button.grid(row=1, column=0)

right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=new_random_word)
right_button.grid(row=1, column=1)

new_random_word()


window.mainloop()