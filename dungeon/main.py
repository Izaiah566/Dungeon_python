import pygame
import constants
from character import Character

pygame.init()



screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Game")
clock = pygame.time.Clock()

# define character movements
moving_left = False
moving_right = False
moving_up = False
moving_down = False

# Create character
character = Character(100, 100)

# Game Loop
running = True
while running:

    # calculate characters movement delta x and delta y
    deltaX = 0
    deltaY = 0
    if moving_left:
        deltaX -= 5
    if moving_right:
        deltaX += 5
    if moving_up:
        deltaY -= 5
    if moving_down:
        deltaY += 5

    # Update character movements
    character.move(deltaX, deltaY)

    print(deltaX, deltaY)

    # draw character on screen
    character.draw_player(screen)

    # set FPS
    clock.tick(constants.FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keyboard inputs
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            moving_left = True
        elif event.key == pygame.K_RIGHT:
            moving_right = True
        elif event.key == pygame.K_UP:
            moving_up = True
        elif event.key == pygame.K_DOWN:
            moving_down = True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            moving_left = False
        elif event.key == pygame.K_RIGHT:
            moving_right = False
        elif event.key == pygame.K_UP:
            moving_up = False
        elif event.key == pygame.K_DOWN:
            moving_down = False

    pygame.display.update()

pygame.quit()
