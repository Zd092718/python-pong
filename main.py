from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(paddle_l.move_up, "w")
screen.onkeypress(paddle_l.move_down, "s")
screen.onkeypress(paddle_r.move_up, "Up")
screen.onkeypress(paddle_r.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
