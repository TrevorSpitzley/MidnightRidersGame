# This game is the dopest dope you've ever smoked, my guy


import pygame
import sys
import helperFuncs
from enemy.Enemy import Enemy
from enemy.EnemyController import EnemyController
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
    scene = league.Tilemap('./finalScene.lvl', tilesheet, 16, 2)
    scene_size = (scene.wide * league.Settings.tile_size, scene.high * league.Settings.tile_size)
    backdrop = league.Tilemap('./ourBackground.lvl', tilesheet, 16, 1)
    # Add to drawables that are passable and impassable

    enemyMap = []
    with open('finalScene.lvl') as f:
        next(f)
        next(f)
        for line in f:
            row = f.readline()
            row = row.strip()
            enemyMap.append([int(i) for i in row.split(',')])
    
    engine.drawables.add(scene.passable.sprites())
    engine.drawables.add(scene.impassable.sprites())
    engine.drawables.add(backdrop.passable.sprites())

    # Create player & enemy
    player = Player(2, 350, 350)
    enemy1 = Enemy(2, 80, 170)
    enemy2 = Enemy(2, 650, 200)
    enemy3 = Enemy(2, 55, 550)
    enemy4 = Enemy(2, 450, 650)
    enemy5 = Enemy(2, 375, 125)
    enemy_list = [enemy1, enemy2, enemy3, enemy4, enemy5]
    character_list = [enemy1, enemy2, enemy3, enemy4, enemy5, player]

    enemyController = EnemyController(enemyMap, enemy_list, player)
    enemyController.findPath

    def engine_add(characters):
        for obj in characters:
            # Add impassable blocks
            obj.blocks.add(scene.impassable)
            obj.blocks.add(scene.impassable.sprites())
            # Set scene size and boundaries
            obj.worldSize = scene_size
            # Load image
            obj.rect = obj.image.get_rect()
            # Add to drawable and updateable lists
            engine.objects.append(obj)
            engine.drawables.add(obj)

    engine_add(character_list)

    # Set locations of characters
    player.rect.x = 350
    player.rect.y = 350

    enemy1.rect.x = 200
    enemy1.rect.y = 200

    enemy2.rect.x = 650
    enemy2.rect.y = 200

    enemy3.rect.x = 55
    enemy3.rect.y = 550

    enemy4.rect.x = 450
    enemy4.rect.y = 650

    # Key event functions for player
    engine.key_events[pygame.K_a] = player.moveLeft
    engine.events[pygame.USEREVENT + evCnt()] = player.moveLeft
    engine.key_events[pygame.K_d] = player.moveRight
    engine.events[pygame.USEREVENT + evCnt()] = player.moveRight
    engine.key_events[pygame.K_w] = player.moveUp
    engine.events[pygame.USEREVENT + evCnt()] = player.moveUp
    engine.key_events[pygame.K_s] = player.moveDown
    engine.events[pygame.USEREVENT + evCnt()] = player.moveDown

    def add_collisions(collision_list, projectile):
        for obj in collision_list:
            engine.collisions[obj] = (projectile, obj.getHit)

    def projectile_add(projectile):
        projectile.blocks.add(scene.impassable)
        add_collisions(enemy_list, projectile)
        engine.drawables.add(projectile)
        engine.objects.append(projectile)

    def make_projectile_left(time):
        fire_ball = Projectile(player, "left")
        projectile_add(fire_ball)
        fire_ball.shoot_left(pygame.time.get_ticks())
        engine.events[pygame.USEREVENT + evCnt()] = fire_ball.shoot_left

    def make_projectile_right(time):
        fire_ball = Projectile(player, "right")
        projectile_add(fire_ball)
        fire_ball.shoot_left(pygame.time.get_ticks())
        engine.events[pygame.USEREVENT + evCnt()] = fire_ball.shoot_right

    def make_projectile_up(time):
        fire_ball = Projectile(player, "up")
        projectile_add(fire_ball)
        fire_ball.shoot_left(pygame.time.get_ticks())
        engine.events[pygame.USEREVENT + evCnt()] = fire_ball.shoot_up

    def make_projectile_down(time):
        fire_ball = Projectile(player, "down")
        projectile_add(fire_ball)
        fire_ball.shoot_left(pygame.time.get_ticks())
        engine.events[pygame.USEREVENT + evCnt()] = fire_ball.shoot_down

    # Key event function for projectile and set timer
    engine.key_events[pygame.K_j] = make_projectile_left
    engine.key_events[pygame.K_i] = make_projectile_up
    engine.key_events[pygame.K_k] = make_projectile_down
    engine.key_events[pygame.K_l] = make_projectile_right


    path_enemy = pygame.USEREVENT + evCnt()
    pygame.time.set_timer(path_enemy, 3000)
    engine.events[path_enemy] = enemyController.findPath

    
    move_enemy1 = pygame.USEREVENT + evCnt()
    pygame.time.set_timer(move_enemy1, 500)
    engine.events[move_enemy1] = enemy1.move

    move_enemy2 = pygame.USEREVENT + evCnt()
    pygame.time.set_timer(move_enemy2, 500)
    engine.events[move_enemy2] = enemy2.move

    move_enemy3 = pygame.USEREVENT + evCnt()
    pygame.time.set_timer(move_enemy3, 500)
    engine.events[move_enemy3] = enemy3.move

    move_enemy4 = pygame.USEREVENT + evCnt()
    pygame.time.set_timer(move_enemy4, 500)
    engine.events[move_enemy4] = enemy4.move

    move_enemy5 = pygame.USEREVENT + evCnt()
    pygame.time.set_timer(move_enemy5, 500)
    engine.events[move_enemy5] = enemy5.move

    # Quit function
    engine.events[pygame.QUIT] = quit
    engine.key_events[pygame.K_ESCAPE] = quit
    # Run the engine
    engine.run()


if __name__ == '__main__':
    main()

print("THIS IS CONFIRMATION THAT I MADE IT TO THE END OF THE FILE WITHOUT GETTING HUNG UP")
