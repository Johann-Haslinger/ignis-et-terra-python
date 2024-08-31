import pygame
from settings import *
from player import Player

PLAYER_START_X = 2
PLAYER_START_Y = 2

class Level:
  def __init__(self):
    
    # get the display surface
    self.display_surface = pygame.display.get_surface()
    
    # sprite groups
    self.all_sprites = LayeredSpritesGroup()
    
    self.setup()
  
  def setup(self):
    self.player = Player(pos = (PLAYER_START_X, PLAYER_START_Y),	group = self.all_sprites )
  
  

  
  def run(self, dt):
    self.display_surface.fill('black')
    self.all_sprites.custom_draw(self.player)
    self.all_sprites.update(dt)
    
	  

class LayeredSpritesGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.offset = pygame.math.Vector2()

	def custom_draw(self, player): 
		self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
		self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2
  
		for layer in LAYERS.values():
			for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
				if sprite.z == layer:
					offset_rect = sprite.rect.copy()
					offset_rect.center -= self.offset
					self.display_surface.blit(sprite.image, offset_rect)

	