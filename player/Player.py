import pygame
import sys
sys.path.append('..')
from engine.league.league import *


class Player(Character):

    def __init__(self, z, x, y):
        # Put z first to mimic his character.py and game_objects.py class
        super().__init__(z, x, y)
        self.health = 100 #My Health
        self.lastHit = pygame.time.get_ticks() #Last booboo
        self.delta = 512 #BIGGER = FASTER
        self.x = x
        self.y = y

        #Image!!!
        self.image = pygame.image.load('./sprites/Player_sprites/IdleFront.png').convert_alpha()
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

        #HUD/Overlay
        self.font = pygame.font.Font('./Beware.ttf', 32)
        self.overlay = self.font.render(str(self.health) + "    3 Lives", True, (0, 0, 0))


    def moveLeft(self, time):
        amount = self.delta * time
        try:
            if self.x - amount < 0:
                raise OffScreenLeftException
            else:
                self.x = self.x - amount
                self.update(0)
                while(len(self.collisions) != 0):
                    self.x = self.x + amount
                    self.update(0)
        except:
            pass

    def moveRight(self, time):
        return 0


    def moveUp(self, time):
        return 0


    def moveDown(self, time):
        return 0

    def update(self, time):
        self.rect.x = self.x
        self.rect.y = self.y
        self.collisions = []
        for sprite in self.blocks:
            self.collider.rect.x = sprite.x
            self.collider.rect.y = sprite.y
            if pygame.sprite.collide_rect(self, self.collider):
                self.collisions.append(sprite)


    def getHit(self, damage):
        now = pygame.time.get_ticks()
        if now - self.lastHit > 1000:
            self.lastHit = self.health - damage
            self.lastHit = now

