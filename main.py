from ursina import *
import random
from level import Level
import enemy
import tiles
mapa = Level("map.txt")

print(mapa.board)

walls = list()
doors = list()
empty = list()
start = None
end = None

y = 0
for line in mapa.board:
    x = 0
    for _tile in line:
        if _tile == "*":
            tile_ = tiles.Wall(x, y)
            walls.append(tile_)
        if _tile == " " or _tile == "@":
            tile_ = tiles.Empty(x, y)
            empty.append(tile_)
        if _tile == "%":
            tile_ = tiles.Door(x, y, 2)
            doors.append(tile_)
        if _tile == "X":
            end = Entity(model='cube', color=color.green, position=((x-10)/2, -(y-8)/2, 0), scale=(0.5,0.5,0.5))
        if _tile == "P":
            start = Entity(model='cube', color=color.blue, position=((x-10)/2, -(y-8)/2, 0), scale=(0.5,0.5,0.5))
        x+=1
    y+=1
      
random_generator = random.Random()      

def update():
    pass


app = Ursina()
app.run()
