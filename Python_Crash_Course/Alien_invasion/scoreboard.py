import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """A class tp report scoring information"""
    def __init__(self, ai_game):
        """initialize scorekeeping attributes"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font settings for scoring information
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        #prepre the initail score image
        self.prep_score()

        #preapare the high score
        self.prep_high_score()

        self.prep_level()

        #ship lifes
        self.prep_ships()


    def prep_score(self):
        """turn the score into a renddered image"""

        #most arcade has score in a multiple of 10 so we do some rounding
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score) # adding comma, in the numbers system

        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """turn high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # center the high score at the top od the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    
    def check_high_score(self):
        """checl to see if there's a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()


    def prep_level(self):
        """trun the level into a rendered image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        #positon the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10



    def prep_ships(self):
        """show how many ships are left"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def show_score(self):
        """Draw score to the screen and ships to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        self.ships.draw(self.screen)




