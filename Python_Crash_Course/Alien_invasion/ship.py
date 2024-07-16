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

        #load settings
        self.settings = ai_game.settings


        #load the ship image and get its rect.
        self.image = pygame.image.load(r"Python_Crash_Course\Alien_invasion\images\ship.bmp")  #retunrs a surace representing the ship
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom


        #store a decimal value for the ship's horizontal position
        # we can use a decimal value to set an attribute of rect, 
        # but the rect will only keep the integer portion of that value.
        # for storing position more accuratly we use x
        self.x = float(self.rect.x)


        # movement flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """update the ship's position based on the movement flag"""
                                            #handle overflow 
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.x += self.settings.ship_speed
        
        # not using elif for a special case! what is both keys are pressed
        # when both keys are pressed the ship will stop moving
        # this condition may occur when the player is switching the direction
        if self.moving_left and (self.rect.left > 0):
            self.x -= self.settings.ship_speed

        #update the rect object from self.x
        # only integer part of x is taken here
        # this is used to display the ships new position
        self.rect.x = int(self.x)


    def blitme(self):
        """draw the ship at is current location"""
        self.screen.blit(self.image, self.rect)  

        # blitme() method, draws the image to the screen at the position specified by self.rect. 


    def center_ship(self):
        """center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)



        
        