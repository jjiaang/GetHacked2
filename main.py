import pygame
import config
from game_state import GameState
import sys

from game import Game

"""
First we initialize pygame and set up the clock. Then we set up the caption as well.
"""
pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

pygame.display.set_caption("Pokemon Clone")

clock = pygame.time.Clock()
 
#This is for drawing the text. A function taken from online

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

"""
Defines the credits for the game. Gives credits to the creators

As well as explaining the game.
"""
def credits():

    # Initialize our running variable to be true, if we were to exit, this is set to false
    running = True
    
    while running:

        #Fill the default screen to black, will be changed later
        screen.fill((0,0,0))

        """
        Below defines the drawing text for the credits/tutorial part. Since we already have our function draw_text above, we just call it
        """
        draw_text('Tutorial and Credits/ How to play?', pygame.font.SysFont(None, 40), (255, 255, 255), screen, 20, 20)

        draw_text('Get Hacked! Is a python pygame based video game created by Jason, Deji, and Davis.', pygame.font.SysFont(None, 20), (255, 255, 255), screen, 20, 60)

        draw_text('This was made for the CPSC 329 class.', pygame.font.SysFont(None, 20), (255, 255, 255), screen, 20, 80)

        draw_text('The goal of this game is to run through and fight the bosses!', pygame.font.SysFont(None, 20), (255, 255, 255), screen, 20, 100)

        draw_text('To defeat the bosses, answer the questions and get it right!', pygame.font.SysFont(None, 20), (255, 255, 255), screen, 20, 120)

        """
        Check for events, if we exit, then we want to quit out of the game. Print quit in console to confirm it works
        """
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()
                print("quit")

            """
            If we press escape, then we set the running variable to false

            We then exit out of this screen, and go back to the main menu screen
            """
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:

                    running = False

        pygame.display.update()
        clock.tick(60)

"""
This is the main loop for the main menu. Each button has its own x and y position. We set up the buttons in the main menu, and then if we click on 
a button and it matches the x and y, then we go to that game loop. In each loop (like credits loop or game loop), if we press escape, then we "quit/break" and go back to main menu

Because in each loop, we have a loop. If we press escape inside one of those loops, like the game loop, etc, then we break out of the loop by setting the running condition to false.


"""
def mainMenu():

    """
    We set click to false. The click boolean is to detect whether something has been clicked or not.
    """
    click = False

    """
    The main menu loop. 
    """
    while True:

        screen.fill((0,0,0))

        #Draw the Main Menu Text for GetHacked!
        draw_text('Get Hacked!', pygame.font.SysFont(None, 40), (255, 255, 255), screen, 20, 20)

        """
        mx and my are where are mouse variables are. 
        """
        mx, my = pygame.mouse.get_pos()

        buttonOne = pygame.Rect(50,100,200,50)
        buttonTwo = pygame.Rect(50,200,200,50)

        if buttonOne.collidepoint((mx,my)):

            pygame.draw.rect(screen, (76, 122, 108), buttonOne)
            draw_text('Play Game', pygame.font.SysFont(None, 30), (0, 0, 0), screen, 80, 115)

            if click:

                startGame()

        else:
            pygame.draw.rect(screen, (136, 242, 210), buttonOne)
            draw_text('Play Game', pygame.font.SysFont(None, 30), (0, 0, 0), screen, 80, 115)

        if buttonTwo.collidepoint((mx,my)):

            pygame.draw.rect(screen, (76, 122, 108), buttonTwo)
            draw_text('Tutorial/Credits', pygame.font.SysFont(None, 30), (0, 0, 0), screen, 70, 215)

            if click:
                    
                credits()
        
        else:

            pygame.draw.rect(screen, (136, 242, 210), buttonTwo)
            draw_text('Tutorial/Credits', pygame.font.SysFont(None, 30), (0, 0, 0), screen, 70, 215)

        click = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()
                print("quit")

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                    
                    click = True

        pygame.display.update()
        clock.tick(60)
        

def startGame():
    game = Game(screen)
    game.set_up()

    while game.game_state == GameState.RUNNING:
        clock.tick(50)
        game.update()
        pygame.display.flip()

mainMenu()