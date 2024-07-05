from math import fabs
import pygame

class Ship:
    """a class to manage the ship"""

    def __init__(self, ai_game):
        """Intialize the ship and set its starting position

            arg : ai_game , this give class ship the access to all game resources defined in ai
        """

        # pygame treats all game elements like reactangles("rects")
        # this treatment is efficient to compute collison
        # we will treat ship and the screen as rectangles in this class.
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()


        #load the ship image and get its rect.
        self.image = pygame.image.load(r"Python_Crash_Course\Alien_invasion\images\ship.bmp")  #retunrs a surace representing the ship
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom


        # movement flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """update the ship's position based on the movement flag"""
        if self.moving_right:
            self.rect.x += 1
        
        # not using elif for a special case! what is both keys are pressed
        # when both keys are pressed the ship will stop moving
        # this condition may occur when the player is switching the direction
        if self.moving_left:
            self.rect.x -=1 

    def blitme(self):
        """draw the ship at is current location"""
        self.screen.blit(self.image, self.rect)  

        # blitme() method, draws the image to the screen at the position specified by self.rect. 



        
        