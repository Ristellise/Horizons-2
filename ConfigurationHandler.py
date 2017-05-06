import logging
import configparser
config = configparser.ConfigParser()
configfile = "config.ini"
def trypopconfig():
    """
    Tries to populate the config.
    :return: True or False if successful or not respectively.
    """
    # TODO: Continue to populate this with configurable stuff
    try:
        if config['GameMechanics']['initialrun'] == 0:
            pass
        else:
            config['GameMechanics'] = {
                "tickspeed": '60',
                "initialrun": '1'
            }
    except KeyError:
        config['GameMechanics'] = {
            "tickspeed": '60',
            "initialrun": '1'
        }
        logging.info("Generated Config!")
        config.write(configfile)
        return True
    else:
        return False
def loadconfig():
    if not config.read(configfile):
        logging.INFO("Failed Reading file!")
    else:
        config.read(configfile)