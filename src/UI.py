import pygame.freetype, os
from src import Utils, Gconstants


def setupFont():
    Utils.log(0, 'UI', 'Begin Fontsetup')
    pygame.freetype.init()
    smallFont = pygame.freetype.Font(str(os.getcwd()) + '\Resources\Fonts\\trench.ttf', 14)
    default = pygame.freetype.Font(str(os.getcwd()) + '\Resources\Fonts\\trench.ttf', 20)
    largefont = pygame.freetype.Font(str(os.getcwd()) + '\Resources\Fonts\\trench.ttf', 24)
    Utils.log(0, 'UI', 'Finished Font Setup!')


def textrender(text, x, y):
    """
    rendertext to screen
    :param y:
    :param x:
    :param args:
    :return:
    """
    fonttext = pygame.freetype.Font.render_to(text)
    Gconstants.screen.blit(fonttext, (x, y))


def fileuireadrender(file):
    with open(file) as f:
        content = f.readlines()
        f.close()
    for string in content:
        slist = string.split(',')
        if slist[0] == 'text':
            textrender(slist[1], slist[2], slist[3])
