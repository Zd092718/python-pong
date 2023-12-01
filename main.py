from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SLEEP_TIME = 0.1

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_l.move_up, "w")
screen.onkeypress(paddle_l.move_down, "s")
screen.onkeypress(paddle_r.move_up, "Up")
screen.onkeypress(paddle_r.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(SLEEP_TIME)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        SLEEP_TIME -= 0.005
        if SLEEP_TIME <= 0:
            SLEEP_TIME = 0.02

    # Right miss
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()
        SLEEP_TIME = 0.1

    # Left miss
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()
        SLEEP_TIME = 0.1

    # Detect collision with l_paddle

screen.exitonclick()
