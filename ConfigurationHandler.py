import logging
import json

__loadedconfig__ = 0
__localdata = None
__file__ = None
def loadconfig(file):
    if __loadedconfig__ == 1:
        logging.INFO("Loaded config already!")
        return False
    else:
        __file__ = file
        __loadedconfig__ += 1
        return True
def save_config():
    with open(str(__file__)) as file:
        try:
            formdump = json.dump(__localdata,sort_keys=False,indent=4)
            file.write(formdump)
            file.close()
        except Exception:
            logging.CRITICAL("Cannot Write To : " +  str(__file__) + " !")
def load_config():
    with open(str(__file__)) as file:
        try:
            __localdata = file.read()
        except Exception:
            logging.CRITICAL("Cannot Read From : " + str(__file__) + " !")