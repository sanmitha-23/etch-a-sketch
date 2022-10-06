from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def counter_cw():
    tim.right(10)


def cw():
    tim.left(10)


def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()
    # tim.goto(0.0, 0.0)
    # tim.setheading(0.0)


# w - forwards
# s - backwards
# a - counterclockwise
# d - clockwise
# c - clears screen and goes to default position


screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=counter_cw, key='a')
screen.onkey(fun=cw, key='d')
screen.onkey(fun=clear_screen, key='c')

screen.exitonclick()
