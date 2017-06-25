

import pygame
import os
Resources = [['Ores'], ['energy']]
DoRender = 0
Freezeticking = 0
screenx = 1000
screeny = 500
Exit = False
Shipsprite = []
BackgroundSprite = []
UISprite = []
PlanetRender = []
uifiles = []
screen = pygame.display.set_mode((screenx, screeny))
Size = 0
Font = None
fontfile = (os.getcwd() + '\Resources\Fonts\\trench.ttf')