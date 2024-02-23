import pygame
from config import *
import math

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
		pygame.sprite.Sprite.__init__(self, self.groups)

		self.x = x * TITLESIZE
		self.y = y * TITLESIZE
		self.width = TITLESIZE
		self.height = TITLESIZE

		self.x_chage = 0
		self.y_chage = 0
		
		self.facing = 'down'
		self.animation_loop = 1

		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(RED)

		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y

	def update(self):
		self.moviment()
		# self.animate()

		self.rect.x += self.x_chage
		self.collide_blocks('x')
		self.rect.y += self.y_chage
		self.collide_blocks('y')

		self.x_chage = 0
		self.y_chage = 0

	def moviment(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.x_chage -= PLAYER_SPEED
			self.facing = 'left'

		if keys[pygame.K_RIGHT]:
			self.x_chage += PLAYER_SPEED
			self.facing = 'right'
			self.facing = 'left'

		if keys[pygame.K_UP]:
			self.y_chage -= PLAYER_SPEED
			self.facing = 'up'

		if keys[pygame.K_DOWN]:
			self.y_chage += PLAYER_SPEED
			self.facing = 'down'

	def collide_blocks(self, direction):
		if direction == "x":
			hits =  pygame.sprite.spritecollide(self, self.game.blocks, False)
			if hits:
				if self.y_chage > 0:
					self.rect.y = hits[0].rect.top - self.rect.height
				if self.y_chage < 0:
					self.rect.y = hits[0].rect.bottom

def animate(self):
	down_animations = [self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height),
						   self.game.character_spritesheet.get_sprite(35, 2, self.width, self.height),
						   self.game.character_spritesheet.get_sprite(68, 2, self.width, self.height)]

	up_animations = [self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height),
						self.game.character_spritesheet.get_sprite(35, 34, self.width, self.height),
						self.game.character_spritesheet.get_sprite(68, 34, self.width, self.height)]

	left_animations = [self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height),
						self.game.character_spritesheet.get_sprite(35, 98, self.width, self.height),
						self.game.character_spritesheet.get_sprite(68, 98, self.width, self.height)]

	right_animations = [self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height),
						self.game.character_spritesheet.get_sprite(35, 66, self.width, self.height),
						self.game.character_spritesheet.get_sprite(68, 66, self.width, self.height)]

	if self.facing == "down":
			self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
			if self.x_chage > 0:
				self.rect.x = hits[0].rect.left - self.rect.widths
			if self.y_chage < 0:
				self.rect.x = hits[0].rect.right

	if self.direction == "y":
		hits = pygame         

		self.facing = 'down'
		if self.y_chage == 0:
			self.image.facing = self.game.character_springtessheet.get_sprite(3, 2, self.width, self.height)
	else:
		self.image = self.down_animations[math.floor(self.animation_loop)]
		self.animation_loop += 0.1
		if self.animation_loop >= 3:
			self.animation = 1
	if self.facing == "up":
		if self.x_chage == 0:
			self.image.facing = self.game.character_springtessheet.get_sprite(3, 2, self.width, self.height)
		else:
			self.image = self.left_animations[math.floor(self.animation_loop)]
			if self.animation_loop >= 3:
				self.animation = 1
  
	if self.facing == "left":
		if self.y_chage == 0:
			self.image.facing = self.game.character_springtessheet.get_sprite(3, 2, self.width, self.height)
		else:
			self.image = self.down_animations[math.floor(self.animation_loop)]
			self.animation_loop += 0.1
			if self.animation_loop >= 3:
				self.animation = 1
	if self.facing == "up":
		if self.x_chage == 0:
			self.image.facing = self.game.character_springtessheet.get_sprite(3, 66, self.width, self.height)
		else:
			self.image = self.richt_animation [math.floor(self.animation_loop)]
			if self.animation_loop >= 3:
				self.animation = 1

  
	self.game = game #verificar como essa linha deve funcionar, possivelmente game ali seria Game()
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
		self.game = game
		self._layer = GROND_LAYER
		self.groups = self.game.all_sprites
		pygame.sprite.Sprite__init__(self, self.grups)

		self.x = x * TITLESIZE
		self.y = y * TITLESIZE
		self.width = TITLESIZE
		self.height = TITLESIZE

		self.image = self.game.terrain_springtessheet.get_sprite(64, 352, self.width, self.height)

		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y