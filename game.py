import pygame
import config
import sys
import math
from player import Player
from game_state import GameState

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
        self.detectBoss()

        self.render_map(self.screen)

        for object in self.objects:
            object.render(self.screen, self.camera)

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

    def detectBoss(self):
        print(self.player.position)

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
