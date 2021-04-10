import pygame
import config
from game_state import GameState
import sys

from game import Game

"""
First we initialize pygame and set up the clock. Then we set up the caption as well.
"""
pygame.init()

#Set up the screen
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

#Set up the name for the border of the application
pygame.display.set_caption("Get Hacked!")

#Set up the clock
clock = pygame.time.Clock()
 
#This is for drawing the text. A function taken from online

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#Code used from Tech with Tim
#Most times, font will be Arial

def fadeOut(): 

    fade = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    fade.fill((0,0,0))

    """
    A for loop, to change the alpha of the screen over time
    """
    for alpha in range(0, 60):

        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))

        pygame.display.update()
        pygame.time.delay(25)
"""
This is the loading screen

Created for aesthetic visual effects. Based on the fade out screen
"""
def loadingGame():

    loadingScreen = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    loadingScreen.fill((0,0,0))

    

    """
    Busy loop used for waiting the game loading screen

    Otherwise idk how to do it lmao
    """

    for i in range(0,150):

        #As usual, check for player events
        for event in pygame.event.get():

            #If we detect that a player has pressed the x button, we quit the application
            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()
                print("quit")

        #Draw the text for loading the game
        draw_text("Loading Game...", pygame.font.SysFont("Arial", 70), (255, 255, 255), screen, 80, 200)

    """
    Deals with the fading out of the screen.
    """

    for alpha in range(0, 40):

        #As usual, check for player events
        for event in pygame.event.get():

            #If we detect that a player has pressed the x button, we quit the application
            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()
                print("quit")

        #Set the alpha, and put the alpha on the screen so it has the fade
        loadingScreen.set_alpha(alpha)
        screen.blit(loadingScreen, (0,0))
        pygame.display.update()
        pygame.time.delay(85)

"""
Defines the credits for the game. Gives credits to the creators

As well as explaining the game.
"""
def credits():

    #Initialize the mouseClicked variable (which is click) to be false
    click = False

    # Initialize our running variable to be true, if we were to exit, this is set to false
    running = True

    #Load the character image from the folder imgs
    characterImage = pygame.image.load("imgs/character/tile000.png")
    
    #Main for loop for the options
    while running:

        #Fill the default screen to black, will be changed later
        screen.fill((0,0,0))

        #Blit the image of player onto the screend
        screen.blit(characterImage, (40,230))

        """
        Below defines the drawing text for the credits/tutorial part. Since we already have our function draw_text above, we just call it
        """
        draw_text('Tutorial and Credits/ How to play?', pygame.font.SysFont("Arial", 40), (255, 255, 255), screen, 20, 20)

        draw_text('Get Hacked! Is a python pygame based video game created by Jason, Deji, and Davis.', pygame.font.SysFont("Arial", 15), (255, 255, 255), screen, 20, 80)

        draw_text('This was made for the CPSC 329 class.', pygame.font.SysFont("Arial", 15), (255, 255, 255), screen, 20, 110)

        draw_text('The goal of this game is to run through and fight the bosses!', pygame.font.SysFont("Arial", 15), (255, 255, 255), screen, 20, 140)

        draw_text('To defeat the bosses, answer the questions and get it right!', pygame.font.SysFont("Arial", 15), (255, 255, 255), screen, 20, 170)

        draw_text("You can press escape in the game to pause and quit to main menu", pygame.font.SysFont("Arial", 15), (255, 255, 255), screen, 20, 200)

        draw_text("This is your character! He wants to learn about cybersecurity to protect himself", pygame.font.SysFont("Arial", 15), (255, 255, 255), screen, 20, 320)

        draw_text("Use WASD to move your character, and use the mouse button to interact with the questions!", pygame.font.SysFont("Arial", 15), (255, 255, 255), screen, 20, 350)

        """
        mx and my are where are mouse variables are. 
        """
        mx, my = pygame.mouse.get_pos()

        #Set up the button for the back button. 
        buttonBack = pygame.Rect(580,445,50,25)

        #Now, if we detect that our mouse if hovering over the position of the back button
        if buttonBack.collidepoint((mx,my)):

            #We first draw the text for back, and if its hovering over, then we will make the button darker as a highlight
            pygame.draw.rect(screen, (76, 122, 108), buttonBack)
            draw_text('Back', pygame.font.SysFont("Arial", 17), (0, 0, 0), screen, 587, 448)

            #If we click the back button, we exit outta that biotch
            if click:

                running = False

        #Else, we keep the button the default color. (No highlight)
        else:
            pygame.draw.rect(screen, (136, 242, 210), buttonBack)
            draw_text('Back', pygame.font.SysFont("Arial", 17), (0, 0, 0), screen, 587, 448)

        #Initialize the click variable to be false again.
        click = False

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

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                    
                    click = True

        #Update the screen!
        pygame.display.update()
        clock.tick(60)

