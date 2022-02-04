from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("./data/french_words.csv")
french_dictionary = {row.French: row.English for (index, row) in data.iterrows()}
french_list = list(french_dictionary.items())
french_list_key = list(french_dictionary.keys())
french_list_val = list(french_dictionary.values())

def new_random_word():
    random_key = random.choice(french_list)
    position = french_list.index(random_key)
    canvas.itemconfig(word, text=f"{french_list_key[position]}")


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0)
flash_card_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=flash_card_front)
language = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=new_random_word)
wrong_button.grid(row=1, column=0)

right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=new_random_word)
right_button.grid(row=1, column=1)

flash_card_back = PhotoImage(file="./images/card_back.png")













window.mainloop()