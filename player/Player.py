from league import *
import pygame

class Player(Character):

    def __init__(self):
        super().__init__(x, y, z)
        self.health = 100 #My Health
        self.lastHit = pygame.time.get_ticks() #Last booboo
        self.delta = 512 #BIGGER = FASTER
        self.x = x
        self.y = y

        #Image!!!
        self.image = pygame.image.load('../sprites/Player sprites/IdleFront.gif').convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()

        #World size, and collisions
        self.worldSize = (Settings.width, Settings.height)
        self.blocks = pygame.sprite.Group()
        self.collideFunction = pygame.sprite.collide_circle #can use other shapes
        solf.collisions = []

        #collision sprite
        self.collider = Drawable()
        self.collider.image = pygame.Surface([Settings.tile_size, Settings.tile_size])
        self.collider.rect = self.collider.image.get_rect()

        #HUD/Overlay
        self.font = pygame.font.Font('../Beware.ttf', 32)
        self.overlay = self.font.render(str(self.health) + "    3 Lives", True, (0, 0, 0))

