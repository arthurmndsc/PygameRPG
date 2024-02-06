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

        self.x_chage = 0
        self.y_chage = 0
        
        self.facing = 'down'

        self.image = pygame.Surface([sellf.width, self.height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        def update(self):
      	  self.moviment() 

        self.rect.x += self.x_chage
        self.rect.y += self.y_chage
        

        self.x_chage = 0
        self.y_chage = 0

        def moviment(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
            self.x_chage -=3
            self.facing = 'left'
            if keys[pygame.K_RIGHT]:
            self.x_chage += PLAYER_SPEED
            self.facing = 'right'
            self.facing = 'left'
            if keys[pygame.K_UP]:
            self.y_chage = PLAYER_SPEED
            self.facing = 'up'
            if keys[pygame.K_DONW]:
            self.y_chage += PLAYER_SPEED
            self.facing = 'down'