from tkinter import *

FONT_TYPE = ("Arial", 18, "bold")


def button_clicked():
    mile_value = mile_input.get()
    mile_value *= 1.60934
    km_output.config(text=round(mile_value, 1))


window = Tk()
window.title("Mile to KM")
window.minsize(width=100, height=50)
window.config(padx=10, pady=20)

# create input for num and miles label for it
mile_input = Entry(width=20)
mile_input.grid(column=2, row=1)

mile_label = Label(text="Miles", font=FONT_TYPE)
mile_label.grid(column=3, row=1)
# create box comparison string
equal_label = Label(text="is equal to", font=FONT_TYPE)
equal_label.grid(column=1, row=2)
# create output number and km label
km_output = Label(text=0, font=FONT_TYPE)
km_output.grid(column=2, row=2)

km_label = Label(text="KM", font=FONT_TYPE)
km_label.grid(column=3, row=2)
# create calculate button
calculate_button = Button(text="Calculate", font=FONT_TYPE, command=button_clicked)
calculate_button.grid(column=2, row=3)

window.mainloop()
