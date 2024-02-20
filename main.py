import pygame
from sprites import *
from config import *
import sys

class Game:
	def init(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HIGHT))
		self.clock = pygame.Clock()
		self.running = True

        self.character_spritesheet = Spritesheet('img/Protect.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')

		def createTitlemap(self):
			for i, row in enumerate(Titlemap)
              for j, collumn in enumerate(row):
              	Ground(self, j, i)
              	if collumn == "B":
              		block(self, j, i)
              	if collumn == "P":
              		player(self, j, i)

			      print(i, row)
	def new(self):
         createTitlemap
		# um novo jogo começa
		self.playing = True

		self.all_sprites = pygame.sprite.LayeredUpdates()
		self.blocks = pygame.sprite.LayeredUpdates()
		self.enemies = pygame.sprite.LayeredUpdates()
		self.attacks= pygame.sprite.LayeredUpdates()

        self.createTitlemap()

		def events(self):
        # game loop evets
        for event in pygame.event.get():
        	if event.type == pygame.QUIT:
        		self.playing = False
        		self.running = False
        
	def update(self):
		# game loop updates
        self.all_sprites.update()
        
	def draw(self):
      #game loop draw
      self.screen.fill(BLACK)
      self.all_sprites.draw(self.screen)
      self.clock.tick(FPS)
      pygame.display.update()

	def main(self):
		#game loop
	while self.playing:
			self.events()
            self.update()
            self.draw()
        self.running = False
	def game_over(self):
           pass

	def intro_screen(self):
           pass

    g = Game()
    g.intro_screen()
    g.new()
    while g.running:
          g.main()
          g.game_over()
         
          pygame.quit()
          sys.exit()  
        
        




