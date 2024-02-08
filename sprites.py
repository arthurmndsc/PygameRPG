import pygame
from config import *
import math
import random

class Spritetessheet:
    def __init__(self,game, x, y):
        self.sheet = pygame.image.load(file).convert()

        def get_sprite(self, x, y, width, height):
            sprite = pygame.Surface([width, height])
            sprite.blit(self.sheet, (0,0), (x, y, width,  height))
            sprite.set_colorkey(BLACK)
            return sprite

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
        self.image.block(RED)

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
            image.facing = self.game.character_springtessheet.get_sprite(3, 2, self.width, self.height)
    self.game = game
    self._layer = BLOCK_LAYER
    self.grups = self.game.all_sprites, self.game.game.blocks
    pygame.sprite.Sprite._init_(self, self.grups)

    self.x = x * TITLESIZE
    self.y = y * TITLESIZE
    self.width = TITLESIZE
    self.height = TITLESIZE

    self.image = self.game.terrain_springtessheet.get_sprite(960, 448, self.width,  self.height)

    self.rect = self.image.get_rect()
    self.rect.x = self.x
    self.rect.y = self.y

class Ground(pygame.sprite.Sprite):
   def __init__(self,  game, x, y):
    self game = game
    self._layer = GROND_LAYER
    self.groups = self.game.all_sprites
    pygame.sprite.Sprite__init__(self, self.grups)

    self.x = x * TITLESIZE
    self.y = y * TITLESIZE
    self.width = TITLESIZE
    self.height = TITLESIZE

    self.image = self.game.terrain_springtessheet.get_sprite(64, 352, self.width, self.height)

    self.rect = self.image.get_rect()
    selfrect.x = self.x
    selfrect.y = self.y