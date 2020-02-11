# This game is the dopest dope you've ever smoked, my guy


import pygame
import sys
import helperFuncs
from projectile import Projectile

sys.path.append('.')
from engine.league import league
from player.Player import Player

# This is the event counter for our manually created events, call with evCnt()
evCnt = lambda: helperFuncs.eventNum.newEvent(helperFuncs.eventNum)


def main():
    def quit(self):
        engine.running = False

    engine = league.Engine("Midnight Riders")
    league.Settings.height = 768
    league.Settings.width = 768
    engine.init_pygame()

    # Our tilesheet is 16x16 pixels
    league.Settings.tile_size = 16
    # Assign tilesheet
    tilesheet = league.Spritesheet('./TilesetGraveyard_16.png', league.Settings.tile_size, 12)
    # Set tilemaps for blank background and main scene
    scene = league.Tilemap('./finalScene.lvl', tilesheet, 16, 1)
    scene_size = (scene.wide * league.Settings.tile_size, scene.high * league.Settings.tile_size)
    backdrop = league.Tilemap('./ourBackground.lvl', tilesheet, 16, 0)
    # Add to drawables that are passable and impassable
    engine.drawables.add(scene.passable.sprites())
    engine.drawables.add(backdrop.passable.sprites())

    # Create player
    player = Player(2, 350, 350)
    # Create projectile
    fire_ball = Projectile(player)

    # Add blocks for player and fire_ball
    player.blocks.add(scene.impassable)
    fire_ball.blocks.add(scene.impassable)

    # Set scene size for boundaries
    player.worldSize = scene_size
    # Set world size for fireball
    fire_ball.worldSize = scene_size

    # Get rekt, set location
    player.rect = player.image.get_rect()
    player.rect.x = 350
    player.rect.y = 350
    # Fireball get rekt
    fire_ball.rect = fire_ball.image.get_rect()
    fire_ball.x = player.x
    fire_ball.y = player.y

    # Add to objects and drawables
    engine.objects.append(player)
    engine.drawables.add(player)
    # Add fireball to objects and drawables
    engine.objects.append(fire_ball)
    engine.drawables.add(fire_ball)

    # Key event functions for player
    engine.key_events[pygame.K_a] = player.moveLeft
    engine.events[pygame.USEREVENT + evCnt()] = player.moveLeft
    engine.key_events[pygame.K_d] = player.moveRight
    engine.events[pygame.USEREVENT + evCnt()] = player.moveRight
    engine.key_events[pygame.K_w] = player.moveUp
    engine.events[pygame.USEREVENT + evCnt()] = player.moveUp
    engine.key_events[pygame.K_s] = player.moveDown
    engine.events[pygame.USEREVENT + evCnt()] = player.moveDown

    # Key event function for projectile
    engine.key_events[pygame.K_j] = fire_ball.shoot_left
    engine.events[pygame.USEREVENT + evCnt()] = fire_ball.shoot_left
    engine.key_events[pygame.K_i] = fire_ball.shoot_up
    engine.events[pygame.USEREVENT + evCnt()] = fire_ball.shoot_up
    engine.key_events[pygame.K_k] = fire_ball.shoot_down
    engine.events[pygame.USEREVENT + evCnt()] = fire_ball.shoot_down
    engine.key_events[pygame.K_l] = fire_ball.shoot_right
    engine.events[pygame.USEREVENT + evCnt()] = fire_ball.shoot_right

    # Quit function
    engine.events[pygame.QUIT] = quit
    # Run the engine
    engine.run()


if __name__ == '__main__':
    main()

print("THIS IS CONFIRMATION THAT I MADE IT TO THE END OF THE FILE WITHOUT GETTING HUNG UP")
