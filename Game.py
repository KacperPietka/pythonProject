import pygame
from Player import Flappy
from Screen import Screen
from Obstacles import UpperRec
from Obstacles import Rectangle
from Obstacles import LowerRec


class Game:
    def __init__(self):
        self.run = True
        self.player = Flappy()
        self.screen = Screen(800, 533)
        self.rectangle = Rectangle()
        self.upperRec = UpperRec()
        self.lowerRec = LowerRec()

    def game_over(self):
        if self.player.position[1] >= self.screen.height - self.player.height or self.player.position[1] <= 0:
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
            pygame.quit()
            exit()


    def game_loop(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            key = pygame.key.get_pressed()
            self.screen.display.fill((0, 0, 128))

            #self.upperRec.spawn_rec(self.screen.display)
            self.upperRec.draw_obstacles(self.screen.display)
            self.lowerRec.draw_obstacles(self.screen.display)

            self.player.update_flappy_image()
            self.player.display_flappy_image(self.screen.display)

            self.player.update_position(key)

            self.player.falling()

            self.upperRec.update_position()
            self.lowerRec.update_position()

            self.game_over()

            pygame.display.update()

        pygame.quit()