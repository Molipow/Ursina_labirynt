from ursina import *
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._tile = Entity(model='cube', color=color.red, position=((self.x-10)/2, -(self.y-8)/2, -0.2), scale=(0.3,0.3,0.3))
        self.direction = 1

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._tile = Entity(model='cube', color=color.blue, position=((self.x-10)/2, -(self.y-8)/2, -0.2), scale=(0.3,0.3,0.3))