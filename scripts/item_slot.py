import pygame
from settings import *

class ItemSlot:
    def __init__(self, position, index):
        self.position = position
        self.item = None
        self.index = index
        self.height = 100 
        self.width = 100

    def draw(self, screen, item):
        if item and item.selected:
            pygame.draw.rect(screen, BLACK, ((
                self.position[0] - 2.5, self.position[1] - 2.5), (105, 105)), 0, 12)
        color = (10, 10, 10) if item else (20, 20, 20)
        pygame.draw.rect(screen, color, (self.position, (self.width, self.height)), 0, 10)

        if item:
            scaled_image = pygame.transform.scale(item.image, (60, 60))
            screen.blit(
                scaled_image, (self.position[0] + 20, self.position[1] + 20))
