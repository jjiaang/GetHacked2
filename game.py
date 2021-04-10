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
        self.level = 0

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

    def incorrectScreen(self,link):

        runningScreen = True

        click = False

        while runningScreen:

            self.screen.fill((0, 0, 0))

            buttonNext = pygame.Rect(10,700,500,125)

            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():
                #If the event is quit, then we exit
                if event.type == pygame.QUIT:

                    runningScreen = False
                    pygame.quit()
                    sys.exit()
                    print("quit")
                
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if event.button == 1:
                        
                        click = True

            self.draw_text("Whoops! That is incorrect, here is a link to help you out", pygame.font.SysFont("Arial", 20), (255, 255, 255), self.screen, 80, 100)
            self.draw_text(link, pygame.font.SysFont("Arial", 20), (255, 255, 255), self.screen, 80, 120)

            if buttonNext.collidepoint((mx,my)):
                pygame.draw.rect(self.screen, (82, 46, 78), buttonNext)
                self.draw_text("Next Question", pygame.font.SysFont("Arial", 30), (255, 255, 255), self.screen, 10, 750)

                if click:

                    runningScreen = False

            else:

                pygame.draw.rect(self.screen, (112, 64, 107), buttonNext)
                self.draw_text("Next Question", pygame.font.SysFont("Arial", 30), (255, 255, 255), self.screen, 10, 750)

            click = False

            pygame.display.update()
            self.clock.tick(60)

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

            buttonC = pygame.Rect(10,500,500,125)
            buttonD = pygame.Rect(10,700,500,125)

            if round == 1:
                #Handling the UI for the button clicks and presses

                #Correct Answer
                if buttonA.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("Falsification of data and data authentication", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 150)

                    if click:

                        round += 1
                        score += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("Falsification of data and data authentication", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 150)

                if buttonB.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("Collection of information such as passwords", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 350)

                    if click:

                        self.incorrectScreen("https://www.geeksforgeeks.org/difference-between-active-attack-and-passive-attack/")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("Collection of information such as passwords", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 350)

                if buttonC.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("Information and messages in the system are acquired", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 550)

                    if click:

                        self.incorrectScreen("https://www.geeksforgeeks.org/difference-between-active-attack-and-passive-attack/")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("Information and messages in the system are acquired", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 550)

                if buttonD.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("System resources are not changed", pygame.font.SysFont("Arial", 16), (105,105,105), self.screen, 10, 750)

                    if click:

                        self.incorrectScreen("https://www.geeksforgeeks.org/difference-between-active-attack-and-passive-attack/")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("System resources are not changed", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 750)

                #Initialize the click variable to be false again.
                click = False

                #Display Text for questions
                self.draw_text("Question " + str(round), pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 15)
                self.draw_text("In cybersecurity there are two types of attacks: passive attack and active attacks. Passive attack involves eavesdropping. What involves active attack?", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 40)

            if round == 2:

                #Display Text for questions
                self.draw_text("Question " + str(round), pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 15)
                self.draw_text("Message or data authentication is a procedure that allows communicating parties to verify that received or stored messages are authentic. ", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 40)
                self.draw_text("What are the two important aspects that needs to be verified of the contents?", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 60)

                #Handling the UI for the button clicks and presses
                if buttonA.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("That contents have not been altered", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 150)

                    if click:

                        self.incorrectScreen("https://www.logsign.com/blog/what-are-authentication-protocols-in-cryptography/ ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("That contents have not been altered", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 150)

                if buttonB.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("That the source is authentic", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 350)

                    if click:

                        self.incorrectScreen("https://www.logsign.com/blog/what-are-authentication-protocols-in-cryptography/ ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("That the source is authentic", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 350)

                if buttonC.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("That time frame is the same for transmitting information ", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 550)

                    if click:

                        self.incorrectScreen("https://www.logsign.com/blog/what-are-authentication-protocols-in-cryptography/ ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("That time frame is the same for transmitting information ", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 550)

                #Correct Answer
                if buttonD.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("That contents have not been altered and that the source is authentic", pygame.font.SysFont("Arial", 16), (105,105,105), self.screen, 10, 750)

                    if click:

                        round += 1
                        score += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("That contents have not been altered and that the source is authentic", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 750)

                click = False

            if round == 3:

                #Display Text for questions
                self.draw_text("Question " + str(round), pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 15)
                self.draw_text("Which one statement about the one-way hash function used for message authentication is correct?", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 40)

                #Handling the UI for the button clicks and presses
                if buttonA.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("Accepts the same sized messages as input and produces the same sized message digest of some fixed length", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 150)

                    if click:

                        self.incorrectScreen("https://en.wikipedia.org/wiki/Cryptographic_hash_function ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("Accepts the same sized messages as input and produces the same sized message digest of some fixed length", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 150)

                if buttonB.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("Accepts variable sized messages as input and produces a variable sized message digest of some fixed length", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 350)

                    if click:

                        self.incorrectScreen("https://en.wikipedia.org/wiki/Cryptographic_hash_function ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("Accepts variable sized messages as input and produces a variable sized message digest of some fixed length", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 350)

                if buttonC.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("Accepts the same sized messages as input and produces a variable sized message digest of some fixed length", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 550)

                    if click:

                        self.incorrectScreen("https://en.wikipedia.org/wiki/Cryptographic_hash_function ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("Accepts the same sized messages as input and produces a variable sized message digest of some fixed length", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 550)

                #Correct Answer
                if buttonD.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("Accepts variable sized messages as input and produces a fixed-sized message digest of some fixed length", pygame.font.SysFont("Arial", 16), (105,105,105), self.screen, 10, 750)

                    if click:

                        round += 1
                        score += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("Accepts variable sized messages as input and produces a fixed-sized message digest of some fixed length", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 750)

                #Initialize the click variable to be false again.
                click = False

            if round == 4:

                #Display Text for questions
                self.draw_text("Question " + str(round), pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 15)
                self.draw_text("What properties describe a hash function which is referred to as collision resistant or as strong collision resistant?", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 40)

                #Handling the UI for the button clicks and presses

                #Correct Answer
                if buttonA.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("It is a hash function where it is computationally infeasible to find any pair (x,y) such that H(x) = H(y)", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 150)

                    if click:

                        round += 1
                        score += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("It is a hash function where it is computationally infeasible to find any pair (x,y) such that H(x) = H(y)", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 150)

                if buttonB.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("For any given block x, it is computationally infeasible to find y is not equal to x with H(y) = H(x)", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 350)

                    if click:

                        self.incorrectScreen("https://en.wikipedia.org/wiki/Cryptographic_hash_function ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("For any given block x, it is computationally infeasible to find y is not equal to x with H(y) = H(x)", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 350)

                if buttonC.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("It is a hash function which produces the same output for all inputs", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 550)

                    if click:

                        self.incorrectScreen("https://en.wikipedia.org/wiki/Cryptographic_hash_function ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("It is a hash function which produces the same output for all inputs", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 550)

                if buttonD.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("It is a hash function which algorithm is hard to understand despite producing the same output for different inputs", pygame.font.SysFont("Arial", 16), (105,105,105), self.screen, 10, 750)

                    if click:

                        self.incorrectScreen("https://en.wikipedia.org/wiki/Cryptographic_hash_function ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("It is a hash function which algorithm is hard to understand despite producing the same output for different inputs", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 750)

                click = False

            if round == 5:

                #Load the image
                round5Image = pygame.image.load("imgs/Q1P3.png")

                #Blit the image
                self.screen.blit(round5Image, (700,230))

                #Display Text for questions
                self.draw_text("Question " + str(round), pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 15)
                self.draw_text("Message Authentication Using a Message Authentication Code. What ingredients of this scheme are represented by numbers?", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 40)

                #Handling the UI for the button clicks and presses
                if buttonA.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("Ciphertext, 2 – Key, 3 – Compare ", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 150)

                    if click:

                        self.incorrectScreen("https://en.wikipedia.org/wiki/Message_authentication_code ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("Ciphertext, 2 – Key, 3 – Compare ", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 150)

                #Correct Answer
                if buttonB.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("Message, 2 – Key, 3 – Compare", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 350)

                    if click:

                        round += 1
                        score += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("Message, 2 – Key, 3 – Compare", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 350)

                if buttonC.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("Ciphertext, 2 – Key, 3 – Authentication", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 550)

                    if click:

                        self.incorrectScreen("https://en.wikipedia.org/wiki/Message_authentication_code ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("Ciphertext, 2 – Key, 3 – Authentication", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 550)

                if buttonD.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("Message, 2 – Compare, 3 – Key", pygame.font.SysFont("Arial", 16), (105,105,105), self.screen, 10, 750)

                    if click:

                        self.incorrectScreen("https://en.wikipedia.org/wiki/Message_authentication_code ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("Message, 2 – Compare, 3 – Key", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 750)

                #Initialize the click variable to be false again.
                click = False

            if round == 6:

                #Load the image
                round5Image = pygame.image.load("imgs/Q1P6.png")

                #Blit the image
                self.screen.blit(round5Image, (650,230))

                #Display Text for questions
                self.draw_text("Question " + str(round), pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 15)
                self.draw_text("Public-Key Cryptography. What ingredients of this scheme are represented by numbers?", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 40)

                #Handling the UI for the button clicks and presses

                #Correct Answer
                if buttonA.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("Public, 2 – Private, 3 – Ciphertext, 4 – Encryption, 5 – Decryption ", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 150)

                    if click:

                        round += 1
                        score += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("Public, 2 – Private, 3 – Ciphertext, 4 – Encryption, 5 – Decryption ", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 150)

                if buttonB.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("Private, 2 – Public, 3 – Ciphertext, 4 – Decryption, 5 – Encryption", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 350)

                    if click:

                        self.incorrectScreen("https://sectigo.com/resource-library/public-key-vs-private-key")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("Private, 2 – Public, 3 – Ciphertext, 4 – Decryption, 5 – Encryption", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 350)

                if buttonC.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("Public, 2 – Private, 3 – Plaintext, 4 – Decryption, 5 – Encryption", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 550)

                    if click:

                        self.incorrectScreen("https://sectigo.com/resource-library/public-key-vs-private-key")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("Public, 2 – Private, 3 – Plaintext, 4 – Decryption, 5 – Encryption", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 550)

                if buttonD.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("Encryption, 2 – Decryption, 3 – Ciphertext, 4 – Public, 5 – Private", pygame.font.SysFont("Arial", 16), (105,105,105), self.screen, 10, 750)

                    if click:

                        self.incorrectScreen("https://sectigo.com/resource-library/public-key-vs-private-key")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("Encryption, 2 – Decryption, 3 – Ciphertext, 4 – Public, 5 – Private", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 750)

                #Initialize the click variable to be false again.
                click = False

            if round == 7:

                #Display Text for questions
                self.draw_text("Question " + str(round), pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 15)
                self.draw_text("In public-key cryptography all participants have access to public keys and private keys are generated locally by each participant. ", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 40)
                self.draw_text("So, let’s say if Bob wishes to send a private message to Alice, Bob encrypts the message using Alice’s public key and when Alice receives the message, ", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 60)
                self.draw_text("she decrypts it using her private key. For how long is this communication secure?", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 80)

                #Handling the UI for the button clicks and presses
                if buttonA.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("As long as Bob protects his public key", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 150)

                    if click:

                        self.incorrectScreen("https://www.securew2.com/blog/what-is-public-key-cryptography ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("As long as Bob protects his public key", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 150)

                if buttonB.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("As long as Bob and Alice protect their keys", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 350)

                    if click:

                        self.incorrectScreen("https://www.securew2.com/blog/what-is-public-key-cryptography ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("As long as Bob and Alice protect their keys", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 350)

                if buttonC.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("This communication is not secure", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 550)

                    if click:

                        self.incorrectScreen("https://www.securew2.com/blog/what-is-public-key-cryptography ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("This communication is not secure", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 550)

                #Correct Answer
                if buttonD.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("As long as Alice protects her private key", pygame.font.SysFont("Arial", 16), (105,105,105), self.screen, 10, 750)

                    if click:

                        round += 1
                        score += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("As long as Alice protects her private key", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 750)

                #Initialize the click variable to be false again.
                click = False

            if round == 8:

                #Display Text for questions
                self.draw_text("Question " + str(round), pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 15)
                self.draw_text("In public-key encryption only the intended recipient should be able to decrypt the ciphertext ", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 40)
                self.draw_text("because only the intended recipient is in possession of the required private key. What property does this sentence define? ", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 60)

                #Handling the UI for the button clicks and presses
                if buttonA.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("Data integrity", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 150)

                    if click:

                        self.incorrectScreen("https://en.wikipedia.org/wiki/Public-key_cryptography")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("Data integrity", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 150)

                if buttonB.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("Security", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 350)

                    if click:

                        self.incorrectScreen("https://en.wikipedia.org/wiki/Public-key_cryptography")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("Security", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 350)

                #Correct Answer
                if buttonC.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("Confidentiality", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 550)

                    if click:

                        round += 1
                        score += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("Confidentiality", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 550)

                if buttonD.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("Verification", pygame.font.SysFont("Arial", 16), (105,105,105), self.screen, 10, 750)

                    if click:

                        self.incorrectScreen("https://en.wikipedia.org/wiki/Public-key_cryptography")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("Verification", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 750)

                #Initialize the click variable to be false again.
                click = False

            if round == 9:

                #Display Text for questions
                self.draw_text("Question " + str(round), pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 15)
                self.draw_text("In public-key encryption, if a user is able to successfully recover the plaintext from Bob’s ciphertext using Bob’s public key, ", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 40)
                self.draw_text("this indicates that only Bob could have encrypted the plaintext. What property does this sentence define?", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 60)

                #Handling the UI for the button clicks and presses

                #Correct Answer
                if buttonA.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("Authentication and/or data integrity", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 150)

                    if click:

                        round += 1
                        score += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("Authentication and/or data integrity", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 150)

                if buttonB.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("Confidentiality", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 350)

                    if click:

                        self.incorrectScreen("https://www.ssh.com/manuals/server-zos-product/55/chooseauth-publickey.html ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("Confidentiality", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 350)

                if buttonC.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("Security", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 550)

                    if click:

                        self.incorrectScreen("https://www.ssh.com/manuals/server-zos-product/55/chooseauth-publickey.html ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("Security", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 550)

                if buttonD.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("Protection", pygame.font.SysFont("Arial", 16), (105,105,105), self.screen, 10, 750)

                    if click:

                        self.incorrectScreen("https://www.ssh.com/manuals/server-zos-product/55/chooseauth-publickey.html ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("Protection", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 750)

                #Initialize the click variable to be false again.
                click = False

            if round == 10:

                #Display Text for questions
                self.draw_text("Question " + str(round), pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 15)
                self.draw_text("Which one of the public-key requirements is not necessary for all public-key applications?", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 20, 40)

                #Handling the UI for the button clicks and presses

                if buttonA.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("It is computationally infeasible for an opponent, knowing the public key, and a ciphertext, to recover the original message", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 150)

                    if click:

                        self.incorrectScreen("https://binaryterms.com/public-key-cryptography.html ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonA)
                    self.draw_text("It is computationally infeasible for an opponent, knowing the public key, and a ciphertext, to recover the original message", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 150)

                #Correct Answer
                if buttonB.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("Either of the two related keys can be used for encryption, with the other used for decryption", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 350)

                    if click:

                        round += 1
                        score += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonB)
                    self.draw_text("Either of the two related keys can be used for encryption, with the other used for decryption", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 350)

                if buttonC.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("It is computationally easy for a sender A, knowing the public key and the message to be encrypted, to generate the corresponding ciphertext", pygame.font.SysFont("Arial", 16), 	(105,105,105), self.screen, 10, 550)

                    if click:

                        self.incorrectScreen("https://binaryterms.com/public-key-cryptography.html ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonC)
                    self.draw_text("It is computationally easy for a sender A, knowing the public key and the message to be encrypted, to generate the corresponding ciphertext", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 550)

                if buttonD.collidepoint((mx,my)):

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("It is computationally easy for the receiver B to decrypt the resulting ciphertext using the private key to recover the original message", pygame.font.SysFont("Arial", 16), (105,105,105), self.screen, 10, 750)

                    if click:

                        self.incorrectScreen("https://binaryterms.com/public-key-cryptography.html ")

                        round += 1

                else:

                    pygame.draw.rect(self.screen, (15, 15, 15), buttonD)
                    self.draw_text("It is computationally easy for the receiver B to decrypt the resulting ciphertext using the private key to recover the original message", pygame.font.SysFont("Arial", 16), (255, 255, 255), self.screen, 10, 750)

                #Initialize the click variable to be false again.
                click = False
                

            click = False

            

            if round > 10:
                return score

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

                    if self.detectBoss():

                        if self.level == 0:
                            result = self.startQuizOne()

                            print(result)

                            if result >= 6:
                                self.level += 1

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
