import logging
import configparser
config = configparser.ConfigParser()
def trypopconfig():
    """
    Tries to populate the config.
    :return: True or False if successful or not respectively.
    """
    # TODO: Continue to populate this with configurable stuff
    if config['GameMechanics']['initialrun'] == 0:
        config['GameMechanics'] = {
            "tickspeed": '60',
            "initialrun": '1'
        }
        logging.info("Generated Config!")
        return True
    else:
        return False
