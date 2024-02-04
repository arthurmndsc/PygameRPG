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

		self.player = Player()

	def update(self):
		
	def draw(self):

	def main(self):

	def game_over(self):

	def intro_screen(self):

