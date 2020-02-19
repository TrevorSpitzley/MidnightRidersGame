import pygame
import sys
from engine.league.league import *
sys.path.append('..')


class Boss(Character):

    def __init__(self, z, x, y):
        # Put z first to mimic his character.py and game_objects.py class
        super().__init__(z, x, y)
        self.health = 200  # My Health
        self.lastHit = pygame.time.get_ticks()  # Last booboo
        self.delta = 128  # BIGGER = FASTER
        self.x = x
        self.y = y
        self._layer = 51
        # self.rect.x = x
        # self.rect.y = y

        # Image!!!
        self.image = pygame.image.load().convert_alpha()
        self.image = pygame.transform.scale(self.image, (36, 36))
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
