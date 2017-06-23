from src import Utils
from src import Gconstants
import pygame, uuid


def init():
    pass


def update():
    for key in pygame.key.get_pressed():
        if key == pygame.QUIT or pygame.K_ESCAPE:
            Utils.safeexit()
        else:
            print(key)


def forcefreeze():
    # Force Freeze of ticking
    if Gconstants.Freezeticking == 1:
        Gconstants.Freezeticking = 0
    else:
        Gconstants.Freezeticking = 1


def addsprite(sprite, x, y, layer):
    suuid = str(uuid.uuid4())[:8]
    if layer == 0:
        Gconstants.BackgroundSprite.append([suuid, sprite, x, y])
    elif layer == 1:
        Gconstants.
    elif layer == 2:
        Gconstants.Shipsprite.append([suuid, sprite, x, y])
    elif layer == 3:
        Gconstants.UISprite.append([suuid, sprite, x, y])


def draw():
    Gconstants.screen.fill([0, 0, 0])
