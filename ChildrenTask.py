from turtle import *

class Sprite(Turtle):
    def __init__(self, x, y, step=10, shape='circle', color='black'):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step
        self.points = 0

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def check(self, player):
        dist = self.distance(player.xcor(), player.ycor())
        if dist < 30:
            return True
        else:
            return False

    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))

    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)

player = Sprite(0, -100, 10, 'circle', 'red')

goal = Sprite(0, 100, 10, 'triangle', 'green')

enemy1 = Sprite(-200, 20, 10, 'square', 'orange')
enemy1.set_move(-200, 0, 200, 0)
enemy2 = Sprite(200, -20, 10, 'square', 'orange')
enemy2.set_move(200, 0, -200, 0)

scr = player.getscreen()
scr.listen()
scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_down, 'Down')

player.points = 0
while player.points < 3:
    enemy1.make_step()
    enemy2.make_step()
    if player.check(goal):
        player.points += 1
        player.goto(0, -100)
    if player.check(enemy1) or player.check(enemy2):
        player.hideturtle()
        break