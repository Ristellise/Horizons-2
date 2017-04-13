from cocos.audio.pygame import mixer
from cocos.director import *
import logging

def QueueTrack(track, channel):
    if mixer.get_init() is not None:
        try:
            if channel is None:
                channel = mixer.find_channel()
            else:
                channel2int = int(channel)
                localchannel = mixer.Channel(channel2int)
                localchannel.queue(track)
        except [ValueError]:
            logging.fatal("Unable to play Sound at: " + channel + " Possibly it cannot be converterd to an INT!")
    else:
        logging.warning("Sound Not initalised! Refusing to play.")

def VolumeChange(volume, channel):
    if mixer.get_init() is not None:
        try:
            if channel is None:
                channel = mixer.find_channel()
            else:
                channel2int = int(channel)
                localchannel = mixer.Channel(channel2int)
                localchannel.set_volume(volume, volume)
        except [ValueError]:
            logging.fatal("Unable to Change Volume at: " + channel + " Possibly it cannot be converterd to an INT!")
    else:
        logging.warning("Sound Not initalised! Refusing to play.")

def init():
    director.init()
    director.show_FPS = True
    mixer.init()
    VolumeChange(50, 1)
    QueueTrack("Sounds/demo.mp3", 1)
init()