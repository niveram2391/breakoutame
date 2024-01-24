from turtle import Turtle

class Brick():
    def __init__(self):
        self.brick_list = []

    def create_brick(self,position_x,position_y,color):
        brick = Turtle("square")
        brick.hideturtle()
        brick.penup()
        brick.speed("fastest")
        brick.color(color)
        brick.turtlesize(stretch_wid=1, stretch_len=3)
        brick.setposition(position_x,position_y)
        brick.showturtle()
        self.brick_list.append(brick)



