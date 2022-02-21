from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')


class StateNames(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.color("red")

    def write_state(self, x, y, state):
        self.goto(x, y)
        self.write(state, align=ALIGNMENT, font=FONT)