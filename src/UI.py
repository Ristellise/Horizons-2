import pygame.freetype, os
from src import Utils, Gconstants


def setupFont():
    Utils.log(0, str(os.getcwd()), 'UI')
    pygame.freetype.init()
    smallFont = pygame.freetype.Font('\Resources\Fonts\trench.ttf', 14)
    default = pygame.freetype.Font('\Resources\Fonts\trench.ttf', 20)
    largefont = pygame.freetype.Font('\Resources\Fonts\trench.ttf', 24)
    Utils.log(0, 'UI', 'Finished Font Setup!')


def textrender(*args, x, y):
    """
    rendertext to screen
    :param args:
    :return:
    """
    fonttext = pygame.freetype.Font.render_to(args)
    Gconstants.screen.blit(fonttext, (x, y))
