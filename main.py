import pygame
from sprites import *
from config import *
import sys

class Game:
	def init(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HIGHT))
		self.clock = pygame.Clock()
		self.font = pygame.font.Font('Arial', 32)
		self.running = True

	def new(self):
		# um novo jogo começa
		self.playing = True

		self.all_sprites = pygame.sprite.LayeredUpdates()
		self.blocks = pygame.sprite.LayeredUpdates()
		self.enemies = pygame.sprite.LayeredUpdates()
		self.attacks= pygame.sprite.LayeredUpdates()

		self.player = Player(self,0 .1)

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

	def main(self):
		#game loop
		while self.playing:
			self.events()
            self.update()
            self.draw()
        self.running = False
	def game_over(self):

	def intro_screen(self):

