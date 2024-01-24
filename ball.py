from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.hideturtle()
        self.shapesize(1,1)
        self.color("blue")
        self.goto(0,-258)
        self.x = 10
        self.y = 10
        self.showturtle()
        self.speed = .05

    def ball_move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x,new_y)

    def hor_bounce(self):
        self.x *=-1

    def ver_bounce(self):
        self.y *= -1

    def ball_reset(self):
        self.goto(0,-258)

    def ball_speed(self):
        self.speed *= .005
