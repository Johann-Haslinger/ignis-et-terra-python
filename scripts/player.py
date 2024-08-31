import pygame
from settings import *
from support import *

RED = (255, 0, 0)
PLAYER_WIDTH = 200
PLAYER_HEIGHT = 200


class Player(pygame.sprite.Sprite):
  def __init__(self, pos, group):
    super().__init__(group)
    
    # general setup
    self.import_assets()
    self.status = ANIMATION.DOWN_IDLE
    self.frame_index = 0
    
    self.image = self.animations[self.status][self.frame_index]
    self.rect = self.image.get_rect(center = pos)
    self.z = LAYERS['main']
  
    # movement
    self.direction = pygame.math.Vector2()
    self.position = pygame.math.Vector2(self.rect.center)
    self.speed = SPEED

  def import_assets(self): 
    self.animations = {
      ANIMATION.UP_IDLE: [],
      ANIMATION.DOWN_IDLE: [],
      ANIMATION.LEFT_IDLE: [],
      ANIMATION.RIGHT_IDLE: [],
      ANIMATION.UP: [],
      ANIMATION.DOWN: [],
      ANIMATION.LEFT: [],
      ANIMATION.RIGHT: []
       
    }
   	
    for animation in self.animations:
      filePath = "assets/character/" + animation.value
      self.animations[animation] = import_folder(filePath)


	

  def attack():
    pass
  
  def use_item():
    pass
  
  def input(self):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
      self.direction.y = -1
      self.status = ANIMATION.UP
    
    elif keys[pygame.K_DOWN]:
      self.direction.y = 1
      self.status = ANIMATION.DOWN
    
    else:
      self.direction.y = 0
    
    if keys[pygame.K_LEFT]:
      self.direction.x = -1
      self.status = ANIMATION.LEFT
    
    elif keys[pygame.K_RIGHT]:
      self.direction.x = 1
      self.status = ANIMATION.RIGHT
      
    else:
      self.direction.x = 0
      
  def animate(self, dt):
    self.frame_index += 4 * dt
    if self.frame_index >= len(self.animations[self.status]):
      self.frame_index = 0
      
    self.image = self.animations[self.status][int(self.frame_index)]
		
    
		
      
  def move(self, dt):
    if self.direction.magnitude() > 0:
      self.direction = self.direction.normalize()
    
    self.position.x += self.direction.x * SPEED * dt
    self.position.y += self.direction.y * SPEED * dt
    
  def get_status(self):
      # idle
     if self.direction.magnitude() == 0:
        new_status_str = self.status.value.split('_')[0] + '_idle'
        self.status = ANIMATION(new_status_str)
			

	 
		
	

    
 
  def update(self, dt):
    print("update", dt)
    self.input()
    self.get_status()
    self.move(dt)
    self.animate(dt)
  