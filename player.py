import pygame
import config

class Player:
    def __init__(self, x_postition, y_position):
        print("player created")
        self.position = [x_postition, y_position]
        self.image = pygame.image.load("imgs/character/tile000.png")
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE)

        self.walkDownCount = 0
        self.walkUpCount = 0
        self.walkLeftCount = 0
        self.walkRightCount = 0

    def update(self):
        print("player updated")

    def update_position(self, new_position):
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]


    def render(self, screen, camera):
        self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE - (camera[1] * config.SCALE), config.SCALE, config.SCALE)
        screen.blit(self.image, self.rect)

    """
    A function for walking the player with the various sprites.

    Basically, a player can be pressed into any direction, down up, etc

    Update the player walk sprite accordignly and based on which player sprite the player is currently on (WalkCount)
    """
    def updateWalk(self, direction):

        if direction == "DOWN":

            if (self.walkDownCount == 0):

                    playerImageLoad = pygame.image.load("imgs/character/tile001.png")

                    self.walkDownCount += 1

            elif (self.walkDownCount == 1):

                playerImageLoad = pygame.image.load("imgs/character/tile000.png")

                self.walkDownCount += 1

            elif (self.walkDownCount == 2):

                playerImageLoad = pygame.image.load("imgs/character/tile003.png")

                self.walkDownCount += 1

            elif (self.walkDownCount == 3):

                playerImageLoad = pygame.image.load("imgs/character/tile000.png")

                self.walkDownCount = 0

        elif direction == "UP":

            if (self.walkUpCount == 0):

                playerImageLoad = pygame.image.load("imgs/character/tile005.png")

                self.walkUpCount += 1

            elif (self.walkUpCount == 1):

                playerImageLoad = pygame.image.load("imgs/character/tile006.png")

                self.walkUpCount += 1

            elif (self.walkUpCount == 2):

                playerImageLoad = pygame.image.load("imgs/character/tile005.png")

                self.walkUpCount += 1

            elif (self.walkUpCount == 3):

                playerImageLoad = pygame.image.load("imgs/character/tile008.png")

                self.walkUpCount = 0

        elif direction == "RIGHT":

            if (self.walkRightCount == 0):

                playerImageLoad = pygame.image.load("imgs/character/tile016.png")

                self.walkRightCount += 1

            elif (self.walkRightCount == 1):

                playerImageLoad = pygame.image.load("imgs/character/tile015.png")

                self.walkRightCount += 1

            elif (self.walkRightCount == 2):

                playerImageLoad = pygame.image.load("imgs/character/tile016.png")

                self.walkRightCount += 1

            elif (self.walkRightCount == 3):

                playerImageLoad = pygame.image.load("imgs/character/tile017.png")

                self.walkRightCount = 0

        elif direction == "LEFT":

            if (self.walkLeftCount == 0):

                playerImageLoad = pygame.image.load("imgs/character/tile010.png")

                self.walkLeftCount += 1

            elif (self.walkLeftCount == 1):

                playerImageLoad = pygame.image.load("imgs/character/tile011.png")

                self.walkLeftCount += 1

            elif (self.walkLeftCount == 2):

                playerImageLoad = pygame.image.load("imgs/character/tile010.png")

                self.walkLeftCount += 1

            elif (self.walkLeftCount == 3):

                playerImageLoad = pygame.image.load("imgs/character/tile013.png")

                self.walkLeftCount = 0

        return playerImageLoad
