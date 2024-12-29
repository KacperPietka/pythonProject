import pygame
from Player import Shiba
from Screen import Screen
from Obstacles import Rectangles

pygame.init()
player = Shiba()
screen = Screen(800, 533)
rectangle = Rectangles()

class Game:
    def __init__(self):
        self.run = True