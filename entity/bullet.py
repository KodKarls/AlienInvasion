import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class designed to manage the bullet fired by the ship."""

    def __init__(self, alien_invasion_game):
        """Initialize Ship content."""

        super().__init__()

        self.screen = alien_invasion_game.screen
        self.settings = alien_invasion_game.settings
        self.color = self.settings.bullet_color

        # Create the bullet rectangle at point (0, 0) and then set the bullet on the top-middle of the ship.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = alien_invasion_game.ship.rect.midtop

        # Use float point number to store bullet position.
        self.bullet_y = float(self.rect.y)

    def update(self, *args, **kwargs):
        """Update the bullet position."""

        # Update bullet position and then its rectangle.
        self.bullet_y -= self.settings.bullet_speed
        self.rect.y = self.bullet_y

    def draw_bullet(self):
        """Display the bullet."""

        pygame.draw.rect(self.screen, self.color, self.rect)
