import sys

sys.path.append('..')
from engine.league.league import *
import pygame


class Projectile:

    def __init__(self, shooter):
        # Set location of projectile to that of shooter
        self.x = shooter.x
        self.y = shooter.y
        # self.rect.x = shooter.rect.x
        # self.rect.y = shooter.rect.y
        # Set delta time
        self.delta = 1024  # BIGGER = FASTER
        # Load image
        self.image = pygame.image.load('./sprites/effects/fire_ball.png').convert_alpha()
        # Set image
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect()
        # Set World size, and make room for collisions
        self.worldSize = (Settings.width, Settings.height)
        self.blocks = pygame.sprite.Group()
        self.collideFunction = pygame.sprite.collide_circle  # can use other shapes
        self.collisions = []
        # Collision sprite
        self.collider = Drawable()
        self.collider.image = pygame.Surface((Settings.tile_size, Settings.tile_size), pygame.SRCALPHA)
        self.collider.rect = self.collider.image.get_rect()

    def shoot_left(self):
        return 0

    def shoot_right(self):
        return 0

    def shoot_up(self):
        return 0

    def shoot_down(self):
        return 0

    def update(self, time):
        return 0

# def shoot_left():
#     return None
#
#
# def shoot_up():
#     return None
#
#
# def shoot_down():
#     return None
#
#
# def shoot_right():
#     return None
