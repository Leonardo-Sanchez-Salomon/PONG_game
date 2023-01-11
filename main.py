from turtle import Screen
from paddle import Paddle
from ball import Ball
from border import Border
from scoreboard import ScoreBoard

import time

scoreboard = ScoreBoard()

border = Border()
ball = Ball()
screen = Screen()
screen.tracer(0)

border.draw()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.screensize(canvwidth=800, canvheight=600, bg="black")
screen.title("PONG")

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.m_speed)
    screen.update()
    ball.move()

    # Collision with top and bottom walls
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_wall()

    # Collisions with paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_paddle()
        print(ball.m_speed)

    if ball.xcor() > 400:
        screen.tracer(0)
        scoreboard.l_point()
        ball.reset()
        screen.update()
        time.sleep(1)

    elif ball.xcor() < -400:
        screen.tracer(0)
        scoreboard.r_point()
        ball.reset()
        screen.update()
        time.sleep(1)


screen.exitonclick()




