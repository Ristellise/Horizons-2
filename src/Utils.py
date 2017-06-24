import traceback
import pygame
import sys
import logging



def panic():
    """
    Panic Routine used to crash the game if it is unintended.
    :return: Nothing 
    """
    print("Horizons 2 Has encoundered a Serious Error and must shutdown!")
    print("-------------------------------------------------------------------------")
    traceback.print_stack()
    print("-------------------------------------------------------------------------")
    import sys
    sys.exit("Horizons 2 Panicked.")


def safeexit():
    """
    Exits The Game Safely
    """
    pygame.quit()
    sys.exit(0)


def log(level, module=None, *args):
    # Thanks to scroyall on Game Dev discord :)
    """
    LoggerUtility
    :param module: from which module?
    :param level: 0,1,2,3 (Debug,Info,warn,Critical) Respectively
    :param args: message
    :return:
    """
    stringargs = map(str, args)
    argsstring = ' '.join(stringargs)
    if module is None:
        if level == 0:
            logging.debug(argsstring)
        elif level == 1:
            logging.info(argsstring)
        elif level == 2:
            logging.warning(argsstring)
        else:
            logging.critical(argsstring)
    else:
        if level == 0:
            logging.debug(module + ': ' + argsstring)
        elif level == 1:
            logging.info(module + ': ' + argsstring)
        elif level == 2:
            logging.warning(module + ': ' + argsstring)
        else:
            logging.critical(module + ': ' + argsstring)
