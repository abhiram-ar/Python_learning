from random import randint
import sys  # to exit the game when the player quits
from time import sleep

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats


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

        
        # -- code for full screen
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")


        # create an instance to store game statistics
        self.stats = GameStats(self)


        self.ship = Ship(self)
        # the Ship() requires on argument, which is an instance of AlienInvasion
        # The self argument here refers to the current instance of AlienInvasion
        # this parameter gives Ship acces to the game's resources
        

        self.bullets = pygame.sprite.Group()
        # store all the live bullets in a group
        # so we can manage the bullets that have already been fired.

        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # group to hold the fleet of aliens

    def run_game(self):
        """start the main loop for the game."""

        while True:
            # watch for keyboard and mouse events.
            # To make our program respond to events, we write this event loop to listen for
            # events and perform appropriate tasks depending on the kinds of events that occur
            self._check_events()

            # elemetst to only when player is playing
            if self.stats.game_active:
                # update the ship position if needed
                self.ship.update()
                
                #update the bullets location and manage out of screen bullets
                self._update_bullet()

                #move the alien ship
                self._update_aliens()
            
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
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


            
    def _check_keydown_events(self, event):
        """respond to keypress"""
        if event.key == pygame.K_RIGHT:
            # move the ship to right
            # untill the key is unpressed 
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        
        elif event.key == pygame.K_q:
                sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()



    def _check_keyup_events(self, event):  
        """respond to release"""  
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
            
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False



    def _fire_bullet(self):
        """create a new bullet and add it to the bullets group"""
        # limiting the no. of bullets a player can fire
        if len(self.bullets) <= self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    
    def _update_bullet(self):
        """update bullets and get rid of old bullets."""
        # When you call update() on a bullet group, 
        # the group automatically calls update() for each sprite in the group.
        self.bullets.update()

        # get rid of bullets that have dsappeared ie, out of window
        # this make sure we only use required memory as the bullets out of view continues to move
            # here we are modifying(deleteing) the contents of loop while it is running,
            # so we pass a copy of the bullet list
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        
        # check for any bullets that have hit aliens.
        # if so, get rid of the bullet and the alien.
        self._check_bullet_alien_collision()

        
        
        
    def _check_bullet_alien_collision(self):
        """respond to bullet alien collision."""

        collision = pygame.sprite.groupcollide(self.bullets, self. aliens, True, True)
            #it compares each bullet’s rect with each alien’s rect and returns a dictionary 
            #containing the bullets and aliens that have collided  
            # True True argument tell the pygame to delete the items that have collided

        
        # repopulatig the fleet if all aliens are dead
        if not self.aliens:
            # Distroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
    


    def _update_aliens(self):
        """
        check if the fleete is at edge 
        then update the position of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # look for alien-ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            # it loops through the group aliens and returns the first alien 
            # it finds that has collided with ship
            # if no collision return none and if condition dont execute
            self._ship_hit()

        # look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()



    def _ship_hit(self):
        """respond to the ship being hit by an alien."""

        if self.stats.ship_left > 0:
            # decrement ships left
            self.stats.ship_left -= 1

            # get rid of remainin bullets and aliens
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet and center the ship.
            self._create_fleet
            self.ship.center_ship()

            #pause
            sleep(0.5)
        
        else:
            self.stats.game_active = False


    def _check_aliens_bottom(self):
        """"check if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #treat this the same as if the ship got hit
                self._ship_hit()
                break



    def _create_fleet(self):
        """create a fleet of aliens."""

        # create an alien and find the number of aliens in a row.
        alien = Alien(self) # This alien won’t be part of the fleet
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2* alien_width) #cutting of some margin
        number_aliens_x = available_space_x // (2 * alien_width)  # taking margin of alien in to consideration

        # determine the number of rows of alien that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3* alien_height) - 4*ship_height
        number_rows = available_space_y // (2*ship_height)

        #create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._creat_alien(alien_number, row_number)
            


    def _creat_alien(self, alien_number, row_number):
        # create an alien and place it in the row.
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size

            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x

            alien.rect.y = alien_height + 2* alien_height * row_number

            # add it to the group
            self.aliens.add(alien)

    
    def _check_fleet_edges(self):
        """respond appropriatly if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1



    def _update_screen(self):
        """update images on the screen and flip to the new screen"""
        
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        # draw(): draws each element in the group at the position defined by its rect attribute. 
        # attribute: a surface on which to draw the elements from the group.

        # make the last drawn screen visible
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

