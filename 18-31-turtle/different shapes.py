from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

angle = 4


def draw_shape(angles):
    corner = 360 // angles
    for i in range(angles):
        timmy.forward(100)
        timmy.right(corner)
    global angle
    angle += 1
    draw_shape(angle)


draw_shape(angle)





screen.exitonclick()
