import pygame
from Player import Flappy
from Screen import Screen
from Obstacles import Rectangle
import Obstacles


class Game:
    def __init__(self):
        self.run = True
        self.player = Flappy()
        self.screen = Screen(800, 533)
        self.rectangle = Rectangle()
        self.points = 0
        self.background = (0,0,128)
    def game_over(self):
        self.reward = -10
        pygame.font.init()
        self.screen.display.fill((0, 0, 0))
        font = pygame.font.Font('arial.ttf', 64)
        text = font.render('YOU LOST!', True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.screen.width // 2, self.screen.height // 2))
        self.screen.display.blit(text, text_rect)
        pygame.display.update()
        #key = pygame.key.get_pressed()
        #ADD WHILE LOOP FOR A CLICKED 'PLAY AGAIN' BUTTON
        pygame.time.wait(2000)
        exit()

    def points_adder(self):
        for rect in Rectangle.rectangles:
            if self.player.position[0] <= rect.position[0] + rect.size[0] and Rectangle.flappy_went_through == True:
                Rectangle.factor += 0.02
                self.points += 1
                Rectangle.flappy_went_through = False

    def collision(self):
        for rect in Rectangle.rectangles:
            if rect.color == self.background and (self.player.position[1] + self.player.height >= rect.position[1] + rect.size[1] or self.player.position[1] <= rect.position[1]) and (rect.position[0] <= self.player.position[0] + self.player.width <= (rect.position[0] + rect.size[0])):
                self.game_over()
    def display_points(self):
        pygame.font.init()
        font = pygame.font.Font('arial.ttf', 50)
        text = font.render(f"{self.points}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.screen.width - 30, 40))
        self.screen.display.blit(text, text_rect)
        pygame.display.update()
    def game_loop(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            self.reward = 0
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            key = pygame.key.get_pressed()
            self.screen.display.fill(self.background)

            self.rectangle.spawn_new_rec(self.screen.display)

            self.player.update_position_human_game(key)

            self.rectangle.update_position(self.screen.display)

            self.player.update_flappy_image()
            self.player.display_flappy_image(self.screen.display)

            self.collision()

            self.player.falling()
            self.points_adder()
            self.display_points()

            if self.player.position[1] >= self.screen.height - self.player.height or self.player.position[1] <= 0:
                self.game_over()
                run = False

            pygame.display.update()
        pygame.quit()


game = Game()
game.game_loop()