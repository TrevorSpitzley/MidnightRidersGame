# This game is the dopest dope you've ever smoked, my guy


import pygame
import sys

sys.path.append('.')
import helperFuncs
from engine.league import league
from player import Player


#This is the event counter for our manually created events, call with evCnt()
evCnt = lambda: helperFuncs.eventNum.newEvent(helperFuncs.eventNum)

def quit(self):
    pygame.exit()
    sys.exit()


league.Settings.height = 768
league.Settings.width = 768
# Our tilesheet is 16x16 pixels
league.Settings.tile_size = 16

tilesheet = league.Spritesheet('', league.Settings.tile_size, )

print("THIS IS CONFIRMATION THAT I MADE IT TO THE END OF THE FILE WITHOUT GETTING HUNG UP")
