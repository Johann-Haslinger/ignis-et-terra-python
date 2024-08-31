import pygame
from settings import *
from support import *

class Player(pygame.sprite.Sprite):
  def __init__(self, pos, group, collision_sprites):
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
    
    # collision
    self.hitbox = self.rect.copy().inflate((-126,-70))
    self.collision_sprites = collision_sprites

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
  
  def input(self):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
      self.direction.x = -1
      self.direction.y = -0.5
      self.status = ANIMATION.UP
    
    elif keys[pygame.K_DOWN]:
      self.direction.x = 1
      self.direction.y = 0.5
      self.status = ANIMATION.DOWN
    
    elif keys[pygame.K_LEFT]:
      self.direction.x = -1
      self.direction.y = 0.5
      self.status = ANIMATION.LEFT
    
    elif keys[pygame.K_RIGHT]:
      self.direction.x = 1
      self.direction.y = - 0.5
      self.status = ANIMATION.RIGHT
      
    else:
      self.direction.x = 0
      self.direction.y = 0
      
  
  def animate(self, dt):
    self.frame_index += 4 * dt
    if self.frame_index >= len(self.animations[self.status]):
      self.frame_index = 0
      
    self.image = self.animations[self.status][int(self.frame_index)]
		
  def collision(self, direction):
    
    for sprite in self.collision_sprites:
      if hasattr(sprite, 'hitbox'):
        print(f"Player hitbox: {self.hitbox.left}: {self.hitbox.right}, Sprite hitbox: {sprite.hitbox.left}; {sprite.hitbox.right}")
        
        
        
        
        if sprite.hitbox.colliderect(self.hitbox):
          print(f"Collision detected! Player hitbox: {self.hitbox}, Sprite hitbox: {sprite.hitbox}")
              
          if direction == 'horizontal':
            if self.direction.x > 0: # moving right
              self.hitbox.right = sprite.hitbox.left
            if self.direction.x < 0: # moving left
              self.hitbox.left = sprite.hitbox.right
              
            self.rect.centerx = self.hitbox.centerx
            self.position.x = self.hitbox.centerx
          
          if direction == 'vertical':
            if self.direction.y > 0: # moving down
              self.hitbox.bottom = sprite.hitbox.top
            if self.direction.y < 0: # moving up
              self.hitbox.top = sprite.hitbox.bottom
              
            self.rect.centery = self.hitbox.centery
            self.position.y = self.hitbox.centery
						

  def move(self, dt):
    if self.direction.magnitude() > 0:
      self.direction = self.direction.normalize()
    
    self.position.x += self.direction.x * self.speed * dt
    self.hitbox.centerx = round(self.position.x)
    self.rect.centerx = round(self.position.x)
    self.collision('horizontal')
    
    self.position.y += self.direction.y * self.speed * dt
    self.hitbox.centery = round(self.position.y)
    self.rect.centery = round(self.position.y)
    self.collision('vertical')
    
  def get_status(self):
    
     if self.direction.magnitude() == 0:
        new_status_str = self.status.value.split('_')[0] + '_idle'
        self.status = ANIMATION(new_status_str)
	
 
  def update(self, dt):
    self.input()
    self.get_status()
    self.move(dt)
    self.animate(dt)
  