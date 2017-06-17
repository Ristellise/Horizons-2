import pygame
import logging
from src import Utils, Constants

logging.basicConfig(level=logging.DEBUG)

ActiveKey = {}


def eventhandle():
    pygame.event.pump()
    event = pygame.event.poll()
    if event.type == 0:  # Act. LIKE. A. FILTER.
        pass  # Coo... Coo... *Blushing Intensifies*
    elif event.type == 1:
        #Mouse State
        ActiveState = event.__dict__
        if ActiveState >= 2:
            Constants.DoRender = False
        else:
            Constants.DoRender = True
            # We are behind a window... stop rendering.
        print(event)
    elif event.type == 12:
        logging.debug(event)
        Utils.safeexit()
    else:
        print(event)


def ispressed(key=None, request=None):
    """
        :param key: key(in numbers... not the unicode one!)
        :param request: can be(add, remove, None)
        :return: If key == None, return True or False Depending on key being pressed...
                else, just spill out all of activekey contents.
    """
    if request == "add":
        ActiveKey[key] = 1
        logging.debug("Added Key: " + str(key))
    elif request == "remove":
        r = dict(ActiveKey)
        try:
            del r[key]
            logging.debug("Removed Key: " + str(key))
        except KeyError:
            logging.warning("Key not found : " + str(key))
    elif request is None:
        try:
            return ActiveKey[key]
        except KeyError:
            return ActiveKey


"""
KeyDown:
DEBUG:root:2
DEBUG:root:{'unicode': 'd', 'key': 100, 'mod': 0, 'scancode': 32}
KeyUp:
DEBUG:root:3
DEBUG:root:{'key': 100, 'mod': 0, 'scancode': 32}
"""
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((1600,900))
    while True:
        eventhandle()
