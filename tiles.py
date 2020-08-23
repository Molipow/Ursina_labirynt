from ursina import *

class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = color.red
        self.tile_ = Entity(model='cube', color=self.color, position=(self.x, -self.y,-1))

class Empty:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = color.white
        self.tile_ = Entity(model='cube', color=self.color, position=(self.x, -self.y, 0))
        
class Door:
    def __init__(self, x, y, timer = 2):
        self.x = x
        self.y = y
        self.color = color.orange
        self.enabed = True
        self.timer = timer
        self.tile_ = Entity(model='cube', color=self.color, position=(self.x, -self.y, -1))

class Start:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = color.yellow
        self.tile_ = Entity(model='cube', color=self.color, position=(self.x, -self.y, 0))