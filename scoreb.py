from turtle import Turtle

FONT = ("Courier", 10, "normal")
ALIGNMENT = 'Center'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        # hides the tracer and the initial turtle shape
        self.hideturtle()
        self.penup()
        self.color("white")
        # moves to a location at the top of the screen
        self.goto(0, 320)
        # runs the update_score method
        self.update_score()

    def update_score(self):
        # writes the variables to the screen. Clear screen was added in here. This is because the game_over method is
        # not being used anymore. this wasn't previously reset because the score stayed in the screen when the game
        # finished
        self.clear()
        with open("high_score.txt", mode="r") as h_score:
            high_score = h_score.read()
        self.write(f"Score: {self.score} High Score: {high_score}", True, align=ALIGNMENT, font=FONT)

    def counter(self):
        self.score += 1
        self.goto(0, 270)
        self.update_score()

    def high_score(self):
        # updating the high score when the current score is higher at the end of the game
        if self.score > self.highscore:
            with open("high_score.txt", mode="w") as h_score:
                h_score.write(f"{self.score}")
        # reset the game score
        self.score = 0
        # reset the position to the center top location. Otherwise, the score will move off screen
        self.goto(0, 270)
        # start the score_update() method all over again
        self.update_score()

