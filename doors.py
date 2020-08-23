import * from tile
class Door(Tile):
    def __init__(self, timer = 2):
        self.color = "orange"
        self.enabed = True
        self.timer = timer