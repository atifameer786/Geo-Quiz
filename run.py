from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from border import Border
import time
from tkinter import *
root = Tk()

def runmygame():
    screen = Screen()
    screen.setup(width=1430, height=900)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)


    borderL = Border()
    borderR = Border()
    borderU = Border()
    borderD = Border()

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()


    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:

        borderU.upward()
        borderD.downward()
        borderL.leftward()
        borderR.rightward()
        screen.update()
        time.sleep(0.1)


        snake.move()

        #Detect collision with food.
        if snake.head.distance(food) < 40:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        #Detect collision with wall.
        if snake.head.xcor() > 675 or snake.head.xcor() < -689 or snake.head.ycor() > 352 or snake.head.ycor() < -360:
            scoreboard.reset()
            game_is_on = False
            scoreboard.game_over()

        #Detect collision with tail.
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 4:
                scoreboard.reset()
                game_is_on = False
                scoreboard.game_over()








    screen.exitonclick()
