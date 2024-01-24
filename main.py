# 8 rows of bricks  color coded
# wall/paddle
# ball
# collision
# score
# decrease the paddle size
# ball
# ball misses te paddle  resets to a start position
# ball speed increases


from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from brick_wall import Brick
from score import Score
import time

COLOR = ['red', 'orange', 'green', 'yellow']


screen = Screen()
# screen.tracer(0)
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=800,height=600)

# create wall
brick = Brick()


def create_wall():
    color_pick = -1
    position_x = 360
    position_y = 280

    for i in range(1,97):
        color = COLOR[color_pick]
        brick.create_brick(position_x, position_y, color)
        position_x -= 65
        if i % 12 == 0:
            position_y -= 30
            position_x = 360
            if i % 24 == 0:
                color_pick += 1


create_wall()

# paddle movement
paddle = Paddle((0,-280))
screen.onkey(paddle.move_right, "Right")
screen.onkey(paddle.move_left, "Left")

ball = Ball()
score = Score((300, -250))
screen.listen()

# ball movement
continue_game = True

while continue_game:
    screen.update()
    ball.ball_move()

    # detect collision with side wall
    if ball.xcor() > 350 or ball.xcor() < -350:
        ball.hor_bounce()

    # detect collision with roof
    if ball.ycor() > 265 :
        ball.ver_bounce()

    # paddle hits ball
    if ball.distance(paddle) <45 and ball.ycor() < -265:
        ball.ver_bounce()

    #paddle miss
    if ball.ycor()< -270:
        ball.hideturtle()
        ball.ball_reset()
        ball.showturtle()
        paddle.reset_paddle((0,-280))
        score.lose_life()
        score.update_score()
        if score.life == 0:
            continue_game = False
            score.game_over()

    for bricks in brick.brick_list:
        if ball.distance(bricks) < 50:
            bricks.penup()
            bricks.goto(5000,5000)
            ball.hor_bounce()
            x_axis_difference = ball.distance(bricks)
            y_axis_difference = ball.distance(bricks)
            if x_axis_difference > y_axis_difference:
                # If the ball ditches at the side of the brick then ball's x-axis will be switched.
                ball.hor_bounce()
            else:
                # If the ball ditches on the top or bottom of the brick then ball's y-axis will be switched.
                ball.hor_bounce()
                ball.ver_bounce()
            if bricks.color()[0] == 'red':
                score.inc_score(7)
                score.update_score()
                ball.ball_speed()
            elif bricks.color()[0] == 'green':
                score.inc_score(3)
                score.update_score()
            elif bricks.color()[0] == 'orange':
                score.inc_score(5)
                score.update_score()
            elif bricks.color()[0] == 'yellow':
                score.inc_score(1)
                score.update_score()
                ball.ball_speed()
            if not brick.brick_list:
                continue_game = False
                score.win()

            brick.brick_list.remove(bricks)









screen.mainloop()