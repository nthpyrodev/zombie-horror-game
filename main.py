from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina(borderless=False)

ground = Entity(model='plane', scale=(10, 1, 10), color=color.green, collider='mesh')

player = FirstPersonController()
player.speed = 5

wall1 = Entity(model='cube', scale=(10, 5, 1), position=(0, 2.5, -5), color=color.rgb32(16, 128, 255), collider='mesh')
wall2 = Entity(model='cube', scale=(10, 5, 1), position=(0, 2.5, 5), color=color.red, collider='mesh')
wall3 = Entity(model='cube', scale=(1, 5, 10), position=(-5, 2.5, 0), color=color.red, collider='mesh')
wall4 = Entity(model='cube', scale=(1, 5, 10), position=(5, 2.5, 0), color=color.red, collider='mesh')


def update():
    

    pass

app.run()
