import sys
import random as rnd
sys.path.append('..')
from engine.league.league import *
from engine.league.league.settings import Settings


class Enemy(Character):

    def __init__(self, z, x, y):
        # Put z first to mimic his character.py and game_objects.py class
        super().__init__(z, x, y)
        # My Health
        self.health = 10
        self.lastHit = pygame.time.get_ticks()
        # BIGGER = FASTER
        self.delta = (128 * 3)
        self.x = x
        self.y = y
        self.move_count = 0
        self._layer = 50

        self.path = [[0,0],[int(self.x/78), int(self.y/78)]]

        Settings.key_repeat = 1

        # Image
        self.image = pygame.image.load('./sprites/EnemySprite/zombie.png').convert_alpha()
        # Tweaked size
        self.image = pygame.transform.scale(self.image, (24, 36))
        self.rect = self.image.get_rect()

        # World size, and collisions
        self.worldSize = (Settings.width, Settings.height)
        self.blocks = pygame.sprite.Group()
        self.collide_function = pygame.sprite.collide_rect # can use other shapes
        self.collisions = []

        # collision sprite
        self.collider = Drawable()
        self.collider.image = pygame.Surface((Settings.tile_size, Settings.tile_size), pygame.SRCALPHA)
        self.collider.rect = self.collider.image.get_rect()

        # Death animation and counter
        self.death = 0
        self.death_mode = ['./sprites/EnemySprite/enemy_death_frames/frame0.png',
                           './sprites/EnemySprite/enemy_death_frames/frame1.png',
                           './sprites/EnemySprite/enemy_death_frames/frame2.png',
                           './sprites/EnemySprite/enemy_death_frames/frame3.png',
                           './sprites/EnemySprite/enemy_death_frames/frame4.png',
                           './sprites/EnemySprite/enemy_death_frames/frame5.png',
                           './sprites/EnemySprite/enemy_death_frames/frame6.png',
                           './sprites/EnemySprite/enemy_death_frames/frame7.png',
                           './sprites/EnemySprite/enemy_death_frames/frame8.png',
                           './sprites/EnemySprite/enemy_death_frames/frame9.png',
                           './sprites/EnemySprite/enemy_death_frames/frame10.png',
                           './sprites/EnemySprite/enemy_death_frames/frame11.png',
                           './sprites/EnemySprite/enemy_death_frames/frame12.png',
                           './sprites/EnemySprite/enemy_death_frames/frame13.png',
                           './sprites/EnemySprite/enemy_death_frames/frame14.png',
                           './sprites/EnemySprite/enemy_death_frames/frame15.png',
                           './sprites/EnemySprite/enemy_death_frames/frame16.png',
                           './sprites/EnemySprite/enemy_death_frames/frame17.png',
                           './sprites/EnemySprite/enemy_death_frames/frame18.png',
                           './sprites/EnemySprite/enemy_death_frames/frame19.png',
                           './sprites/EnemySprite/enemy_death_frames/frame20.png',
                           './sprites/EnemySprite/enemy_death_frames/frame21.png',
                           './sprites/EnemySprite/enemy_death_frames/frame22.png',
                           './sprites/EnemySprite/enemy_death_frames/frame23.png',
                           './sprites/EnemySprite/enemy_death_frames/frame24.png']

    def death_change(self, time):
        if self.death < 24:
            self.image = pygame.image.load(self.death_mode[self.death]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (24, 36))
            self.rect = self.image.get_rect()
            self.death += 1
        else:
            if self.death >= 24:
                return

    def move(self, time):
        if(len(self.path) > 1):
            tile = self.path[1]
            enPos = (int(self.x/78), int(self.y/78))
            amount = self.delta * time
            if self.health != 0:    
                if tile[0] > enPos[0]:
                    self.x = self.x + amount
            
                elif tile[0] < enPos[0]:
                    self.x = self.x - amount
                else:
                    self.x = self.x

                if tile[1] > enPos[1]:
                    self.y = self.y + amount
            
                elif tile[1] < enPos[1]:
                    self.y = self.y - amount
                else:
                    self.y = self.y
    def move_random(self, time):
        amount = self.delta * time
        move_count = rnd.randint(0, 3)
        if self.health != 0:
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
            # print("Health is" + str(self.health))
        if self.health <= 0:
            self.death_change(1)

    def setPath(self, path):
        self.path = path
