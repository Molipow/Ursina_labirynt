from ursina import *

class Wall():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = color.red
        self.tile_ = Entity(model='cube', color=self.color, position=((self.x-10)/2, -(self.y-8)/2, 0), scale=(0.5,0.5,0.5))

class Empty():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = color.white
        self.tile_ = Entity(model='cube', color=self.color, position=((self.x-10)/2, -(self.y-8)/2, 0), scale=(0.5,0.5,0.5))
        
class Door():
    def __init__(self, x, y, timer = 2):
        self.x = x
        self.y = y
        self.color = color.orange
        self.enabed = True
        self.timer = timer
        self.tile_ = Entity(model='cube', color=self.color, position=((self.x-10)/2, -(self.y-8)/2, 0), scale=(0.5,0.5,0.5))