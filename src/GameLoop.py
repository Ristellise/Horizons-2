from src import Gconstants,Utils
import math,uuid
import pygame
def update():
    if Gconstants.Freezeticking == 1:
        if pygame.key.get_focused():
            Gconstants.Freezeticking = 0
        else:
            Gconstants.Freezeticking = 1
        pass
    else:
        print('Doing Tick...')
    for key in pygame.key.get_pressed():
        if key == pygame.QUIT or pygame.K_ESCAPE:
            Utils.safeexit()
        else:
            print(key)
def addsprite(sprite,x,y,layer):
    # Generate UUID
    id = (str(uuid.uuid4())[:8])
    for sprite in Gconstants.Spritelist:
        if sprite[0] in id:
            #We attempt to redo the list
            addsprite(sprite,x,y,layer)
    Gconstants.Spritelist.append([id,x,y,sprite,layer])
def draw():
    for sprite in Gconstants.Spritelist:
        pygame.sprite.Sprite.
