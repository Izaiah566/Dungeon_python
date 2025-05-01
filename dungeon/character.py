import pygame
import constants



class Character():
    def __init__(self, x, y):
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)

    def move(self, deltaX, deltaY):
        self.rect.x += deltaX
        self.rect.y += deltaY

    def draw_player(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)
