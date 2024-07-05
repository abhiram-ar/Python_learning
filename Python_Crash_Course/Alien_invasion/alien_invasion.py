import sys  # to exit the game when the player quits
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """overall class to manage the game assests and behavior."""

    def __init__(self):
        """initialize the game, and create game resources."""

        # initialize the background settings that pygame need to work properly
        pygame.init()
        self.settings = Settings()


        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # stored in object so it can be used in other class methods
        # The object we assigned to self.screen is called a surface. A surface in
        # Pygame is a part of the screen where a game element can be displayed.
        # Each element in the game, like an alien or a ship, is its own surface. The
        # surface returned by display.set_mode() represents the entire game window.
        # When we activate the game’s animation loop, this surface will be redrawn
        # on every pass through the loop, so it can be updated with any changes triggered by user input.

        pygame.display.set_caption("Alien Invasion")


        self.ship = Ship(self)
        # the Ship() requires on argument, which is an instance of AlienInvasion
        # The self argument here refers to the current instance of AlienInvasion
        # this parameter gives Ship acces to the game's resources



    def run_game(self):
        """start the main loop for the game."""

        while True:
            # watch for keyboard and mouse events.
            # To make our program respond to events, we write this event loop to listen for
            # events and perform appropriate tasks depending on the kinds of events that occur
            self._check_events()
            
            # Redraw the screen during each pass through the loop.
            self._update_screen()
            
        
    
    def _check_events(self):
        """respond to keypressess and mouse events"""
        # To access the events that Pygame detects, we’ll use the pygame.event.get() function
        # This function returns a list of events that have taken place since the last time this function was called.
        for event in pygame.event.get():
            # Any keyboard or mouse event will cause this for loop to run.
            if event.type == pygame.QUIT:
                sys.exit()

            #Each keypress is registered as a KEYDOWN event. 


    def _update_screen(self):
        """update images on the screen and flip to the new screen"""
        
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # make the last drawn screen visible
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

