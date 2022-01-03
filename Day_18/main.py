from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def rotate_right():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def rotate_left():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()

def go_home_tim():
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(rotate_right, "a")
screen.onkey(rotate_left, "d")
screen.onkey(clear, "c")
screen.onkey(go_home_tim, "g")

screen.exitonclick()