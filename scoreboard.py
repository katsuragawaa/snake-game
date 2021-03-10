from turtle import Turtle

ALIGN = 'center'
FONT = ('BankGothic Lt BT', 16, 'normal')

class Scoreboard(Turtle) :


    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color('white')
        self.goto(0, 240)
        self.update()
        self.hideturtle()


    def update(self) :
        self.write(f'Score: {self.score}', align=ALIGN, font=FONT)


    def score_increase(self) :
        self.score += 1
        self.clear()
        self.update()


    def game_over(self) :
        self.penup()
        self.color('white')
        self.goto(0, 0)
        self.write('Game Over', align=ALIGN, font=FONT)
        self.hideturtle() 