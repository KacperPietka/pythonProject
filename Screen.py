import pygame

class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((width, height))