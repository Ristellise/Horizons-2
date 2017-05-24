from src.Tests import eventhandler
import sys
import pygame
pygame.init()
Display = pygame.display.set_mode((1600,900))
Shipimage = pygame.image.load_extended('Crusier.png')
ClockFPS = pygame.time.Clock()
while True:
    Display.fill((0, 0, 0))
    eventhandler.eventhandle()
    ClockFPS.tick(60)