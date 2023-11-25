from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


start_x = 0
start_y = 0

snake_segments = []

for segment in range(3):
    turtle_segment = Turtle()
    turtle_segment.color('white')
    turtle_segment.shape("square")
    turtle_segment.penup()
    turtle_segment.goto(x=start_x, y=start_y)
    start_x -= 20





















screen.exitonclick()
