import logging
import configparser
config = configparser.ConfigParser()
def addconfig(*args):

def updateconfig(*args):

def configpop():
    addconfig()
def openconfig():
    loaded = 0
    if loaded == 0:
        config.read("config.ini")
        loaded += 1
    else:
        logging.info("config already loaded! not loading...")
