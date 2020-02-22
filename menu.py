import pygame
import sys
sys.path.append('..')
from engine.league import league
import game

def main():

    def iterateMenuScreen():
        return  0


    engine = league.menuEngine("Midnight Riders")

    league.Settings.height = 768
    league.Settings.width = 768
    engine.init_pygame()

    #load images
    gameIcon = pygame.image.load('./background/passive2.png').convert_alpha()
    mainBack = pygame.image.load('./background/cyberpunk-street-files/PNG/cyberpunk-street2.png').convert_alpha()
    menuDef= pygame.image.load('./background/cyberpunk-street-files/PNG/menuDef.png').convert_alpha()
    menuPlay = pygame.image.load('./background/cyberpunk-street-files/PNG/menuPlay.png').convert_alpha()
    menuCredits= pygame.image.load('./background/cyberpunk-street-files/PNG/menuCredits.png').convert_alpha()
    menuQuit= pygame.image.load('./background/cyberpunk-street-files/PNG/menuQuit.png').convert_alpha()
    midnightRidersLogo = pygame.image.load('./introScreens/midnightRiders.png').convert()

    #set selection-representing versions of menu images into an array for iteration
    selectMenuScreens = [menuPlay, menuCredits, menuQuit]

    #set intro screens to array
    introScreens = [midnightRidersLogo]

    #add menus to menu engine
    engine.setMenus(mainBack, menuDef, selectMenuScreens)

    #set menu music
    engine.setMusic('./Spartacus.ogg')


    #set game icon
    pygame.display.set_icon(gameIcon)

    def quit(self):
        engine.running = False

    # Quit function
    engine.events[pygame.QUIT] = quit
    engine.key_events[pygame.K_RETURN] = quit

    #pygame.mixer.music.load('./Spartacus.ogg')
    #pygame.mixer.music.play(-1)

    engine.showIntro(introScreens)

    engine.run()

    if (False):
        game.main()

if __name__ == '__main__':
    main()
