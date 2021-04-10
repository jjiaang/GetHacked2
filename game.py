import pygame
import config
import sys
import math
from player import Player
from game_state import GameState
from quiz import Quiz

"""
Define the Game class
"""
class Game:

    """
    Begin with init, by defining our screen, objects, our game_state (which is an enum)

    the map, and the camera
    """

    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE
        self.map = []
        self.camera = [0, 0]
        self.clock = pygame.time.Clock()

    #This is for when we set up the game. We spawn the player in a coordinate, and then run the game
    def set_up(self):
        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        self.game_state = GameState.RUNNING

        self.load_map("01")

    def update(self):
        self.screen.fill(config.BLACK)
        self.handle_events()

        self.render_map(self.screen)

        for object in self.objects:
            object.render(self.screen, self.camera)

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def startQuizOne(self):

        runningQuiz = True

        click = False

        score = 0

        round = 1

        while runningQuiz:

            self.screen.fill((0, 0, 0))

            #Check for events
            for event in pygame.event.get():

                #If the event is quit, then we exit
                if event.type == pygame.QUIT:

                    runningQuiz = False
                    pygame.quit()
                    sys.exit()
                    print("quit")

                #If we escape, return back to the game
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_ESCAPE:

                        runningQuiz = False

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if event.button == 1:
                        
                        click = True

            """
            mx and my are where are mouse variables are. 
            """
            mx, my = pygame.mouse.get_pos()

            #Setting up the quiz buttons
            buttonA = pygame.Rect(10,100,500,125)
            buttonB = pygame.Rect(10,300,500,125)

            buttonC = pygame.Rect(750,100,500,125)
            buttonD = pygame.Rect(750,300,500,125)

            if round == 1:
                #Handling the UI for the button clicks and presses
                if buttonA.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("Falsification of data and data authentication", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 150)

                    if click:

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("Falsification of data and data authentication", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 150)

                if buttonB.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("Collection of information such as passwords", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 350)

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("Collection of information such as passwords", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 350)

                if buttonC.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("Information and messages in the system are acquired", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 750, 150)

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("Information and messages in the system are acquired", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 750, 150)

                if buttonD.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("System resources are not changed", pygame.font.SysFont("Arial", 16), (105,105,105), self.screen, 750, 350)

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("System resources are not changed", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 750, 350)

                #Initialize the click variable to be false again.
                click = False

                #Display Text for questions
                self.draw_text("Question " + str(round), pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 15)
                self.draw_text("In cybersecurity there are two types of attacks: passive attack and active attacks. Passive attack involves eavesdropping. What involves active attack?", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 40)

            if round == 2:
                #Handling the UI for the button clicks and presses
                if buttonA.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("That contents have not been altered", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 150)

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("That contents have not been altered", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 150)

                if buttonB.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("That the source is authentic", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 350)

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("That the source is authentic", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 350)

                if buttonC.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("That time frame is the same for transmitting information ", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 750, 150)

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("That time frame is the same for transmitting information ", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 750, 150)

                if buttonD.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("That contents have not been altered and that the source is authentic", pygame.font.SysFont("Arial", 16), (105,105,105), self.screen, 750, 350)

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("That contents have not been altered and that the source is authentic", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 750, 350)

                #Initialize the click variable to be false again.
                click = False

                #Display Text for questions
                self.draw_text("Question " + str(round), pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 15)
                self.draw_text("Message or data authentication is a procedure that allows communicating parties to verify that received or stored messages are authentic.", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 40)
                self.draw_text("What are the two important aspects that needs to be verified of the contents?", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 60)

            click = False

            pygame.display.update()
            self.clock.tick(60)

    """
    Detect if the player is at the correct position in front of the boss

    We also have to check if its in the range of the map
    """
    def detectBoss(self):
        print(self.player.position)

        #Check to see if the x value is out of bounds
        if (self.player.position[0] - 1 < 0 or self.player.position[0] + 1 > (len(self.map[0]) - 1)):
            return False

        #Check to see if the y value is out of bounds
        if self.player.position[0] - 1 < 0 or self.player.position[0] > (len(self.map) - 1):
            return False
        
        """
        If they are not out of bounds, then we return true if we detected a boss

        Then we check in a 360 radius to see if we have a boss around us
        """
        if (self.map[self.player.position[1]][self.player.position[0] + 1] == 'A' or 
        self.map[self.player.position[1]][self.player.position[0] - 1] == 'A' or 
        self.map[self.player.position[1] + 1][self.player.position[0]] == 'A' or 
        self.map[self.player.position[1] - 1][self.player.position[0]] == 'A'):
        
            print(self.map[self.player.position[1]][self.player.position[0]])
            return True

    """
    A function that handles events. Handles events such as if we quit, escape, move up down side, etc
    """
    def handle_events(self):

        """
        A for loop for detecting events

        Because we see that there can be multiple events
        """
        for event in pygame.event.get():

            #If we quit/ press the X button, then we quit and exit the game
            if event.type == pygame.QUIT:

                self.game_state = GameState.ENDED
                pygame.quit()
                sys.exit()

            #Handle key pressing events
            elif event.type == pygame.KEYDOWN:

                #Handles the escape button
                if event.key == pygame.K_ESCAPE:

                    self.game_state = GameState.ENDED

                elif event.key == pygame.K_w: # up

                    playerMovement = self.player.updateWalk("UP")
                    self.player.image = pygame.transform.scale(playerMovement, (config.SCALE, config.SCALE))
                    self.move_unit(self.player, [0, -1])

                elif event.key == pygame.K_s: # down

                    playerMovement = self.player.updateWalk("DOWN")

                    self.player.image = pygame.transform.scale(playerMovement, (config.SCALE, config.SCALE))
                    self.move_unit(self.player, [0, 1])

                elif event.key == pygame.K_a: # left

                    playerMovement = self.player.updateWalk("LEFT")
                    self.player.image = pygame.transform.scale(playerMovement, (config.SCALE, config.SCALE))

                    self.move_unit(self.player, [-1, 0])

                elif event.key == pygame.K_d: # right

                    playerMovement = self.player.updateWalk("RIGHT")
                    self.player.image = pygame.transform.scale(playerMovement, (config.SCALE, config.SCALE))

                    self.move_unit(self.player, [1, 0])
                
                elif event.key == pygame.K_SPACE: #Spacebar for boss

                    self.startQuizOne()

                    if self.detectBoss():
                        print("Ok")

    """
    This function is for loading the map and creating it.
    """
    def load_map(self, file_name):

        """
        Our maps are shown a text file

        So basically, the layout of the map will be in the format of a text file
        """
        with open('maps/' + file_name + ".txt") as map_file:

            #Iterate through each line
            for line in map_file:

                tiles = []

                #Iterate through each entry of each line
                for i in range(0, len(line) - 1, 2):

                    #Append the selected map description to the tile array
                    tiles.append(line[i])

                self.map.append(tiles)
            
            #Print the map to the console for testing
            print(self.map)

    """
    This function is for rendering the map
    """
    def render_map(self, screen):

        #Determine where the camera should be first
        self.determine_camera()

        y_pos = 0

        #Go through the grid line by line
        for line in self.map:

            x_pos = 0

            #Go through each individual tile
            for tile in line:

                #Find the corresponding thing to go with, for example G for grass, W for water
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos * config.SCALE, y_pos * config.SCALE - (self.camera[1] * config.SCALE), config.SCALE, config.SCALE)
                #Draw the image onto the rectangle (the map tiles)
                screen.blit(image, rect)
                x_pos = x_pos + 1

            y_pos = y_pos + 1

    """
    This function is for moving the player

    Player position is based on each tile, so it is a one dimensional array, with position[0] being X and position[1] being Y

    Meanwhile, we know that the map is a 2d array, with map[0][z] being the first row, zth column, and vice versa

    X position for the player refers to the column the player is on, while the Y position is the row

    If a player is at position X Y, then the corresponding map entry would be map[Y][X]
    """
    def move_unit(self, unit, position_change):

        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]

        """
        Handles out of bound errors
        """
        if new_position[0] < 0 or new_position[0] > (len(self.map[0]) - 1):
            return

        if new_position[1] < 0 or new_position[1] > (len(self.map) - 1):
            return

        """
        If we detect water, a rock, or a boss

        We break out. Will add more later
        """
        if (self.map[new_position[1]][new_position[0]] == "W" or self.map[new_position[1]][new_position[0]] == "A" 
        or self.map[new_position[1]][new_position[0]] == "R"):
            return
            

        unit.update_position(new_position)

    """
    This is for controlling the player camera

    If the player exceeds the maximum y position, then we move the camera
    """
    def determine_camera(self):

        max_y_position = len(self.map) - config.SCREEN_HEIGHT / config.SCALE
        y_position = self.player.position[1] - math.ceil(round(config.SCREEN_HEIGHT/ config.SCALE / 2))

        if y_position <= max_y_position and y_position >= 0:

            self.camera[1] = y_position

        elif y_position < 0:

            self.camera[1] = 0

        else:

            self.camera[1] = max_y_position


#A python dict/hashmap for the types of tiles in the game, they should be 64x64
map_tile_image = {

    "G" : pygame.transform.scale(pygame.image.load("imgs/grass1.png"), (config.SCALE, config.SCALE)),
    "W": pygame.transform.scale(pygame.image.load("imgs/water.png"), (config.SCALE, config.SCALE)),
    "A" : pygame.transform.scale(pygame.image.load("imgs/boss1Tile.png"),(config.SCALE, config.SCALE)),
    "R" : pygame.transform.scale(pygame.image.load("imgs/rock1Tile.png"),(config.SCALE, config.SCALE))

}
