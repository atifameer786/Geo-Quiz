import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


def runyourgame():
    screen = Screen()
    screen.setup(width=1000, height=600)
    screen.bgcolor('black')
    screen.title('PONG GAME')
    screen.tracer(0)


    l_paddle = Paddle((-450, 0))
    r_paddle = Paddle((450, 0))
    ball = Ball()
    scoreboard = Scoreboard()


    screen.listen()
    screen.onkey(r_paddle.go_up, 'Up')
    screen.onkey(r_paddle.go_down, 'Down')
    screen.onkey(l_paddle.go_up, 'w')
    screen.onkey(l_paddle.go_down, 's')


    is_game_on = True
    while is_game_on:

        time.sleep(ball.move_speed)
        turtle.update()
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < - 280:
            ball.y_bounce()

        if ball.distance(r_paddle) < 50 and ball.xcor() > 420:
            ball.x_bounce()

        if ball.distance(l_paddle) < 50 and ball.xcor() < -420:
            ball.x_bounce()

        if ball.xcor() > 480:
            ball.reset_position()
            scoreboard.l_point()

        if ball.xcor() < -480:
            ball.reset_position()
            scoreboard.r_point()


    screen.exitonclick()