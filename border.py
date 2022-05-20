from turtle import Turtle


class Border(Turtle):
    def __init__(self):
       super(Border, self).__init__()
       self.shape('square')
       self.penup()
       self.color('white')


    def upward(self):
        # self.shape('square')
        # self.penup()
        # self.color('white')
        self.shapesize(stretch_len=72, stretch_wid=1)
        self.goto(x=0, y=370)

    def downward(self):

        self.shapesize(stretch_len=72, stretch_wid=1)
        self.goto(x=0, y=-405)

    def rightward(self):

        self.shapesize(stretch_len=2, stretch_wid=45)
        self.goto(x=700, y=0)

    def leftward(self):

        self.shapesize(stretch_len=2, stretch_wid=45)
        self.goto(x=-705, y=0)



