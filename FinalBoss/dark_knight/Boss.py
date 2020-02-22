import pygame
import sys
from engine.league.league import *
import random as rnd

sys.path.append('..')


class Boss(Character):

    def __init__(self, z, x, y):
        # Put z first to mimic his character.py and game_objects.py class
        super().__init__(z, x, y)
        self.health = 200  # My Health
        self.lastHit = pygame.time.get_ticks()  # Last booboo
        self.delta = (128 * 4)  # BIGGER = FASTER
        self.x = x
        self.y = y
        self._layer = 51
        self.move_count = 0
        self.rand_count = 0
        # self.rect.x = x
        # self.rect.y = y

        # Image!!!
        self.image = pygame.image.load('./FinalBoss/dark_knight_frames/idle_frames/frame_00_delay-0.14s.png').convert_alpha()
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

        # Animation counters and arrays
        self.move_up_down = 0
        self.move_left = 0
        self.move_right = 0
        self.attack_left = 0
        self.attack_right = 0
        self.left_move = ['./FinalBoss/dark_knight_frames/moving_left_frames/frame_00_delay-0.08s.png',
                          './FinalBoss/dark_knight_frames/moving_left_frames/frame_01_delay-0.08s.png',
                          './FinalBoss/dark_knight_frames/moving_left_frames/frame_02_delay-0.08s.png',
                          './FinalBoss/dark_knight_frames/moving_left_frames/frame_03_delay-0.08s.png',
                          './FinalBoss/dark_knight_frames/moving_left_frames/frame_04_delay-0.08s.png',
                          './FinalBoss/dark_knight_frames/moving_left_frames/frame_05_delay-0.08s.png',
                          './FinalBoss/dark_knight_frames/moving_left_frames/frame_06_delay-0.08s.png',
                          './FinalBoss/dark_knight_frames/moving_left_frames/frame_07_delay-0.08s.png',
                          './FinalBoss/dark_knight_frames/moving_left_frames/frame_08_delay-0.08s.png',
                          './FinalBoss/dark_knight_frames/moving_left_frames/frame_09_delay-0.08s.png',
                          './FinalBoss/dark_knight_frames/moving_left_frames/frame_10_delay-0.08s.png',
                          './FinalBoss/dark_knight_frames/moving_left_frames/frame_11_delay-0.08s.png',
                          './FinalBoss/dark_knight_frames/moving_left_frames/frame_12_delay-0.08s.png']
        self.right_move = ['./FinalBoss/dark_knight_frames/moving_right_frames/frame_00_delay-0.08s.png',
                           './FinalBoss/dark_knight_frames/moving_right_frames/frame_01_delay-0.08s.png',
                           './FinalBoss/dark_knight_frames/moving_right_frames/frame_02_delay-0.08s.png',
                           './FinalBoss/dark_knight_frames/moving_right_frames/frame_03_delay-0.08s.png',
                           './FinalBoss/dark_knight_frames/moving_right_frames/frame_04_delay-0.08s.png',
                           './FinalBoss/dark_knight_frames/moving_right_frames/frame_05_delay-0.08s.png',
                           './FinalBoss/dark_knight_frames/moving_right_frames/frame_06_delay-0.08s.png',
                           './FinalBoss/dark_knight_frames/moving_right_frames/frame_07_delay-0.08s.png',
                           './FinalBoss/dark_knight_frames/moving_right_frames/frame_08_delay-0.08s.png',
                           './FinalBoss/dark_knight_frames/moving_right_frames/frame_09_delay-0.08s.png',
                           './FinalBoss/dark_knight_frames/moving_right_frames/frame_10_delay-0.08s.png',
                           './FinalBoss/dark_knight_frames/moving_right_frames/frame_11_delay-0.08s.png',
                           './FinalBoss/dark_knight_frames/moving_right_frames/frame_12_delay-0.08s.png']
        self.up_down_move = ['./FinalBoss/dark_knight_frames/idle_frames/frame_01_delay-0.14s.png',
                             './FinalBoss/dark_knight_frames/idle_frames/frame_02_delay-0.14s.png',
                             './FinalBoss/dark_knight_frames/idle_frames/frame_03_delay-0.14s.png',
                             './FinalBoss/dark_knight_frames/idle_frames/frame_04_delay-0.14s.png',
                             './FinalBoss/dark_knight_frames/idle_frames/frame_05_delay-0.14s.png',
                             './FinalBoss/dark_knight_frames/idle_frames/frame_06_delay-0.14s.png',
                             './FinalBoss/dark_knight_frames/idle_frames/frame_07_delay-0.14s.png',
                             './FinalBoss/dark_knight_frames/idle_frames/frame_08_delay-0.14s.png',
                             './FinalBoss/dark_knight_frames/idle_frames/frame_09_delay-0.14s.png',
                             './FinalBoss/dark_knight_frames/idle_frames/frame_10_delay-0.14s.png']
        self.left_attack = ['./FinalBoss/dark_knight_frames/attack_left_frames/frame_01_delay-0.1s.png',
                            './FinalBoss/dark_knight_frames/attack_left_frames/frame_02_delay-0.1s.png',
                            './FinalBoss/dark_knight_frames/attack_left_frames/frame_03_delay-0.1s.png',
                            './FinalBoss/dark_knight_frames/attack_left_frames/frame_04_delay-0.1s.png',
                            './FinalBoss/dark_knight_frames/attack_left_frames/frame_05_delay-0.1s.png',
                            './FinalBoss/dark_knight_frames/attack_left_frames/frame_06_delay-0.1s.png',
                            './FinalBoss/dark_knight_frames/attack_left_frames/frame_07_delay-0.1s.png',
                            './FinalBoss/dark_knight_frames/attack_left_frames/frame_08_delay-0.1s.png',
                            './FinalBoss/dark_knight_frames/attack_left_frames/frame_09_delay-0.1s.png',
                            './FinalBoss/dark_knight_frames/attack_left_frames/frame_10_delay-0.1s.png',
                            './FinalBoss/dark_knight_frames/attack_left_frames/frame_11_delay-0.1s.png',
                            './FinalBoss/dark_knight_frames/attack_left_frames/frame_12_delay-0.1s.png',
                            './FinalBoss/dark_knight_frames/attack_left_frames/frame_13_delay-0.1s.png',
                            './FinalBoss/dark_knight_frames/attack_left_frames/frame_14_delay-0.1s.png',
                            './FinalBoss/dark_knight_frames/attack_left_frames/frame_15_delay-0.1s.png',
                            './FinalBoss/dark_knight_frames/attack_left_frames/frame_16_delay-0.1s.png',
                            './FinalBoss/dark_knight_frames/attack_left_frames/frame_17_delay-0.1s.png']
        self.right_attack = ['./FinalBoss/dark_knight_frames/attack_right_frames/frame_01_delay-0.1s.png',
                             './FinalBoss/dark_knight_frames/attack_right_frames/frame_02_delay-0.1s.png',
                             './FinalBoss/dark_knight_frames/attack_right_frames/frame_03_delay-0.1s.png',
                             './FinalBoss/dark_knight_frames/attack_right_frames/frame_04_delay-0.1s.png',
                             './FinalBoss/dark_knight_frames/attack_right_frames/frame_05_delay-0.1s.png',
                             './FinalBoss/dark_knight_frames/attack_right_frames/frame_06_delay-0.1s.png',
                             './FinalBoss/dark_knight_frames/attack_right_frames/frame_07_delay-0.1s.png',
                             './FinalBoss/dark_knight_frames/attack_right_frames/frame_08_delay-0.1s.png',
                             './FinalBoss/dark_knight_frames/attack_right_frames/frame_09_delay-0.1s.png',
                             './FinalBoss/dark_knight_frames/attack_right_frames/frame_10_delay-0.1s.png',
                             './FinalBoss/dark_knight_frames/attack_right_frames/frame_11_delay-0.1s.png',
                             './FinalBoss/dark_knight_frames/attack_right_frames/frame_12_delay-0.1s.png',
                             './FinalBoss/dark_knight_frames/attack_right_frames/frame_13_delay-0.1s.png',
                             './FinalBoss/dark_knight_frames/attack_right_frames/frame_14_delay-0.1s.png',
                             './FinalBoss/dark_knight_frames/attack_right_frames/frame_15_delay-0.1s.png',
                             './FinalBoss/dark_knight_frames/attack_right_frames/frame_16_delay-0.1s.png',
                             './FinalBoss/dark_knight_frames/attack_right_frames/frame_17_delay-0.1s.png']

    def _left_move(self, time):
        if self.move_left <= 11:
            self.image = pygame.image.load(self.left_move[self.move_left]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (36, 36))
            self.rect = self.image.get_rect()
            self.move_left += 1
        else:
            if self.move_left == 12:
                self.move_left = 0

    def _right_move(self, time):
        if self.move_right <= 11:
            self.image = pygame.image.load(self.right_move[self.move_right]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (36, 36))
            self.rect = self.image.get_rect()
            self.move_right += 1
        else:
            if self.move_right == 12:
                self.move_right = 0

    def _up_down_move(self, time):
        if self.move_up_down <= 9:
            self.image = pygame.image.load(self.up_down_move[self.move_up_down]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (36, 36))
            self.rect = self.image.get_rect()
            self.move_up_down += 1
        else:
            if self.move_up_down == 10:
                self.move_up_down = 0

    def _left_attack(self, time):
        if self.attack_left <= 16:
            self.image = pygame.image.load(self.left_attack[self.attack_left]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (36, 36))
            self.rect = self.image.get_rect()
            self.attack_left += 1
        else:
            if self.attack_left == 17:
                self.attack_left = 0

    def _right_attack(self, time):
        if self.attack_right <= 16:
            self.image = pygame.image.load(self.left_attack[self.attack_right]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (36, 36))
            self.rect = self.image.get_rect()
            self.attack_right += 1
        else:
            if self.attack_right == 17:
                self.attack_right = 0

    def move(self, time):
        amount = self.delta * time
        if self.health > 0:
            if self.move_count == 6 or self.move_count == 7:
                if self.move_count == 7:
                    # move up
                    self._up_down_move()
                    self.y = self.y - amount
                    self.move_count = 0
                    return
                else:
                    self._up_down_move()
                    self.y = self.y - amount
                    self.move_count += 1
            if self.move_count == 4 or self.move_count == 5:
                # move left
                self._left_move()
                self.x = self.x - amount
                self.move_count += 1

            if self.move_count == 2 or self.move_count == 3:
                # move down
                self._up_down_move()
                self.y = self.y + amount
                self.move_count += 1

            if self.move_count == 0 or self.move_count == 1:
                # move right
                self._right_attack()
                self.x = self.x + amount
                self.move_count += 1

    def move_random(self, time):
        amount = self.delta * time
        rand_count = rnd.randint(0, 3)
        if self.health > 0:
            if rand_count == 5:
                # Attacks left
                self._left_attack(1)
            if rand_count == 4:
                # Attacks right
                self._right_attack(1)
            if rand_count == 3:
                # move up
                self._up_down_move(1)
                self.y = self.y - amount
            if rand_count == 2:
                # move left
                self._left_move(1)
                self.x = self.x - amount
            if rand_count == 1:
                # move down
                self._up_down_move(1)
                self.y = self.y + amount
            if rand_count == 0:
                # move right
                self._right_move(1)
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
