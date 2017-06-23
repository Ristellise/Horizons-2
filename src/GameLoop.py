from src import Utils
from src import Gconstants
import pygame


def init():
    pass


def update():
    for key in pygame.key.get_pressed():
        if key == pygame.QUIT or pygame.K_ESCAPE:
            Utils.safeexit()
        else:
            print(key)


def ForceFreeze():
    # Force Freeze of ticking
    if Gconstants.Freezeticking == 1:
        Gconstants.Freezeticking = 0
    else:
        Gconstants.Freezeticking = 1


def addsprite(sprite, x, y, layer):
    if layer == 0:
        Gconstants.BackgroundSprite.add(sprite)


def draw():
    Gconstants.screen.fill((0, 0, 0))
    Gconstants.BackgroundSprite.draw(Gconstants.screen)
    Gconstants.Shipsprite.draw(Gconstants.screen)
    Gconstants.UISprite.draw(Gconstants.screen)
