from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    

    count_down(1 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_minute = math.floor(count / 60)
    count_second = count % 60
    if count_second == 0:
        count_second = "00"
    elif len(str(count_second)) == 1:
        count_second = f"0{str(count_second)}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        window.after(1000, count_down, count - 1)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100 ,pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
background_tom = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=background_tom)
timer_text = canvas.create_text(100, 130, text="00.00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)


check_marks = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()






