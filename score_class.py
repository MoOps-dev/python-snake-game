from turtle import Turtle


class Score(Turtle):
    """Score class will handle score and highscore registration/loading"""
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt", "r") as file:
            self.highest_score = file.read()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x = 0 , y = 260)
        self.write(f"Score: {self.score} - Highest Score: {self.highest_score}", False, "center",
                   ("Courier", 18, "normal"))

    def increase_score(self):
        """Increases the score and writes it on the screen"""
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} - Highest Score: {self.highest_score}", False, "center", ("Courier", 18, "normal"))

    def game_over(self):
        """Resets the current score and save the highest score if score is higher than it"""
        if int(self.highest_score) < self.score:
            with open("score.txt", "w") as file:
                file.write(str(self.score))
            self.highest_score = self.score
        self.score = 0
        self.clear()

        self.write(f"Score: {self.score} - Highest Score: {self.highest_score}", False, "center",("Courier", 18, "normal"))
