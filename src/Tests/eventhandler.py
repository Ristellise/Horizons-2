import pygame
import logging


def eventhandle():
    pygame.event.pump()
    event = pygame.event.poll()
    if event.type == 0:  # Act. LIKE. A. FILTER
        pass  # Coo. Coo.
    else:
        logging.DEBUG(event.dict)


if __name__ == "__Main__":
    logging.basicConfig(level=logging.DEBUG)