"""
This is the main loop for the main menu. Each button has its own x and y position. We set up the buttons in the main menu, and then if we click on 
a button and it matches the x and y, then we go to that game loop. In each loop (like credits loop or game loop), if we press escape, then we "quit/break" and go back to main menu

Because in each loop, we have a loop. If we press escape inside one of those loops, like the game loop, etc, then we break out of the loop by setting the running condition to false.


"""
def mainMenu():

    #Get the image from the imgs folder for the background
    backGround = pygame.image.load("imgs/menuBackground.png")

    """
    We set click to false. The click boolean is to detect whether something has been clicked or not.
    """
    click = False

    """
    The main menu loop. 
    """
    while True:

        screen.fill((0,0,0))

        #Set the background
        screen.blit(backGround,(0,0))

        #Draw the Main Menu Text for GetHacked!
        draw_text('Get Hacked!', pygame.font.SysFont("Arial", 40), (255, 255, 255), screen, 20, 20)

        """
        mx and my are where are mouse variables are. 
        """
        mx, my = pygame.mouse.get_pos()

        """
        We initialize the start and credits button, to their respective x and y positions on the screen

        pygame.rect(xPos,yPos,Width,Height) is the format
        """
        buttonStart = pygame.Rect(20,100,180,50)
        buttonCredits = pygame.Rect(20,200,180,50)

        """
        This section is for detecting if our mouse is hovering over the buttons

        If it is, we run the respective codes
        """
        if buttonStart.collidepoint((mx,my)):

            """
            This section is for if the mouse is hovering over the start button

            If it is, then we highlight the button, by drawing it a lighter color, and then draw the same text!
            """
            pygame.draw.rect(screen, (76, 122, 108), buttonStart)
            draw_text('Play Game', pygame.font.SysFont("Arial", 20), (0, 0, 0), screen, 59, 115)

            if click:

                """
                If we click on the start button, then we fade out, load the game, and start the game

                otherwise we go to else, which is just not highlighting the button, and same text
                """

                #fadeOut()
                #loadingGame()
                startGame()

        else:
            pygame.draw.rect(screen, (136, 242, 210), buttonStart)
            draw_text('Play Game', pygame.font.SysFont("Arial", 20), (0, 0, 0), screen, 59, 115)

        """
        Same as above for the start button!

        We do and follow the same procedure
        """
        if buttonCredits.collidepoint((mx,my)):

            pygame.draw.rect(screen, (76, 122, 108), buttonCredits)
            draw_text('Tutorial/Credits', pygame.font.SysFont("Arial", 20), (0, 0, 0), screen, 43, 215)

            if click:
                    
                credits()
        
        else:

            pygame.draw.rect(screen, (136, 242, 210), buttonCredits)
            draw_text('Tutorial/Credits', pygame.font.SysFont("Arial", 20), (0, 0, 0), screen, 43, 215)

        #Initialize the click variable to be false
        click = False

        """
        This for loop is to check for events. We use a for loop because there can be events in the queue and we wanna get all of em
        """
        for event in pygame.event.get():
            
            """
            If we quit, then we exit outta pygame

            lata biotch
            """
            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()
                print("quit")

            #Otherwise if we click our mouse, then click becomes true
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                    
                    click = True

        #Update and display the screen
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