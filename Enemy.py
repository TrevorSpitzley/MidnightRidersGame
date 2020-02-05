import pygame
import sys
sys.path.append('..')
from engine.league.league import *


class Enemy(Character):

    def __init__(self, z, x, y):
        # Put z first to mimic his character.py and game_objects.py class
        super().__init__(z, x, y)
        self.health = 100 #My Health
        self.lastHit = pygame.time.get_ticks()
        self.delta = 512 #BIGGER = FASTER
        self.x = x
        self.y = y

        #Image
        self.image = pygame.image.load('./sprites/EnemySprite').convert_alpha()
        # Tweaked size
        self.image = pygame.transform.scale(self.image, (48, 48))
        self.rect = self.image.get_rect()

        #World size, and collisions
        self.worldSize = (Settings.width, Settings.height)
        self.blocks = pygame.sprite.Group()
        self.collideFunction = pygame.sprite.collide_circle #can use other shapes
        self.collisions = []

        #collision sprite
        self.collider = Drawable()
        self.collider.image = pygame.Surface((Settings.tile_size, Settings.tile_size), pygame.SRCALPHA)
        self.collider.rect = self.collider.image.get_rect()

    def moveLeft(self, time):
        amount = self.delta * time
        self.x = self.x - amount
        self.update(0)
        while(len(self.collisions) != 0):
            self.x = self.x + amount
            self.update(0)

    def moveRight(self, time):
        return 0


    def moveDown(self, time):
        return 0


    def update(self, time):
        return 0


    def getHit(self, damage):
        now = pygame.time.get_ticks()
        if now - self.lastHit > 1000:
            self.lastHit = self.health - damage
            self.lastHit = now

                                                                                                     75,0-1        Bot

