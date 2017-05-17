import logging
import configparser
config = configparser.ConfigParser()
configfile = "config.ini"
def trypopconfig():
    """
    Tries to populate the config.
    :return: True or False if successful or not respectively.
    """
    # TODO:
    try:
        #  Test for a Valid initial run key.
        config['GameMechanics']['initialrun']
    except KeyError:
        config['GameMechanics'] = {
            "tickspeed": '60',
            "initialrun": '1',
        }
        config['Experimental'] = {
            "VSync": '0',
            "ProcessLock": '5'
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
def getconfig(section, option):
    """
    gets value for specified config.
    :param section: section of config
    :param option: options.
    :return: Value given. Else, Return False.
    """
    try:
        return config.get(section=section, option=option)
    except configparser.NoOptionError:
        return False
