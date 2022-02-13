import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class designed to manage the player."""

    def __init__(self, alien_invasion_game):
        """Initialize Ship content."""

        super().__init__()

        self.screen = alien_invasion_game.screen
        self.setting = alien_invasion_game.settings
        self.screen_rect = alien_invasion_game.screen.get_rect()

        # Loads the ship image and get its rectangle.
        self.image = pygame.image.load('res/images/ship.bmp')
        self.rect = self.image.get_rect()

        # Set the ship to mid-bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Use float point number to store ship position.
        self.ship_x = float(self.rect.x)

        # Options that indicate the movement of the ship.
        self.moving_right = False
        self.moving_left = False

    def update(self, *args, **kwargs):
        """Update the ship position."""

        # Updating the value of the X coordinate of the ship, not its rectangle.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.ship_x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.ship_x -= self.setting.ship_speed

        # Update rect object based on self.ship_x value.
        self.rect.x = self.ship_x

    def display(self):
        """Display the ship."""

        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Set the ship to mid-bottom of the screen."""

        self.rect.midbottom = self.screen_rect.midbottom
        self.ship_x = float(self.rect.x)
