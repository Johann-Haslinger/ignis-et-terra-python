import pygame
from settings import *
from support import *

RED = (255, 0, 0)
PLAYER_WIDTH = 200
PLAYER_HEIGHT = 200


class Player:
  def __init__(self, pos):
    
    self.import_assets()
    print("Initialized Player on:", pos)
    
    
    self.image = self.animations[0][0]
    self.rect = self.image.get_rect(center = 0)


    # Movement
    self.direction = pygame.math.Vector2()
    self.position = pygame.math.Vector2(self.rect)
    self.speed = SPEED

  def import_assets(self): 
    self.animations = {'up': [], 'down': [], 'left': [], 'right': []}
    
    for animation in self.animations.keys():
      filePath = "assets/character/" + animation
      self.animations[animation] = import_folder(filePath)

	

  def attack():
    pass
  
  def use_item():
    pass
  
  def input(self):
    keys = pygame.key.get_pressed()
    
    
    
 
  
  