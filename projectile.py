import sys

sys.path.append('..')
from engine.league.league import *
import pygame
from pygame import mixer


class Projectile(DUGameObject):

    def __init__(self, shooter, direction):
        super().__init__()
        # Set location of projectile to that of shooter
        self.x = shooter.x + 60
        self.y = shooter.y + 12
        self.rect.x = shooter.rect.x
        self.rect.y = shooter.rect.y
        # Set delta time
        self.delta = 1  # BIGGER = FASTER
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
        self._layer = 50
        self.direction = direction
        self.fire_ball_sound = mixer.Sound()

    def play_sound(self):
        self.fire_ball_sound.play()

    def shoot_left(self, time):
        # Based on timer, move 50 pixels
        self.x = self.x - 50
        self.rect.x = self.rect.x - 50

    def shoot_right(self, time):
        # Based on time, move 50 pixels
        self.x = self.x + 50
        self.rect.x = self.rect.x - 50

    def shoot_up(self, time):
        # Based on time, move 50 pixels
        self.y = self.y - 50
        self.rect.y = self.rect.y - 50

    def shoot_down(self, time):
        # Based on time, move 50 pixels
        self.y = self.y + 50
        self.y = self.rect.y - 50

    def update(self, time):
        if self.direction == "left":
            self.x = self.x - time * 150
            self.y = self.y + time * 0
        if self.direction == "right":
            self.x = self.x + time * 100
            self.y = self.y + time * 0
        if self.direction == "down":
            self.x = self.x + time * 0
            self.y = self.y + time * 100
        if self.direction == "up":
            self.x = self.x + time * 0
            self.y = self.y - time * 100
        self.rect.x = self.x
        self.rect.y = self.y
        self.collisions = []
        for sprite in self.blocks:
            self.collider.rect.x = sprite.x
            self.collider.rect.y = sprite.y
            if pygame.sprite.collide_rect(self, self.collider):
                self.collisions.append(sprite)
