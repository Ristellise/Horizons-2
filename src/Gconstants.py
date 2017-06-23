import pygame

Resources = [['Ores'], ['energy']]
DoRender = 0
Freezeticking = 0
screenx = 300
screeny = 400
Exit = False
Shipsprite = pygame.sprite.RenderUpdates()
BackgroundSprite = pygame.sprite.RenderUpdates()
UISprite = pygame.sprite.RenderUpdates()
screen = pygame.display.set_mode((screenx, screeny))

