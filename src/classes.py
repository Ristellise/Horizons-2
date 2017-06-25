import os

import pygame
import pygame.freetype

from src import Gconstants, Utils


class Generic:
    """
    Generic BaseClass
    Does nothing on it's own
    Extend it!
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


class image(Generic):
    """
    Image Base
    Extended from Generic
    """

    def __init__(self, x, y, selfimage):
        """

        :param x: x coord
        :param y: y coord
        :param selfimage: image file
        """
        super().__init__(x, y)
        self.image = pygame.image.load(selfimage)
        self.size = image.get_size()
        print(self.size)
        self.rect = image.get_size()

    def draw(self, canvas):
        canvas.blit(self.image, (self.x, self.y))

    def overlaps(self, otherrect):
        return otherrect.colliderect(pygame.Rect(self.x, self.y, self.h, self.w))


class text(Generic):
    def __init__(self, selftext, x, y, color, aa):
        super().__init__(x, y)
        self.color = color
        self.antialias = aa
        self.text = selftext

    def draw(self, canvas):
        print(self.color, self.antialias, self.text)
        if Gconstants.Font is None:
            print('font is none!')
        render = Gconstants.Font.render(self.text, self.antialias, pygame.Color(self.color),
                                        pygame.Color(255, 255, 255))
        canvas.blit(render, (self.x, self.y))


# Ship class Extends from image class
class shipclass(image):
    def __init__(self, x, y, selfimage):
        super().__init__(x, y, selfimage)


def setupfont():
    Utils.log(0, 'UI', 'Begin Fontsetup')
    pygame.font.init()
    if Gconstants.Size == 0:
        Gconstants.Font = pygame.font.Font(str(Gconstants.fontfile), 14)
    elif Gconstants.Size == 1:
        Gconstants.Font = pygame.font.Font(str(Gconstants.fontfile), 20)
    elif Gconstants.Size == 2:
        Gconstants.Font = pygame.font.Font(str(Gconstants.fontfile), 24)
    Utils.log(0, 'UI', 'Finished Font Setup!')
