import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite):
	def __init__(self, game, x, y):
		self.game = game
		self._layer = PLAYER_LAYER
		self.groups = self.game.all_sprites
		pygame.sprite.Sprite._init_(self, self.grups)

        self.x = x * TITLESIZE
        self.y = y * TITLESIZE
        self.width = TITLESIZE
        self.height = TITLESIZE

        self.image = pygame.Surface([sellf.width, self.height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

      def update(self):
      	  pass