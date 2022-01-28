from utils.file_manager import FileManager

class GameStats():
    """Monitorowanie danych statystycznych w grze "Inwazja obcych"."""

    def __init__(self, alien_invasion_game):
        """Inicjalizacja danych statystycznych."""
        self.settings = alien_invasion_game.settings
        self.reset_stats()

        # Uruchomienie gry "Inwazja obcych" w stanie aktywnym.
        self.game_active = False

        # Creating the file manager.
        self.file_manager = FileManager()

        # Load best score from file.
        self.high_score = self.file_manager.load_data()

    def reset_stats(self):
        """ Inicjalizacja danych statystycznych, które mogą zmieniać
        się w trakcie gry."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
