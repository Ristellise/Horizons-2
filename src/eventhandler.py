import pygame
import logging
from src import Utils
logging.basicConfig(level=logging.DEBUG)

ActiveKey = {}


def eventhandle():
    pygame.event.pump()
    event = pygame.event.poll()
    if event.type == 0:  # Act. LIKE. A. FILTER.
        pass  # Coo... Coo... *Blushing Intensifies*
    elif event.type == 1:
        pass
    elif event.type == 2:  # This is a KeyDown Event
        logging.debug(event)
        eventdict = event.__dict__
        ispressed(eventdict["key"], "add")
    elif event.type == 3:
        logging.debug(event)
        eventdict = event.__dict__
        ispressed(eventdict["key"], "remove")
    elif event.type == 12:
        logging.debug(event)
        Utils.safeexit()
    else:
        logging.debug(event)


def ispressed(key, request):
    """
        :param key: key(in numbers... not the unicode one!)
        :param request: can be(add, remove, None)
        :return: If key == None, return True or False Depending on key being pressed.
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
        return ActiveKey[key]


"""
KeyDown:
DEBUG:root:2
DEBUG:root:{'unicode': 'd', 'key': 100, 'mod': 0, 'scancode': 32}
KeyUp:
DEBUG:root:3
DEBUG:root:{'key': 100, 'mod': 0, 'scancode': 32}
"""
