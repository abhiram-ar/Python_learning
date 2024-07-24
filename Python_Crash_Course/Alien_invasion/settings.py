class Settings:
    """A class to store all settings for alien invasion"""

    def __init__(self):
        """initialize the game's static settings"""

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # ship setting
        self.ship_limit = 2

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Alien settings
        self.fleet_drop_speed = 10
        


        # how quicky the game speed up
        self.speedup_scale = 1.2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initiaize settings that change thoroughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 0.3

        self.fleet_direction = 1  # move left -1, move right +1

    
    def _increase_speed(self):
        """increse speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

