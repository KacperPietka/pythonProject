import pygame
import random

Speed = 0.05
class Rectangle:
    rectangles = []
    def __init__(self):
        self.position = [750, 0]
        self.size = [60, 800]
        self.last_image_switch_time = 0
        self.color = (0,123,0)

    def spawn_new_rec(self, screen):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_image_switch_time >= 3000 or len(self.rectangles) == 0:
            new_object = Rectangle()
            hole = Rectangle()
            hole.position[1] = random.randint(20, 400)
            hole.color = (0,0,128)
            hole.size = [60, 120]
            self.last_image_switch_time = current_time

            pygame.draw.rect(screen, self.color,
                             pygame.Rect(new_object.position[0], new_object.position[1], new_object.size[0],
                                         new_object.size[1]))
            pygame.draw.rect(screen, hole.color,
                             pygame.Rect(hole.position[0], hole.position[1], hole.size[0],
                                         hole.size[1]))
            Rectangle.rectangles.append(new_object)
            Rectangle.rectangles.append(hole)
    def update_position(self, screen):
        for rect in Rectangle.rectangles:
            rect.position[0] -= 2
            pygame.draw.rect(screen, rect.color, pygame.Rect(rect.position[0], rect.position[1], rect.size[0], rect.size[1]))
            if rect.position[0] <= rect.size[0]*(-1):
                Rectangle.rectangles = Rectangle.rectangles[1:]
