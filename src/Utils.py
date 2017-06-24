import traceback
import pygame
import sys
import logging
logging.basicConfig(filename='latest.log', level=logging.INFO)
Utilslogger = logging.getLogger()
handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.DEBUG)
Utilslogger.addHandler(handler)
Utilslogger.setLevel(logging.DEBUG)

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
    argsstring = ' '.join(map(str, args))
    if module is None:
        if level == 0:
            Utilslogger.debug(argsstring)
        elif level == 1:
            Utilslogger.info(argsstring)
        elif level == 2:
            Utilslogger.warning(argsstring)
        else:
            Utilslogger.critical(argsstring)
    else:
        if level == 0:
            Utilslogger.debug(module + ': ' + argsstring)
        elif level == 1:
            Utilslogger.info(module + ': ' + argsstring)
        elif level == 2:
            Utilslogger.warning(module + ': ' + argsstring)
        else:
            Utilslogger.critical(module + ': ' + argsstring)
