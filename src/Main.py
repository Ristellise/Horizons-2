import logging
import pygame
from src import Utils, eventhandler, gameclock, renderqueue

logging.basicConfig(level=logging.INFO)
version = ["0.0.2", "Pre - Alpha"]
versionstring = ' '.join(version)
#Constants For now...
DoRender = 0
Freezeticking = 0
"""
Stepload
Where:
1 (Setup)
2 (Load core Module)
3 (Load Mods)
4 (Mod Interaction)
5 (Cleanup and run game)
"""
print("Starting GalaxyTest Version : " + versionstring)
print("Stepload : 1(Pygame Setup)")
pygame.init()

print("StepLoad : 2")
print("StepLoad : 3")
print("StepLoad : 4")
print("StepLoad : 5")


class Gameloop:
    def __init__(self):
        clock = gameclock.GameClock(update_callback=self.updater(),
                                    frame_callback=self.draw(),
                                    pause_callback=self.pause())

    def run(self):
        while 1:
            if Freezeticking:
                self.pause()
            eventhandler.eventhandle()
            self.clock.tick()

    def updater(self):
        pass

    def draw(self):
        if not DoRender:
            pass
        else:
            for list in renderqueue.renderqueue:
                spritegroup, image, x, y = list
                image =
    def pause(self):
