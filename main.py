import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

RIGHT_STARTING_POS = (350, 0)
LEFT_STARTING_POS = (-350, 0)


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(RIGHT_STARTING_POS)
left_paddle = Paddle(LEFT_STARTING_POS)

scoreboard = Scoreboard()
ball = Ball()


screen.update()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


#     detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # detect point for left
    if ball.distance(right_paddle) > 50 and ball.xcor() > 340:
        ball.reset_position()
        scoreboard.l_point()

    # detect point for right
    if ball.distance(left_paddle) > 50 and ball.xcor() < -340:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
