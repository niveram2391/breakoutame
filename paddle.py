from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.turtlesize(stretch_wid=1, stretch_len=4)
        self.hideturtle()
        self.goto(position)
        self.showturtle()

    def move_right(self):

        if self.xcor() < 350:
            self.forward(20)

    def move_left(self):

        if self.xcor() > - 350:
            self.backward(20)

    def reset_paddle(self, position):
        self.goto(position)