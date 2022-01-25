from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New text"
my_label.config(text="New Text")

# Button

def button_clicked():
    print("I got clicked!")
    my_label.config(text="I got clicked!")

button = Button(text="Click Me!", command=button_clicked)
button.pack()











window.mainloop()
