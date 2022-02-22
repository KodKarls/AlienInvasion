from utils.file_manager import FileManager


class GameStats:
    """A class to manage the game data stats."""

    def __init__(self, alien_invasion_game):
        """Initialize GameStats content."""

        self.settings = alien_invasion_game.settings
        self.reset_stats()

        # Run the game in a deactivated state.
        self.game_active = False

        # Create the file manager.
        self.file_manager = FileManager()

        # Load the best score from file.
        self.high_score = self.file_manager.load_data()

        # Create dynamic game data.
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def reset_stats(self):
        """Reset dynamic game data."""

        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
