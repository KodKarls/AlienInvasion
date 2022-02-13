import pygame.font
from pygame.sprite import Group

from entity.ship import Ship

class Scoreboard:
    """A class to manage scoreboard."""

    def __init__(self, alien_invasion_game):
        """Initialize Scoreboard content."""

        self.alien_invasion_game = alien_invasion_game
        self.screen = alien_invasion_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = alien_invasion_game.settings
        self.stats = alien_invasion_game.stats

        # Font settings.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(self.settings.font_name, self.settings.font_point_size)

        # Prepare data for showing on the screen.
        self.score_image = None
        self.score_rect = None
        self.prep_score()

        self.high_score_image = None
        self.high_score_rect = None
        self.prep_high_score()

        self.level_image = None
        self.level_rect = None
        self.prep_level()

        self.ships = Group()
        self.prep_ships()

    def prep_score(self):
        """Convert the score to a generated image."""

        # Format the score.
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.background_color)

        # Set the score position in the right-top corner of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Convert the best score to a generated image."""

        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.background_color)

        # Set the best score position in the middle-top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Convert the level to a generated image."""

        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.background_color)

        # Set the level position under the current score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Prepare images of the remaining ship lives."""

        # Clear the previous lives images.
        self.ships.empty()

        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.alien_invasion_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def check_high_score(self):
        """Check if player achieve the new best score."""

        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_data(self):
        """Display score, the best score and remaining ship lives on the screen."""

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
