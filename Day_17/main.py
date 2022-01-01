from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("blue", "green")



def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 21):
    draw_shape(shape_side_n)










screen = Screen()
screen.exitonclick()