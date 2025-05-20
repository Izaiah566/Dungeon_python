import pygame
import constants
from character import Character

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Game")

# Create clock for FPS
clock = pygame.time.Clock()

# Define character movements
moving_left = False
moving_right = False
moving_up = False
moving_down = False

# Scale function
def scale_image(image, scale):
    return pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))

# Load character images
character_animations = []
character_types = ["player", "buggy", "chunky", "ghosty", "kibby", "kitty", "muddy"]

animation_types = ["standing", "running"]
animated_player_images = []

for character_type in character_types:
    animation_list = []
    for animation_type in animation_types:
        temp_list = []
        for i in range(4):
            player_image =  pygame.image.load(f"/Users/izaiahharrison/Repos/python_pygame/dungeon/assets/characters/{character_type}/{animation_type}/{i}.png")
            player_image = scale_image(player_image, constants.SCALE)
            temp_list.append(player_image)
        animated_player_images.append(temp_list)
        
    animation_list.append(animation_list)

# Create character
player = Character(100, 100, animated_player_images)

# Game Loop
running = True
while running:

    # Set FPS
    clock.tick(constants.FPS)

    # Clear background
    screen.fill(constants.BACKGROUND_WHITE)

    # Calculate characters movement delta x and delta y
    deltaX = 0
    deltaY = 0
    if moving_left:
        deltaX -= constants.SPEED
    if moving_right:
        deltaX += constants.SPEED
    if moving_up:
        deltaY -= constants.SPEED
    if moving_down:
        deltaY += constants.SPEED

    # Update player movements
    player.move(deltaX, deltaY)

    # Draw player on screen
    player.draw_player(screen)

    # Update player
    player.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keyboard inputs
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
