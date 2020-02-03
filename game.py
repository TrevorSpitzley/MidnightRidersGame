# This game is the dopest dope you've ever smoked, my guy


import pygame
import sys
import helperFuncs
sys.path.append('.')
from engine.league import league
from player import Player

# This is the event counter for our manually created events, call with evCnt()
evCnt = lambda: helperFuncs.eventNum.newEvent(helperFuncs.eventNum)


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
scene = league.Tilemap('./ridersScene.lvl', tilesheet, 16, 1)
scene_size = (scene.wide * league.Settings.tile_size, scene.high * league.Settings.tile_size)
backdrop = league.Tilemap('./ourBackground.lvl', tilesheet, 16, 0)
# Add to drawables
engine.drawables.add(scene.passable.sprites())
engine.drawables.add(backdrop.passable.sprites())
# Quit function
engine.events[pygame.QUIT] = quit
# Run the engine
engine.run()

print("THIS IS CONFIRMATION THAT I MADE IT TO THE END OF THE FILE WITHOUT GETTING HUNG UP")
