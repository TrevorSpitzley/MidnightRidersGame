import pygame
import sys
from engine.league.league import *
import random as rnd
sys.path.append('..')


class Boss(Character):
    spawned = False

    def __init__(self, z, x, y):
        # Put z first to mimic his character.py and game_objects.py class
        super().__init__(z, x, y)
        self.health = 200  # My Health
        self.lastHit = pygame.time.get_ticks()  # Last booboo
        self.delta = (128 * 8)  # BIGGER = FASTER
        self.x = x
        self.y = y
        self._layer = 51
        self.move_count = 0
        # self.rect.x = x
        # self.rect.y = y

        # Image!!!
        self.image = pygame.image.load('./FinalBoss/dark_knight_frames/idle_frames/frame_00_delay-0.14s.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()

        # World size, and collisions
        self.worldSize = (Settings.width, Settings.height)
        self.blocks = pygame.sprite.Group()
        self.collideFunction = pygame.sprite.collide_circle  # can use other shapes
        self.collisions = []

        # collision sprite
        self.collider = Drawable()
        self.collider.image = pygame.Surface([Settings.tile_size, Settings.tile_size], pygame.SRCALPHA)
        self.collider.rect = self.collider.image.get_rect()

    def move(self, time):
        amount = self.delta * time
        if self.health > 0:
            if self.move_count == 6 or self.move_count == 7:
                if self.move_count == 7:
                    # move up
                    self.y = self.y - amount
                    self.move_count = 0
                    return
                else:
                    self.y = self.y - amount
                    self.move_count += 1
            if self.move_count == 4 or self.move_count == 5:
                # move left
                self.x = self.x - amount
                self.move_count += 1

            if self.move_count == 2 or self.move_count == 3:
                # move down
                self.y = self.y + amount
                self.move_count += 1

            if self.move_count == 0 or self.move_count == 1:
                # move right
                self.x = self.x + amount
                self.move_count += 1

    def move_random(self, time):
        amount = self.delta * time
        move_count = rnd.randint(0, 3)
        if self.health > 0:
            if move_count == 3:
                # move up
                self.y = self.y - amount
            if move_count == 2:
                # move left
                self.x = self.x - amount
            if move_count == 1:
                # move down
                self.y = self.y + amount
            if move_count == 0:
                # move right
                self.x = self.x + amount

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
        self.collisions = []
        now = pygame.time.get_ticks()
        if now - self.lastHit > 300 and self.health > 0:
            self.health = self.health - 10
            self.lastHit = now
