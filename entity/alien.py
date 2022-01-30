import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class designed to manage the alien."""

    def __init__(self, alien_invasion_game):
        """Initialize Alien content."""

        super().__init__()

        self.screen = alien_invasion_game.screen
        self.settings = alien_invasion_game.settings

        # Loads the alien image and get its rectangle.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Set the alien to near the top left corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Use float point number to store alien position.
        self.alien_x = float(self.rect.x)

    def check_edges(self):
        """Return True if the alien is near the edge of the screen."""

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self, *args, **kwargs):
        """Update the alien position."""

        self.alien_x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.alien_x
