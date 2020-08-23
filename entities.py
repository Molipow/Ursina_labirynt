from ursina import *
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tile_ = Entity(model='cube', color=color.red, position=(self.x, -self.y, -1), scale=(0.5,0.5,0.5))
        self.direction = "up"
    def move(self):
        if self.direction == "up":
            self.tile_.position += (0, time.dt*1.5, 0)
        if self.direction == "down":
            self.tile_.position -= (0, time.dt*1.5, 0)
        if self.direction == "left":
            self.tile_.position -= (time.dt*1.5, 0, 0)
        if self.direction == "right":
            self.tile_.position += (time.dt*1.5, 0, 0)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tile_ = Entity(model='cube', color=color.blue, position=(self.x, -self.y, -1), scale=(0.5,0.5,0.5))
    def move(self, direction):
        if direction == "up":
            self.tile_.position += (0, time.dt*2, 0)
        if direction == "down":
            self.tile_.position -= (0, time.dt*2, 0)
        if direction == "left":
            self.tile_.position -= (time.dt*2, 0, 0)
        if direction == "right":
            self.tile_.position += (time.dt*2, 0, 0)