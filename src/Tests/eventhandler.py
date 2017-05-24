import pygame
import logging

logging.basicConfig(level=logging.DEBUG)


def eventhandle():
    pygame.event.pump()
    event = pygame.event.poll()
    if event.type == 0:  # Act. LIKE. A. FILTER.
        pass  # Coo... Coo... *Blushing Intensifies*
    else:
        logging.debug(event.__dict__)
        logging.debug(event)


def isPressed(key, *args):
    """
    :param key: key(in numbers... not the unicode one!)
    :param args: can be(True, False, None)
    :return: If key == None, return True or False Depending on key being pressed.
    """
