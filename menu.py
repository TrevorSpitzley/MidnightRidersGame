import pygame
import sys
sys.path.append('..')
from engine.league import league
import game
import menuEngine
from helperFuncs import eventNum


def main():

    # This is the event counter for our manually created events, call with evCnt()
    evCnt = lambda: helperFuncs.eventNum.newEvent(helperFuncs.eventNum)


    engine = menuEngine.menuEngine("Midnight Riders")

    league.Settings.height = 768
    league.Settings.width = 768
    league.Settings.key_repeat = 1000
    engine.init_pygame()

    def changeSelectionBack(self):
        engine.currentSelection = engine.currentSelection - 1

        if (engine.currentSelection < 0):
            engine.currentSelection = engine.numSelectOptions

    def changeSelectionForward(self):
        engine.currentSelection = engine.currentSelection + 1

        if (engine.currentSelection > engine.numSelectOptions):
            engine.currentSelection = 0


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

    #set selector locations for choosing menu items
    selectLocations = [(75, 125), (75, 290), (75, 460)]
    engine.setSelectLocations(selectLocations)

    #set intro screens to array
    introScreens = [midnightRidersLogo, midnightRidersLogo, midnightRidersLogo]

    #add menus to menu engine
    engine.setMenus(mainBack, menuDef, selectMenuScreens)

    #set menu music
    engine.setMusic('./Spartacus.ogg')

    #set selector sprites and locations
    selectorImages = []
    for i in range(61):
        if(i < 10):
            imageNum = "00" + str(i)
        else:
            imageNum = "0" + str(i)
        temp = "./sprites/menuSelector/tile" + imageNum + ".png"
        selectorImages.append(temp)
    engine.setSelectorSprite(selectorImages, 110, 110)


    #set game icon
    pygame.display.set_icon(gameIcon)

    def quit(self):
        engine.running = False

    # Quit function
    engine.events[pygame.QUIT] = quit
    engine.key_events[pygame.K_RETURN] = quit

    engine.showIntro(introScreens, 24.6)

    #add events
    engine.key_events[pygame.K_ESCAPE] = quit
    engine.events[pygame.USEREVENT + 1] = changeSelectionBack
    engine.key_events[pygame.K_UP] = changeSelectionBack
    engine.events[pygame.USEREVENT + 2] = changeSelectionForward
    engine.key_events[pygame.K_DOWN] = changeSelectionForward


    engine.run()

    if (False):
        game.main()

if __name__ == '__main__':
    main()
