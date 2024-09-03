import pygame
from settings import *
from cooldown import Cooldown


INVENTORY_SIZE = (640, 440)
INVENTORY_POSITION = ((SCREEN_WIDTH - INVENTORY_SIZE[0]) / 2, (SCREEN_HEIGHT -  INVENTORY_SIZE[1]) / 2)
BLACK = (0, 0, 0)

class Inventory:
  def __init__(self):
    self.visible = False
    
    self.cool_downs = { 
      "change visibility": Cooldown(200)
    }
  
  def draw(self, screen):
   if self.visible:
      pygame.draw.rect(screen, BLACK, (INVENTORY_POSITION, INVENTORY_SIZE), 0, 10)
  
  def input(self):
    pressed_keys = pygame.key.get_pressed()
    
    if pressed_keys[pygame.K_e] and not self.visible and not self.cool_downs["change visibility"].active:
      self.cool_downs["change visibility"].activate()
      self.visible = True
      
    elif len(pressed_keys) > 0 and self.visible and not self.cool_downs["change visibility"].active:
      self.cool_downs["change visibility"].activate()
      self.visible = False
      
  def update_cooldowns(self):
    for cool_down in self.cool_downs.values():
      cool_down.update()
  
  def update(self, player, screen):
    self.input()
    self.draw(screen)
    self.update_cooldowns()