import pygame
from Player import Shiba
from Screen import Screen
from Obstacles import Rectangles

pygame.init()
player = Shiba()
screen = Screen(800, 533)
rectangle = Rectangles()

screen.display.fill((0,0,128))

pygame.display.update()

def game_over():
    font = pygame.font.Font('arial.ttf', 32)
    text = font.render('YOU LOST!', True, (0,0,0))
    text_rect = text.get_rect()
    run = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.display.fill((0,0,0))
        screen.display.blit(text, text_rect)

run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    pygame.draw.rect(screen.display, (0,123,0), pygame.Rect(30, 30, 60, 60), 2)
    player.update_position(key)
    if falling:
        player.position[1] += 2
        rectangle.position[0] -= 2
    if player.position[1] >= screen.height - player.height or player.position[1] <= 0:
        game_over()

    screen.display.fill((0,0,128))
    pygame.draw.rect(screen.display, (0, 123, 0), pygame.Rect(rectangle.position[0], rectangle.position[1], rectangle.size[0], rectangle.size[1]))
    player.display(screen.display)

    pygame.display.update()
pygame.quit()