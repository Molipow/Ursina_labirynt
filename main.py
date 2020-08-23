from ursina import *
import random
from level import Level
import entities
import tiles
mapa = Level("map.txt")

app = Ursina()

print(mapa.board)

walls = list()
doors = list()
empty = list()
enemies = list()
start = None
end = None

y = 0
for line in mapa.board:
    x = 0
    for _tile in line:
        if _tile == "*":
            tile_ = tiles.Wall(x, y)
            walls.append(tile_)
        if _tile == " ":
            tile_ = tiles.Empty(x, y)
            empty.append(tile_)
        if _tile == "%":
            tile_ = tiles.Door(x, y, 2)
            doors.append(tile_)
        if _tile == "X":
            end = Entity(model='cube', color=color.green, position=((x-10)/2, -(y-8)/2, 0), scale=(0.5,0.5,0.5))
        if _tile == "P":
            start = tiles.Start(x, y)
        if _tile == "@":
            enemy = entities.Enemy(x, y)
            enemies.append(enemy)
            tile_ = tiles.Empty(x, y)
            empty.append(tile_)
        x+=1
    y+=1
      
player = entities.Player(start.x, start.y)

random_generator = random.Random()      

def update():
    pass
# scene.camera.orthographic = True

window.title = 'Labirynth'
window.borderless = False
window.fullscreen = False 
window.exit_button.visible = False
window.size = Vec2(800,800)

app.run()
