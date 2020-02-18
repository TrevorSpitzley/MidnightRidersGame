# This game is the dopest dope you've ever smoked, my guy


import pygame
import sys
import helperFuncs
from enemy.Enemy import Enemy
from projectile import Projectile

sys.path.append('.')
from engine.league import league
from player.Player import Player
from pygame import mixer

# This is the event counter for our manually created events, call with evCnt()
evCnt = lambda: helperFuncs.eventNum.newEvent(helperFuncs.eventNum)


def main():
    def quit(self):
        engine.running = False

    engine = league.Engine("Midnight Riders")
    league.Settings.height = 768
    league.Settings.width = 768
    engine.init_pygame()
    mixer.music.load('./ogg_files/boss.ogg')
    mixer.music.play(-1)

    # Our tilesheet is 16x16 pixels
    league.Settings.tile_size = 16
    # Assign tilesheet
    tilesheet = league.Spritesheet('./TilesetGraveyard_16.png', league.Settings.tile_size, 12)
    # Set tilemaps for blank background and main scene
    scene = league.Tilemap('./finalScene.lvl', tilesheet, 16, 1)
    scene_size = (scene.wide * league.Settings.tile_size, scene.high * league.Settings.tile_size)
    z_scene_size = ((scene.wide * league.Settings.tile_size) - 32, (scene.high * league.Settings.tile_size) - 32)
    backdrop = league.Tilemap('./ourBackground.lvl', tilesheet, 16, 0)
    # Add to drawables that are passable and impassable
    engine.drawables.add(scene.passable.sprites())
    engine.drawables.add(backdrop.passable.sprites())

    # Create player & enemy
    player = Player(2, 350, 350)
    enemy1 = Enemy(2, 80, 170)
    enemy2 = Enemy(2, 650, 200)
    enemy3 = Enemy(2, 55, 550)
    # enemy4 = Enemy(2,)
    fire_ball1 = Projectile

    # Add blocks for player
    player.blocks.add(scene.impassable)
    enemy1.blocks.add(scene.impassable)
    enemy2.blocks.add(scene.impassable)
    enemy3.blocks.add(scene.impassable)

    # Set scene size for boundaries
    player.worldSize = scene_size
    enemy1.worldSize = z_scene_size
    enemy2.worldSize = z_scene_size
    enemy3.worldSize = z_scene_size

    # Get rekt, set location
    player.rect = player.image.get_rect()
    player.rect.x = 350
    player.rect.y = 350

    enemy1.rect = enemy1.image.get_rect()
    enemy1.rect.x = 200
    enemy1.rect.y = 200

    enemy2.rect = enemy2.image.get_rect()
    enemy2.rect.x = 650
    enemy2.rect.y = 200

    enemy3.rect = enemy3.image.get_rect()
    enemy3.rect.x = 55
    enemy3.rect.y = 550

    # Add to objects and drawables
    engine.objects.append(player)
    engine.drawables.add(player)

    engine.objects.append(enemy1)
    engine.drawables.add(enemy1)

    engine.objects.append(enemy2)
    engine.drawables.add(enemy2)

    engine.objects.append(enemy3)
    engine.drawables.add(enemy3)

    # Key event functions for player
    engine.key_events[pygame.K_a] = player.moveLeft
    engine.events[pygame.USEREVENT + evCnt()] = player.moveLeft
    engine.key_events[pygame.K_d] = player.moveRight
    engine.events[pygame.USEREVENT + evCnt()] = player.moveRight
    engine.key_events[pygame.K_w] = player.moveUp
    engine.events[pygame.USEREVENT + evCnt()] = player.moveUp
    engine.key_events[pygame.K_s] = player.moveDown
    engine.events[pygame.USEREVENT + evCnt()] = player.moveDown

    def make_projectile_left(time):
        fire_ball = Projectile(player, "left")
        fire_ball.blocks.add(scene.impassable)
        fire_ball.shoot_left(pygame.time.get_ticks())
        engine.objects.append(fire_ball)
        engine.drawables.add(fire_ball)
        engine.events[pygame.USEREVENT + 1000] = fire_ball.shoot_left

    def make_projectile_right(time):
        fire_ball = Projectile(player, "right")
        fire_ball.blocks.add(scene.impassable)
        fire_ball.shoot_left(pygame.time.get_ticks())
        engine.objects.append(fire_ball)
        engine.drawables.add(fire_ball)
        engine.events[pygame.USEREVENT + 1030] = fire_ball.shoot_right

    def make_projectile_up(time):
        fire_ball = Projectile(player, "up")
        fire_ball.blocks.add(scene.impassable)
        fire_ball.shoot_left(pygame.time.get_ticks())
        engine.collisions[enemy1] = (fire_ball, enemy1.getHit)
        engine.objects.append(fire_ball)
        engine.drawables.add(fire_ball)
        engine.events[pygame.USEREVENT + 1010] = fire_ball.shoot_up

    def make_projectile_down(time):
        fire_ball = Projectile(player, "down")
        fire_ball.blocks.add(scene.impassable)
        fire_ball.shoot_left(pygame.time.get_ticks())
        engine.objects.append(fire_ball)
        engine.drawables.add(fire_ball)
        engine.events[pygame.USEREVENT + 1020] = fire_ball.shoot_down

    # Key event function for projectile and set timer
    engine.key_events[pygame.K_j] = make_projectile_left
    engine.key_events[pygame.K_i] = make_projectile_up
    engine.key_events[pygame.K_k] = make_projectile_down
    engine.key_events[pygame.K_l] = make_projectile_right

    # Auto movement for enemy1
    move_enemy1 = pygame.USEREVENT + evCnt()
    pygame.time.set_timer(move_enemy1, 500)
    # engine.events[move_enemy1] = enemy1.move
    engine.events[move_enemy1] = enemy1.move_random

    move_enemy2 = pygame.USEREVENT + evCnt()
    pygame.time.set_timer(move_enemy2, 500)
    # engine.events[move_enemy2] = enemy2.move
    engine.events[move_enemy2] = enemy2.move_random

    move_enemy3 = pygame.USEREVENT + evCnt()
    pygame.time.set_timer(move_enemy3, 500)
    # engine.events[move_enemy3] = enemy3.move
    engine.events[move_enemy3] = enemy3.move_random

    # Quit function
    engine.events[pygame.QUIT] = quit
    engine.key_events[pygame.K_ESCAPE] = quit
    # Run the engine
    engine.run()


if __name__ == '__main__':
    main()

print("THIS IS CONFIRMATION THAT I MADE IT TO THE END OF THE FILE WITHOUT GETTING HUNG UP")
