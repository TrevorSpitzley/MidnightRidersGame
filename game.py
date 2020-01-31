# This game is the dopest dope you've ever smoked, my guy


import pygame
import sys

sys.path.append('.')
from engine.league import league
from player import Player


def quit(self):
    pygame.exit()
    sys.exit()


league.Settings.height = 768
league.Settings.width = 768
# Our tilesheet is 16x16 pixels
league.Settings.tile_size = 16

tilesheet = league.Spritesheet('', league.Settings.tile_size, )
