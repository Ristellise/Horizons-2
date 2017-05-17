import logging
import pygame
from src import Utils
logging.basicConfig(level=logging.INFO)
version = ["0.0.2", "Pre - Alpha"]
versionstring = ' '.join(version)
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

