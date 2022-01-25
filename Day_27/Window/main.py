from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


def button_clicked():
    string_entry = input.get()
    my_label.config(text=string_entry)


# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()
my_label.grid(column=0, row=0)

my_label["text"] = "New text"
my_label.config(text="New Text")


# Button
button = Button(text="Click Me!", command=button_clicked)
button.grid(column=0, row=1)

# Entry

input = Entry(width=20)
input.get()
input.grid(column=0, row=2)

window.mainloop()
