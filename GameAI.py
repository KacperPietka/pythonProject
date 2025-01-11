import pygame
from Player import Flappy
from Screen import Screen
from Obstacles import Rectangle
import math


class Game:
    pygame.init()
    def __init__(self):
        self.run = True
        self.previous_distance = None
        self.player = Flappy()
        self.screen = Screen(800, 600)
        self.rectangle = Rectangle()
        self.points = 0
        self.point_added = False
        self.dead = False
        self.reward = 0
        self.background = (0,0,128)

    def restart(self):
        self.player.position = [10, 200]
        self.player.last_image_switch_time = 0
        self.player.speed = 0.05
        self.player.fall = 2
        self.points = 0
        self.rectangle.factor = 0.02
        self.rectangle.speed = 2
        Rectangle.rectangles = []
        Rectangle.last_image_switch_time = 0

    def points_adder(self):
        for rect in Rectangle.rectangles:
            if self.player.position[0] >= rect.position[0] + rect.size[0] and Rectangle.flappy_went_through == True:
                self.points += 1
                Rectangle.factor += 0.02
                self.reward = 10
                Rectangle.flappy_went_through = False

    def calculate_distance_to_hole(self):
        player_x, player_y = self.player.position
        player_y += self.player.height / 2  # MIDDLE
        for rect in Rectangle.rectangles:
            if rect.color == (0, 0, 128):
                hole_x, hole_y = rect.position
                hole_y += rect.size[1] / 2
                distance_y = abs(hole_y - player_y)
                distance_x = abs(hole_x - player_x)
                distance = math.sqrt(distance_x**2 + distance_y**2)
                return distance
        return None

    def collision(self):
        for rect in Rectangle.rectangles:
            if rect.color == self.background and (self.player.position[1] + self.player.height >= rect.position[1] + rect.size[1] or self.player.position[1] <= rect.position[1]) and (rect.position[0] <= self.player.position[0] + self.player.width <= (rect.position[0] + rect.size[0])):
                self.dead = True
                self.reward = -10
    def display_points(self):
        pygame.font.init()
        font = pygame.font.Font('arial.ttf', 50)
        text = font.render(f"{self.points}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.screen.width - 30, 40))
        self.screen.display.blit(text, text_rect)
        pygame.display.update()

    def play(self, move):
        clock = pygame.time.Clock()
        self.dead = False
        self.reward = 0

        self.screen.display.fill(self.background)
        self.rectangle.spawn_new_rec(self.screen.display)
        self.player.update_position(move)
        self.rectangle.update_position(self.screen.display)
        self.player.update_flappy_image()
        self.player.display_flappy_image(self.screen.display)
        self.collision()
        self.player.falling()
        self.points_adder()
        self.display_points()

        current_distance = self.calculate_distance_to_hole()

        if current_distance is not None:
            if self.previous_distance is not None:
                if current_distance < self.previous_distance:
                    self.reward += 1
                elif current_distance > self.previous_distance:
                    self.reward -= 0.5
            self.previous_distance = current_distance

        if self.player.position[1] >= self.screen.height - self.player.height or self.player.position[1] <= 0:
            self.dead = True
            self.reward = -10

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        clock.tick(60)

        return self.reward, self.dead, self.points
