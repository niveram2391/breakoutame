from turtle import Turtle


class Score(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.life = 3
        self.goto(position)
        self.color("white")
        self.write(f"Score:{self.score} Lives:{self.life}", align="right", font=("Arial", 18, "normal"))
        self.hideturtle()

    def lose_life(self):
        self.life -=1

    def inc_score(self,points):
        self.score += points
    def update_score(self):

        self.clear()
        self.write(f"Score:{self.score} Lives:{self.life}",align ="right", font=("Arial",18,"normal"))



    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write(f"Game Over. Your Score {self.score}", align="center", font=("Arial", 18, "normal"))

    def win(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"You Win. Your Score {self.score}", align="center", font=("Arial", 18, "normal"))
