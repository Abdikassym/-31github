from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
  tim.forward(10)

def move_backward():
  tim.backward(10)

def clear_the_board():
  tim.clear()
  tim.penup()
  tim.goto(0, 0)
  tim.pendown()
  tim.setheading(0)

def turn_right():
  tim.right(5)

def turn_left():
  tim.left(5)

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='c', fun=clear_the_board)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='a', fun=turn_left)

screen.exitonclick
