from ursina import *
import random
from level import Level
import enemy
import tile
mapa = Level("map.txt")

print(mapa.board)

grid = list()
y = 0
for line in mapa.board:
    x = 0
    for _tile in line:
        if _tile == "*":
            tile_ = Entity(model='cube', color=color.red, position=((x-10)/2, -(y-8)/2, 0), scale=(0.5,0.5,0.5))
            grid.append(tile_)
        if _tile == " " or _tile == "@":
            tile_ = Entity(model='cube', color=color.white, position=((x-10)/2, -(y-8)/2, 0), scale=(0.5,0.5,0.5))
            grid.append(tile_)
        if _tile == "%":
            tile_ = Entity(model='cube', color=color.orange, position=((x-10)/2, -(y-8)/2, 0), scale=(0.5,0.5,0.5))
            grid.append(tile_)
        if _tile == "X":
            tile_ = Entity(model='cube', color=color.green, position=((x-10)/2, -(y-8)/2, 0), scale=(0.5,0.5,0.5))
            grid.append(tile_)
        if _tile == "P":
            tile_ = Entity(model='cube', color=color.blue, position=((x-10)/2, -(y-8)/2, 0), scale=(0.5,0.5,0.5))
            grid.append(tile_)
        x+=1
    y+=1
      
random_generator = random.Random()      

def update():
    pass


app = Ursina()
app.run()
