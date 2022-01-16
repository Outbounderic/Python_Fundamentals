from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")

class Guess(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def add_guess(self, state_name, coords):
        self.goto(coords)
        self.write(f"{state_name}", align=ALIGNMENT, font=FONT)