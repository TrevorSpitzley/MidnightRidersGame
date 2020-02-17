import pygame
import sys
sys.path.append('..')
from engine.league.league import *


class Enemy(Character):

    def __init__(self, z, x, y):
        # Put z first to mimic his character.py and game_objects.py class
        super().__init__(z, x, y)
        # My Health
        self.health = 100
        self.lastHit = pygame.time.get_ticks()
        # BIGGER = FASTER
        self.delta = (128 * 3)
        self.x = x
        self.y = y
        self.move_count = 0
        self._layer = 50

        # Image
        self.image = pygame.image.load('./sprites/EnemySprite/zombie.png').convert_alpha()
        # Tweaked size
        self.image = pygame.transform.scale(self.image, (24, 36))
        self.rect = self.image.get_rect()

        # World size, and collisions
        self.worldSize = (Settings.width, Settings.height)
        self.blocks = pygame.sprite.Group()
        self.collideFunction = pygame.sprite.collide_circle # can use other shapes
        self.collisions = []

        # collision sprite
        self.collider = Drawable()
        self.collider.image = pygame.Surface((Settings.tile_size, Settings.tile_size), pygame.SRCALPHA)
        self.collider.rect = self.collider.image.get_rect()

    def move(self, time):
        amount = self.delta * time
        if self.move_count == 3:
            # move up
            self.y = self.y - amount
            self.move_count = 0
            return

        if self.move_count == 2:
            # move left
            self.x = self.x - amount
            self.move_count += 1

        if self.move_count == 1:
            # move down
            self.y = self.y + amount
            self.move_count += 1

        if self.move_count == 0:
            # move right
            self.x = self.x + amount
            self.move_count += 1

    # def moveLeft(self, time):
    #     amount = self.delta * time
    #     self.x = self.x - amount
    #     self.update(0)
    #     while(len(self.collisions) != 0):
    #         self.x = self.x + amount
    #         self.update(0)
    #
    # def moveRight(self, time):
    #     return 0
    #
    # def moveDown(self, time):
    #     return 0

    def update(self, time):
        self.rect.x = self.x
        self.rect.y = self.y
        self.collisions = []
        for sprite in self.blocks:
            self.collider.rect.x = sprite.x
            self.collider.rect.y = sprite.y
            if pygame.sprite.collide_rect(self, self.collider):
                self.collisions.append(sprite)

    def getHit(self):
        now = pygame.time.get_ticks()
        if now - self.lastHit > 1000:
            self.lastHit = self.health - 10
            self.lastHit = now
            if self.health == 0:
                self.kill()
                self.image = pygame.image.load('./sprites/EnemySprite/zombie.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, (24, 36))
                self.rect = self.image.get_rect()

