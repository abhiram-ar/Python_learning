class GameStats:
    """track statistics for alien invasion"""

    def __init__(self, ai_game):
        """initialize staticstics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # start alien invasion in a active state
        self.game_active = False

        # High score should never be reset
        self.high_score =0

    
    def reset_stats(self):
        """initialize staticstics that can change during the game"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
