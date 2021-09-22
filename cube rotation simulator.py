from ursina import *
import time
WIN = Ursina()
cube = Entity(model='cube',texture='white_cube',color=color.white)
Circle = Entity(model='circle',texture='white_circle',color=color.white)

def update():

    cube.rotation_x += 30 * time.dt
    cube.rotation_y += 30 * time.dt
    if held_keys['2']:
        cube.color = color.green
    if held_keys['3']:
        cube.color = color.white

    if held_keys['1']:
        cube.color = color.red
    if held_keys['F6']:
        Circle() == True
        Cube() == False
    if held_keys['4']:
        cube.color = color.black


    for c in range(1,999):
        if held_keys['r']:
            cube.color = color.random_color()
            time.sleep(0.01)

WIN.run()

