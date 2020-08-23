from ursina import *
import random
from level import Level
import entities
import tiles
class Game:
    def __init__(self):
        self.walls = list()
        self.doors = list()
        self.empty = list()
        self.enemies = list()
        self.start = None
        self.end = None
        self.player = None

    def load(self, mapa):
        try:
            for item in self.walls:
                item.tile_.remove_node()
            for item in self.doors:
                item.tile_.remove_node()
            for item in self.empty:
                item.tile_.remove_node()
            for item in self.enemies:
                item.tile_.remove_node()
            self.walls.clear()
            self.doors.clear()
            self.empty.clear()
            self.enemies.clear()
            self.start.tile_.remove_node()
            self.end.remove_node()
            self.player.tile_.remove_node()
            self.start = None
            self.end = None
            self.player = None
        except AttributeError:
            pass
        mapa = Level(mapa)
        y = 0
        for line in mapa.board:
            x = 0
            for _tile in line:
                if _tile == "*":
                    tile_ = tiles.Wall(x, y)
                    self.walls.append(tile_)
                if _tile == " ":
                    tile_ = tiles.Empty(x, y)
                    self.empty.append(tile_)
                if _tile == "%":
                    tile_ = tiles.Door(x, y, 2)
                    self.doors.append(tile_)
                if _tile == "X":
                    self.end = Entity(model='cube', color=color.green, position=(x, -y, 0), scale=(1,1,1))
                if _tile == "P":
                    self.start = tiles.Start(x, y)
                if _tile == "@":
                    enemy = entities.Enemy(x, y)
                    self.enemies.append(enemy)
                    tile_ = tiles.Empty(x, y)
                    self.empty.append(tile_)
                x+=1
            y+=1
        self.player = entities.Player(self.start.x, self.start.y)

def input(key):
    if key == "space":
        game.load("map.txt")

def update():
    if held_keys['w']:
        game.player.move("up")
    if held_keys['s']:
        game.player.move("down")
    if held_keys['a']:
        game.player.move("left")
    if held_keys['d']:
        game.player.move("right")
    for item in game.enemies:
        item.move()

game = Game()
app = Ursina()
window.title = 'Labirynth'
window.size = Vec2(800,800)
window.borderless = False
camera.position = (8, -8, -23.5)
app.run()