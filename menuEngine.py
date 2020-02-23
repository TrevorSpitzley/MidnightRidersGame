import abc
import os
import time
import pygame

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import  sys
sys.path.append('.')
from engine.league.league.settings import *
from engine.league.league import *

class menuEngine(Engine):

    #background color for intro



    def setMenus(self, background, mainMenu, selectionMenus):
        self.background = background
        self.mainMenu = mainMenu
        self.selectionMenus = selectionMenus


    def setMusic(self, musicPath):
        pygame.mixer.music.load(musicPath)

    def setSelectLocations(self, selectorLocations):
        self.selectorLocations = selectorLocations
        self.numSelectOptions = len(selectorLocations)

    def setSelectorSprite(self, selectorSprite, x, y):
        self.selectorSprite = selectorSprite
        self.numSelectorSprites = len(selectorSprite)

        #convert sprites to proper type and size
        for i in range(self.numSelectorSprites):
            selectorSprite[i] = pygame.image.load(selectorSprite[i]).convert_alpha()
            selectorSprite[i] = pygame.transform.scale(selectorSprite[i], (x, y))

        self.selectCounter = 0 #counter for sprite interation
        self.currentSelectorImage = selectorSprite[0]

    def iterateSelectorSprite(self):
        self.currentSelectorImage = self.selectorSprite[self.selectCounter]
        arrCount = self.numSelectorSprites - 1
        if (self.selectCounter >= (arrCount)):
            self.selectCounter = 0
        else:
            self.selectCounter = self.selectCounter + 1

    def changeSelection(self):


    def playMusic(self):
        pygame.mixer.music.play(-1)

    def animateSprite(self):
        self.currentSprite


    def showMenu(self):
        self.screen.blit(self.mainMenu, (0, 0))


    def showIntro(self, introScreens, runTime):
        #runTime is the total desired time for the entire intro sequence

        black = (0, 0, 0) #fill color for screen
        self.screen.fill(black) #give them something to look at while we do all this wibbly wobbly timey wimey math
        screenWidth = Settings.width
        screenHeight = Settings.height
        fadeTimePerImage = 5.983205318450928  # time for fade in and fade out per image
        darkTime = .5 #time between the previous and next image during which the screen is blank
        #two lines below are for benchmarking machines. above constant is from my machine
        # fadeFrameTimePerFrame = 0.011731775134217505 #time in seconds that each fading frame requires
        # print(fadeFrameTimePerFrame * 510) #print total fade time per image. For testing purposes on various machines
        numImages = len(introScreens) #the number of intro screens
        totalFadeTime = fadeTimePerImage * len(introScreens) #total fade time for the entire intro sequence
        imageHoldTime = (runTime - totalFadeTime - (darkTime * numImages)) / numImages #remaining time to hold each image after fade is remobed

        pygame.mixer.music.play(-1)

        for i in range(numImages):

            imageWidth = introScreens[i].get_width()
            imageHeight = introScreens[i].get_height()

            #resize to display size if too large

            #else, calculate x and y position
            x = (screenWidth / 2) - (imageWidth / 2)
            y = (screenHeight / 2) - (imageHeight / 2)

            for j in range(256):
                introScreens[i].set_alpha(j)
                self.screen.fill(black)
                self.screen.blit(introScreens[i], (x, y))
                pygame.display.flip()
                time.sleep(.01)
            time.sleep(imageHoldTime)
            for j in range(255):
                introScreens[i].set_alpha(255-(j+1))
                self.screen.fill(black)
                self.screen.blit(introScreens[i], (x, y))
                pygame.display.flip()
                time.sleep(.01)
            time.sleep(darkTime)


    def run(self):
        """The main menu loop, which makes animating the menu possible"""
        self.running = True
        while self.running:
            # The time since the last check
            now = pygame.time.get_ticks()
            self.real_delta_time = now - self.last_checked_time
            self.last_checked_time = now
            self.game_delta_time = self.real_delta_time * (0.001 * Settings.gameTimeFactor)

            # Wipe screen
            self.screen.fill(Settings.fill_color)

            # Process inputs
            self.handle_inputs()

            # Update game world
            # Each object must have an update(time) method
            self.check_collisions()
            for o in self.objects:
                o.update(self.game_delta_time)

            self.showMenu()
            self.iterateSelectorSprite()
            self.screen.blit(self.currentSelectorImage, self.selectorLocations[0])

            # Generate outputs
            # d.update()
            self.drawables.draw(self.screen)

            # Show statistics?
            if self.visible_statistics:
                self.show_statistics()

            # Could keep track of rectangles and update here, but eh.
            pygame.display.flip()

            # Frame limiting code
            self.clock.tick(Settings.fps)
