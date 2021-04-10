import pygame
import config
import sys
import math
from player import Player
from game_state import GameState

class Quiz:

    def __init__(self):
        self.click = False
        self.running = True

        pygame.init()
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def startQuiz(self):

        while self.running:
            self.screen.fill((0,0,0))

            #As usual, check for player events
            for event in pygame.event.get():

                #If we detect that a player has pressed the x button, we quit the application
                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()
                    print("quit")

