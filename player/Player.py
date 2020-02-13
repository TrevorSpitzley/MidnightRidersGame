import pygame
import sys

sys.path.append('..')
from engine.league.league import *


# from engine.league.examples import overlay


class Player(Character):

    def __init__(self, z, x, y):
        # Put z first to mimic his character.py and game_objects.py class
        super().__init__(z, x, y)
        self.health = 100  # My Health
        self.lastHit = pygame.time.get_ticks()  # Last booboo
        self.delta = 128  # BIGGER = FASTER
        self.x = x
        self.y = y
        self._layer = 51
        # self.rect.x = x
        # self.rect.y = y

        # Image!!!
        self.image = pygame.image.load('./sprites/Player_sprites/IdleFront.png').convert_alpha()
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

        # HUD/Overlay
        self.font = pygame.font.Font('./Beware.ttf', 32)
        self.overlay = self.font.render(str(self.health) + "    3 Lives", True, (0, 0, 0))

        # Create image arrays for animation and make counters for image access
        self.up_counter = 0
        self.down_counter = 0
        self.right_counter = 0
        self.left_counter = 0

        self.up_array = [
            './sprites/Player_sprites/player_sprites_frames/back_idle_frames/frame_0_delay-0.5s.png',
            './sprites/Player_sprites/player_sprites_frames/back_idle_frames/frame_0_delay-0.5s.png',
            './sprites/Player_sprites/player_sprites_frames/back_idle_frames/frame_1_delay-0.5s.png',
            './sprites/Player_sprites/player_sprites_frames/back_idle_frames/frame_1_delay-0.5s.png']
        self.down_array = [
            './sprites/Player_sprites/player_sprites_frames/front_idle_frames/frame_0_delay-0.5s.png',
            './sprites/Player_sprites/player_sprites_frames/front_idle_frames/frame_1_delay-0.5s.png',
            './sprites/Player_sprites/player_sprites_frames/front_idle_frames/frame_2_delay-0.5s.png',
            './sprites/Player_sprites/player_sprites_frames/front_idle_frames/frame_3_delay-0.5s.png',
            './sprites/Player_sprites/player_sprites_frames/front_idle_frames/frame_4_delay-0.5s.png',
            './sprites/Player_sprites/player_sprites_frames/front_idle_frames/frame_5_delay-0.5s.png',
            './sprites/Player_sprites/player_sprites_frames/front_idle_frames/frame_6_delay-0.5s.png',
            './sprites/Player_sprites/player_sprites_frames/front_idle_frames/frame_7_delay-0.5s.png']
        self.right_array = [
            './sprites/Player_sprites/player_sprites_frames/moving_right_frames/frame_0.png',
            './sprites/Player_sprites/player_sprites_frames/moving_right_frames/frame_1.png',
            './sprites/Player_sprites/player_sprites_frames/moving_right_frames/frame_2.png',
            './sprites/Player_sprites/player_sprites_frames/moving_right_frames/frame_3.png',
            './sprites/Player_sprites/player_sprites_frames/moving_right_frames/frame_4.png',
            './sprites/Player_sprites/player_sprites_frames/moving_right_frames/frame_5.png',
            './sprites/Player_sprites/player_sprites_frames/moving_right_frames/frame_6.png',
            './sprites/Player_sprites/player_sprites_frames/moving_right_frames/frame_7.png']
        self.left_array = [
            './sprites/Player_sprites/player_sprite_frames/moving_left_frames/frame_1.png',
            './sprites/Player_sprites/player_sprite_frames/moving_left_frames/frame_2.png',
            './sprites/Player_sprites/player_sprite_frames/moving_left_frames/frame_3.png',
            './sprites/Player_sprites/player_sprite_frames/moving_left_frames/frame_4.png',
            './sprites/Player_sprites/player_sprite_frames/moving_left_frames/frame_5.png',
            './sprites/Player_sprites/player_sprite_frames/moving_left_frames/frame_6.png',
            './sprites/Player_sprites/player_sprite_frames/moving_left_frames/frame_7.png',
            './sprites/Player_sprites/player_sprite_frames/moving_left_frames/frame_8.png']

    def moveLeft(self, time):
        # Reset other counters on first move to ensure the animation starts on image[0]
        self.up_counter = 0
        self.down_counter = 0
        self.right_counter = 0
        amount = self.delta * time
        try:
            if self.x - amount < 0:
                raise OffScreenLeftException
            else:
                self.image = pygame.image.load(self.left_array[self.left_counter]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (36, 36))
                self.rect = self.image.get_rect()
                if self.left_counter < 7:
                    self.left_counter += 1
                else:
                    self.left_counter = 0
                self.x = self.x - amount
                self.update(0)
                while (len(self.collisions) != 0):
                    self.x = self.x + amount
                    self.update(0)
        except:
            pass

    def moveRight(self, time):
        # Reset other counters on first move to ensure the animation starts on image[0]
        self.up_counter = 0
        self.down_counter = 0
        self.left_counter = 0
        self.collisions = []
        amount = self.delta * time
        try:
            if self.x + amount > self.worldSize[0] - Settings.tile_size:
                raise OffScreenRightException
            else:
                self.image = pygame.image.load(self.right_array[self.right_counter]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (36, 36))
                self.rect = self.image.get_rect()
                if self.right_counter < 7:
                    self.right_counter += 1
                else:
                    self.right_counter = 0
                self.x = self.x + amount
                self.update(0)
                while (len(self.collisions) != 0):
                    self.x = self.x - amount
                    self.update(0)
        except:
            pass

    def moveUp(self, time):
        # Reset other counters on first move to ensure the animation starts on image[0]
        self.down_counter = 0
        self.right_counter = 0
        self.left_counter = 0
        self.collisions = []
        amount = self.delta * time
        try:
            if self.y - amount < 0:
                raise OffScreenTopException
            else:
                self.image = pygame.image.load(self.up_array[self.up_counter]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (36, 36))
                self.rect = self.image.get_rect()
                if self.up_counter < 4:
                    self.up_counter += 1
                else:
                    self.up_counter = 0
                self.y = self.y - amount
                self.update(0)
                if len(self.collisions) != 0:
                    self.y = self.y + amount
                    self.update(0)
                    self.collisions = []
        except:
            pass

    def moveDown(self, time):
        # Reset other counters on first move to ensure the animation starts on image[0]
        self.up_counter = 0
        self.right_counter = 0
        self.left_counter = 0
        amount = self.delta * time
        try:
            if self.y + amount > self.worldSize[1] - Settings.tile_size:
                raise OffScreenBottomException
            else:
                self.image = pygame.image.load(self.down_array[self.down_counter]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (36, 36))
                self.rect = self.image.get_rect()
                if self.down_counter < 7:
                    self.down_counter += 1
                else:
                    self.down_counter = 0
                self.y = self.y + amount
                self.update(0)
                if len(self.collisions) != 0:
                    self.y = self.y - amount
                    self.update(0)
                    self.collisions = []
        except:
            pass

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
