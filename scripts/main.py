import pygame, sys
from level import Level
from settings import *

FPS = 60

class Game:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption('Ignis et Terra')
    self.clock = pygame.time.Clock()
    self.level = Level()
   
  def run(self): 
    run = True 
    
    while run:
      for event in pygame.event.get():
        if event.type == pygame.QUIT: 
          run = False
        
      deltaTime = self.clock.tick(FPS) / 1000
      self.level.run(deltaTime)
      pygame.display.update()
        
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
	game = Game()
	game.run()
