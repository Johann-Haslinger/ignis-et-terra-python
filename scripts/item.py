import pygame

class Item():
  def __init__(self, name, amount = 0, selected = False):
    self.name = name
    self.amount = amount
    self.image = pygame.image.load(f"assets/items/{name}.png").convert_alpha()
    self.selected = selected
