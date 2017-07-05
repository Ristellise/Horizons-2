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


class Image(Generic):
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
        # noinspection PyUnresolvedReferences
        # This actually works. but PyCharm goes "NOPE ITS NOT THERE HURR DURR"
        self.image = pygame.image.load(selfimage)
        self.size = self.image.get_size()
        self.rect = self.image.get_size()

    def draw(self, canvas):
        canvas.blit(self.image, (self.x, self.y))


class Text(Generic):
    def __init__(self, selftext, x, y, color, aa):
        super().__init__(x, y)
        self.color = color
        self.antialias = aa
        self.text = selftext

    def draw(self, canvas):
        if Gconstants.Font is None:
            Utils.log(3, 'UI', 'Font Config is none! Check if Font file is loaded at "GConstants.Font"')
        else:
            render = Gconstants.Font.render(self.text, self.antialias, self.color)
            canvas.blit(render, (self.x, self.y))





def setupfont():
    Utils.log(0, 'UI', 'Begin Font setup.')
    pygame.font.init()
    if Gconstants.Size == 0:
        Gconstants.Font = pygame.font.Font(str(Gconstants.fontfile), 14)
    elif Gconstants.Size == 1:
        Gconstants.Font = pygame.font.Font(str(Gconstants.fontfile), 20)
    elif Gconstants.Size == 2:
        Gconstants.Font = pygame.font.Font(str(Gconstants.fontfile), 24)
    Utils.log(0, 'UI', 'Finished Font Setup!')

# Ship class Extends from image class
class Ship(Image):
    def __init__(self, x, y, selfimage):
        super().__init__(x, y, selfimage)
        self.shipporgress = None


    def progress(self,increment):
        if increment:
            if self.shipporgress is None:
                self.shipporgress = 1
            else:
                self.shipporgress += 1
        elif not increment:
            if self.shipporgress == 1:
                self.shipporgress = None


    def draw(self, canvas):
        if self.shipporgress >= 1:
            canvas.
            canvas.blit(self.image, (self.x, self.y))
        else:
            pass
    def states(self):
