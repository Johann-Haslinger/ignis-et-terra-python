import pygame
from settings import *
from player import Player
from sprites import Generic
from pytmx.util_pygame import load_pygame

class Level:
  def __init__(self):
    
    # get the display surface
    self.display_surface = pygame.display.get_surface()
    
    # sprite groups
    self.all_sprites = LayeredSpritesGroup()
    self.collision_sprites = pygame.sprite.Group()
    
    self.setup()
    
    
  
  def setup(self):
    tmx_data = load_pygame('data/map.tmx')
    
    for x, y, surf in tmx_data.get_layer_by_name('Collision').tiles():
      # iso_x = (x - y) * (TILE_SIZE // 2) + (1520 )/ 2
      # iso_y = (x + y) * (TILE_SIZE // 4) - (240 +60 )/ 2
      iso_x = (x - y) * (TILE_SIZE // 2) + 1440 / 2
      iso_y = (x + y) * (TILE_SIZE // 4) - 400 / 2
   
      

      
      new_width = int(surf.get_width() * 2.5)
      new_height = int(surf.get_height() * 2.5)
      scaled_surf = pygame.transform.scale(surf, (new_width, new_height))

      Generic((iso_x, iso_y), scaled_surf, self.collision_sprites)
      # Generic((iso_x, iso_y), scaled_surf, self.all_sprites)

			

    
    self.player = Player(
      pos = (PLAYER_START_X, PLAYER_START_Y),
      group = self.all_sprites, 
      collision_sprites=self.collision_sprites 
    )
    
    Generic(
			pos = (0,0),
			surf = pygame.image.load("assets/world/ground.png").convert_alpha(),
			groups = self.all_sprites,
			z = LAYERS['ground']
		)

  
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

					# anaytics
					# if sprite == player:
					# 	pygame.draw.rect(self.display_surface,'red',offset_rect,5)
					# 	hitbox_rect = player.hitbox.copy()
					# 	hitbox_rect.center = offset_rect.center
					# 	pygame.draw.rect(self.display_surface,'green',hitbox_rect,5)
						# target_pos = offset_rect.center + PLAYER_TOOL_OFFSET[player.status.split('_')[0]]
						# pygame.draw.circle(self.display_surface,'blue',target_pos,5)