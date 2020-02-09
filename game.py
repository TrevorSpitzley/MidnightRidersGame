# This game is the dopest dope you've ever smoked, my guy


import pygame
import sys
import helperFuncs
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
    # Add to drawables
    engine.drawables.add(scene.passable.sprites())
    engine.drawables.add(backdrop.passable.sprites())
    # Create player
    player = Player(2, 350, 350)
    # Set scene size for boundaries
    player.worldSize = scene_size
    # Get rekt, set location
    player.rect = player.image.get_rect()
    player.rect.x = 350
    player.rect.y = 350
    # Add to objects and drawables
    engine.objects.append(player)
    engine.drawables.add(player)
    # Key event functions
    engine.key_events[pygame.K_a] = player.moveLeft
    engine.events[pygame.USEREVENT + evCnt()] = player.moveLeft
    engine.key_events[pygame.K_d] = player.moveRight
    engine.events[pygame.USEREVENT + evCnt()] = player.moveRight
    engine.key_events[pygame.K_w] = player.moveUp
    engine.events[pygame.USEREVENT + evCnt()] = player.moveUp
    engine.key_events[pygame.K_s] = player.moveDown
    engine.events[pygame.USEREVENT + evCnt()] = player.moveDown
    # Quit function
    engine.events[pygame.QUIT] = quit
    # Run the engine
    engine.run()

if __name__=='__main__':
    main()

print("THIS IS CONFIRMATION THAT I MADE IT TO THE END OF THE FILE WITHOUT GETTING HUNG UP")
